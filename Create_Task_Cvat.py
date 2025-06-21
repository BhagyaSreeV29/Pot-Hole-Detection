import os
import json
from cvat_sdk import make_client
from cvat_sdk.core.proxies.tasks import ResourceType

# Configuration
HOST = "http://localhost:8080"
USERNAME = "bhagyasrivemavarapu09"
PASSWORD = "Bhagya@12345"
TASK_NAME = "CVAT Task - Pothole"
LABEL_NAME = "pothole"
IMAGE_DIR = r"C:/Users/bhagy/OneDrive - sfc.edu/Desktop/Project/Data/Train/Images/batch_1"

# Gather image file paths
image_paths = sorted([
    os.path.join(IMAGE_DIR, f)
    for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
])
with open('C:/Users/bhagy/OneDrive - sfc.edu/Desktop/Project/Annatation.json', 'r') as f:
    annotations = json.load(f)
# Connect to CVAT and create + upload in one step
with make_client(host=HOST) as client:
    client.login((USERNAME, PASSWORD))

    task = client.tasks.create_from_data(
    
        spec=annotations,
        annotation_format='COCO 1.0',
        resource_type=ResourceType.LOCAL,
        resources=image_paths,
        data_params={'image_quality':100}    )

    print(f"✅ Task '{TASK_NAME}' created with ID: {task.id}")
    print("✅ Images uploaded successfully.")
