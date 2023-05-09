from flask import Flask, request
from io import BytesIO
from minio import Minio
import json
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

@app.route("/upload/jpeg", methods=["POST"])
def upload_as_jpeg_file():
    """
    This Endpoint decodes the base64 encoded image and uploads it as
    jpeg with the detections and confidences as metadata to MinIO
    """
    base64_encoded_image = request.json.get("image")
    decoded_image = base64.b64decode(base64_encoded_image)
    
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

@app.route("/upload/json", methods=["POST"])
def upload_as_json_file():
    """
    This Endpoint saves the base64 encoded image with the detections
    and confidences in a JSON file and uploads it to MinIO
    """
    try:
        # Get the JSON object from the request
        json_object = request.get_json()

        # Convert the JSON object to a string
        json_string = json.dumps(json_object)

        # Generate a unique filename using a timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{timestamp}.json"

        # Write the JSON string to a file
        with open(file_name, "w") as json_file:
            json_file.write(json_string)

        # Upload the JSON file to MinIO
        minio_client.fput_object(MINIO_BUCKET_NAME, file_name, file_name)

        return "JSON file uploaded successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)