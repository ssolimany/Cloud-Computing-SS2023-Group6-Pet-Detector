# cc-ss23-group5-pet-detector
An edge computing solution for the automatic detection of pets (cats, dogs, golden hamsters) for the cloud computing module in SS2023.


## Frontend

TODO


## Backend


### Requirements

- [Python 3.11.3](https://www.python.org/downloads/)
- [MinIO RELEASE.2023-05-18T00-05-36Z](https://min.io/download)


### Installation

- Start the MinIO server, use `minioadmin` as username **and** password
  - **macOS** (using Terminal): \
    `# MINIO_ROOT_USER=minioadmin MINIO_ROOT_PASSWORD=minioadmin minio server ~/data --console-address ":9001"`
  - **Windows** (using PowerShell): \
    `PS> setx MINIO_ROOT_USER minioadmin` \
    `PS> setx MINIO_ROOT_PASSWORD minioadmin` \
    `PS> C:\minio.exe server F:\Data --console-address ":9001"`
- Setup and start the Flask backend
  - Navigate into `cluster-nodes/web-app/back-end`
  - Create and activate a Python virtual environment:
    - **Windows** (using PowerShell): \
      `PS> python -m venv .venv` \
      `PS> .venv\Scripts\activate`
    - **macOS** (using Terminal): \
      `# python3 -m venv .venv` \
      `# source .venv/bin/activate`
  - Install the required pip packages
    - **Windows**: \
      `PS> pip install -r requirements.txt`
    - **macOS**: \
      `# pip3 install -r requirements.txt`
  - Start the Flask backend
    - **Windows**: \
      `PS> python app.py`
    - **macOS**: \
      `# python3 app.py`
  - (Optionally) Send some test detections to the backend using the test script `send-test-detections-to-backend.py`
    - Navigate into `cluster-nodes/web-app/back-end/test`
    - Run `send-test-detections-to-backend.py`
      - **Windows**: \
        `PS> python send-test-detections-to-backend.py`
      - **macOS**: \
        `# python3 send-test-detections-to-backend.py`
  - (Optionally) Receive the latest detections from the backend using the test script `get-latest-detections-from-backend.py`
    - Navigate into `cluster-nodes/web-app/back-end/test`
    - Run `get-latest-detections-from-backend.py`
      - **Windows**: \
        `PS> python get-latest-detections-from-backend.py`
      - **macOS**: \
        `# python3 get-latest-detections-from-backend.py`