import requests
import base64
import random

# Flask backend URL
BACKEND_URL = 'http://192.168.178.20:5001'

# Path to example images
IMAGE_PATH = "./example-images/cute-doge.jpg"

def read_and_encode_image_to_base64(image_path):
    # Read the image file as binary data
    with open(IMAGE_PATH, 'rb') as file:
        image_data = file.read()

    # Encode the image data as base64
    base64_encoded_image = base64.b64encode(image_data).decode('utf-8')

    return base64_encoded_image

def generate_random_confidences():
    # Generate a random number between 1 and 3
    number_of_floats = random.randint(1, 3)

    # Create a list where the to-be-generated floats should be stored
    floats = []

    # Generate random floats between 0.5 and 1.0, rounded to 2 decimal places
    for iteration in range(number_of_floats):
        random_value = random.uniform(0.5, 1.0)
        rounded_value = round(random_value, 2)
        floats.append(rounded_value)
    
    return floats

base64_encoded_image = read_and_encode_image_to_base64(IMAGE_PATH)
confidence_values = generate_random_confidences()

# The amount of detections equals the amount of confidence values
amount_of_detections = len(confidence_values)

# Create a dictionary with the image and metadata
data = {
    'image': base64_encoded_image,
    'detections': amount_of_detections,
    'confidences': confidence_values
}

for api_endpoint in ["/upload/jpeg", "/upload/json"]:
    # Send a POST request to the Endpoint /upload/jpeg"
    response = requests.post(url=f"{BACKEND_URL}{api_endpoint}", json=data)

    # Check the response status
    if response.status_code == 200:
        print("Data sent successfully.")
    else:
        print("Failed to send data. Status code:", response.status_code)

    # Print the response from the server
    print(response.text)