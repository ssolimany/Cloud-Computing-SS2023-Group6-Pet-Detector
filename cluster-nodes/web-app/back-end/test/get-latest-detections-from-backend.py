import requests
import base64
import json


# Flask backend URL
BACKEND_URL = 'http://127.0.0.1:5001'

response = requests.get(url=f"{BACKEND_URL}/")

# Check the response status
if response.status_code == 200:
    print("Data successfully received.")
    print(response)
else:
    print("Failed to receive data. Status code:", response.status_code)

# Print the response from the server
print(response.text)