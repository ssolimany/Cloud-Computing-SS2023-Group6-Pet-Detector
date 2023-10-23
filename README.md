# Cloud Computing SS23 - Group6 - Pet detector

An edge computing solution for the automatic detection of pets (cats, dogs, golden hamsters) for the [cloud computing module in SS2023](https://www.christianbaun.de/CGC23/index.html).

The project involves several key steps:

1. Setting up sensor nodes using Raspberry Pi 4 and camera modules.
1. Deploying an operating system and object detection software, such as Raspberry Pi OS, Ubuntu, YOLO, or TensorFlow.
1. Collecting a sufficient number of images for training and testing the object detection model, using either personal hardware with GPUs or a cloud service like Roboflow or V7.
1. Creating a backend system to manage sensor nodes and collected data, deployed as Docker containers on a Raspberry Pi Kubernetes Cluster with k3s. The backend infrastructure is designed to be robust and scalable, featuring a distributed file system like Ceph or a storage service like MinIO.
1. Developing a frontend to display log information, event messages, and a map of events with accompanying images and timestamps. The frontend is deployed as a Docker container on the same Raspberry Pi Kubernetes Cluster and is built using a modern framework like Vue.js or React.
1. Utilizing protocols like REST or MQTT for communication between various components, including the frontend, backend, and services.
1. Implementing a Telegram notification feature using a Telegram Bot.

Overall, the project aims to create a comprehensive system for sensor-based object detection and data management, with a strong focus on scalability and modern software development practices.


## Frontend


### Requirements

- [Node.js](https://nodejs.org/en) >= 18.17.0


### Installation

npm install --global yarn
yarn
yarn add eslint --dev
npx eslint --init
npm install --save-dev sass
npm i -D react-router-dom 
yarn add infinite-react-carousel

npm run dev // Start the frontend with following command


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
