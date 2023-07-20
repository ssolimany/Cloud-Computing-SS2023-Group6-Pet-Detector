# cc-ss23-group6-pet-detector
An edge computing solution for the automatic detection of pets (cats, dogs, golden hamsters) for the cloud computing module in SS2023.


## Frontend


### Installation

npm install --global yarn
yarn
yarn add eslint --dev
npx eslint --init
npm install --save-dev sass
npm i -D react-router-dom 
yarn add infinite-react-carousel


### Start the frontend with following command

npm run dev


## Backend


### Requirements

- [Python 3.11.3](https://www.python.org/downloads/)
- [MinIO RELEASE.2023-05-18T00-05-36Z](https://min.io/download)


### Installation

- [Start the MinIO server](https://min.io/docs/minio/linux/index.html), use `minioadmin` as username **and** password
  - **macOS** (using Terminal): \
    `# MINIO_ROOT_USER=minioadmin MINIO_ROOT_PASSWORD=minioadmin minio server ~/data --console-address ":9001"`
  - **Windows** (using PowerShell): \
    `PS> setx MINIO_ROOT_USER minioadmin` \
    `PS> setx MINIO_ROOT_PASSWORD minioadmin` \
    `PS> C:\minio.exe server F:\Data --console-address ":9001"`
- Setup and start the Flask backend
  - Navigate into [`cluster-nodes/web-app/back-end`](https://github.com/ssolimany/cc-ss23-group5-pet-detector/tree/main/cluster-nodes/web-app/back-end)
  - In [app.py](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/main/cluster-nodes/web-app/back-end/app.py)
    - Change the MinIO server configuration in line [16](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/afe19fca21ccee716fc766b46ed79abe77ce1c2a/cluster-nodes/web-app/back-end/app.py#L16)-[19](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/afe19fca21ccee716fc766b46ed79abe77ce1c2a/cluster-nodes/web-app/back-end/app.py#L19) accordingly
    - Change the Telegram Bot API Token, URL and Chat ID in line [11](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/afe19fca21ccee716fc766b46ed79abe77ce1c2a/cluster-nodes/web-app/back-end/app.py#L11)-[13](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/afe19fca21ccee716fc766b46ed79abe77ce1c2a/cluster-nodes/web-app/back-end/app.py#L13) accordingly
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
  - (Optionally) Send some test detections to the backend using the test script [`send-test-detections-to-backend.py`](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/main/cluster-nodes/web-app/back-end/test/send-test-detections-to-backend.py)
    - Navigate into [`cluster-nodes/web-app/back-end/test`](https://github.com/ssolimany/cc-ss23-group5-pet-detector/tree/main/cluster-nodes/web-app/back-end/test)
    - Change the Backend URL in line [8](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/afe19fca21ccee716fc766b46ed79abe77ce1c2a/cluster-nodes/web-app/back-end/test/send-test-detections-to-backend.py#L8) accordingly
    - Run `send-test-detections-to-backend.py`
      - **Windows**: \
        `PS> python send-test-detections-to-backend.py`
      - **macOS**: \
        `# python3 send-test-detections-to-backend.py`
  - (Optionally) Receive the latest detections from the backend using the test script [`get-latest-detections-from-backend.py`](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/main/cluster-nodes/web-app/back-end/test/get-latest-detections-from-backend.py)
    - Navigate into [`cluster-nodes/web-app/back-end/test`](https://github.com/ssolimany/cc-ss23-group5-pet-detector/tree/main/cluster-nodes/web-app/back-end/test)
    - Change the Backend URL in line [7](https://github.com/ssolimany/cc-ss23-group5-pet-detector/blob/afe19fca21ccee716fc766b46ed79abe77ce1c2a/cluster-nodes/web-app/back-end/test/get-latest-detections-from-backend.py#L7) accordingly
    - Run `get-latest-detections-from-backend.py`
      - **Windows**: \
        `PS> python get-latest-detections-from-backend.py`
      - **macOS**: \
        `# python3 get-latest-detections-from-backend.py`
