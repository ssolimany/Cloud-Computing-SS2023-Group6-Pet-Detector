import requests
import base64
import os
import time


# Flask backend URL
BACKEND_URL = 'http://192.168.178.66:5001'

# Path to example-images folder
FOLDER_PATH = "./example-images"

image1_metadata = {
    "detection_amount": 2,
    "detection_classes": ("dog", "cat"),
    "detection_confidence_values": (0.98, 0.88)    
}

image2_metadata = {
    "detection_amount": 1,
    "detection_classes": "cat",
    "detection_confidence_values": 1    
}

image3_metadata = {
    "detection_amount": 1,
    "detection_classes": "dog",
    "detection_confidence_values": 0.97   
}

image_metadata_list = [image1_metadata, image2_metadata, image3_metadata]

def encode_image_to_base64(image_path: str) -> str:
    """
    Read the image file as binary data and encode as base 64
    """
    with open(image_path, 'rb') as file:
        image_data = file.read()
        base64_encoded_image = base64.b64encode(image_data).decode('utf-8')
    return base64_encoded_image

def main():
    # Get list of JPEG files in the folder
    jpeg_file_list = [jpeg_file for jpeg_file in os.listdir(FOLDER_PATH) if jpeg_file.lower().endswith('.jpg') or jpeg_file.lower().endswith('.jpeg')]
    
    index = 0

    for jpeg_file in jpeg_file_list:
        jpeg_filepath = os.path.join(FOLDER_PATH, jpeg_file)
        base64_data = encode_image_to_base64(jpeg_filepath)
        
        image_metadata = image_metadata_list[index]

        # Prepare data for JSON payload
        data = {
            "image_data": base64_data,
            "detection_amount": image_metadata["detection_amount"],
            "detection_classes": image_metadata["detection_classes"],
            "detection_confidence_values": image_metadata["detection_confidence_values"],
        }

        # Send a POST request to the Endpoint /upload/jpeg"
        response = requests.post(url=f"{BACKEND_URL}/upload/jpeg", json=data)

        # Check the response status
        if response.status_code == 200:
            print(f'File {jpeg_file} successfully sent to the backend.')
            print(response.text)
            index += 1
        else:
            print(f'Failed to send file {jpeg_file}. Status code:', response.status_code)
            print(response.text)
        
        # Wait for 1 second
        time.sleep(1)

if __name__ == '__main__':
    main()