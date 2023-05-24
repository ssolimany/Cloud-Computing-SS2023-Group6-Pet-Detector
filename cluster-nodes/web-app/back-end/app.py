from flask import Flask, request, jsonify
from io import BytesIO
from minio import Minio
import datetime
import base64

# MinIO server configuration
MINIO_ENDPOINT = "192.168.178.20:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
MINIO_BUCKET_NAME = "detections"

# Initialize MinIO client
minio_client = Minio(
    endpoint=MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

# Create 'MINIO_BUCKET_NAME' bucket if it doesn't exist in MinIO.
found = minio_client.bucket_exists(MINIO_BUCKET_NAME)
if not found:
    print(f"Bucket '{MINIO_BUCKET_NAME}' doesn't exist, creating it now...")
    minio_client.make_bucket(MINIO_BUCKET_NAME)
    print(f"Created Bucket '{MINIO_BUCKET_NAME}'")
else:
    print(f"Bucket '{MINIO_BUCKET_NAME}' already exists")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_latest_detections():
    """
    This Endpoint retrieves the 9 latest detection images together with their confidences and detections metadata from MinIO,
    encodes the image in base64 and returns it with the metadata in JSON
    """
    
    try:
        objects = minio_client.list_objects(MINIO_BUCKET_NAME, recursive=True)

        # Sort objects by 'last_modified' attribute in descending order
        sorted_objects = sorted(objects, key=lambda obj: obj.last_modified, reverse=True)

        # Retrieve up to 9 latest objects
        latest_objects = sorted_objects[:9]

        response_data = []

        for obj in latest_objects:
            response = minio_client.get_object(MINIO_BUCKET_NAME, obj.object_name)

            # Read the object data
            object_data = response.read()

            # Convert the object data to a base64 encoded string
            base64_encoded_data = base64.b64encode(object_data).decode('utf-8')

            # Retrieve metadata
            confidences = response.headers.get('x-amz-meta-confidences')
            detections = response.headers.get('x-amz-meta-detections')

            # Create a dictionary for each object with the encoded data and metadata
            object_dict = {
                'image_data': base64_encoded_data,
                'confidences': confidences,
                'detections': detections
            }

            response_data.append(object_dict)

        # Create a JSON response with the list of objects
        json_response = jsonify(response_data)

        return json_response
    
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/upload/jpeg", methods=["POST"])
def upload_detections():
    """
    This Endpoint decodes the base64 encoded image and uploads it as
    jpeg with the detections and confidences as metadata to MinIO
    """
    
    try:
        # Retrieve base64 encoded image data and decode it
        base64_encoded_image = request.json.get("image")
        decoded_image = base64.b64decode(base64_encoded_image)
    
        # Retrieve image metadata
        image_metadata = {
            "detections" : request.json.get("detections"),
            "confidences" : request.json.get("confidences")
        }

        # Generate timestamp for the object name
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        object_name = f"{timestamp}.jpg"

        # Upload the image to MinIO
        minio_client.put_object(
            bucket_name=MINIO_BUCKET_NAME,
            object_name=object_name,
            data=BytesIO(decoded_image),
            length=len(decoded_image),
            metadata=image_metadata
        )

        return "Image uploaded successfully!"
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)