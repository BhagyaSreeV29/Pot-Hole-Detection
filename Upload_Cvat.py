import os
import json
from dotenv import load_dotenv
from cvat_sdk import make_client
from cvat_sdk.core.proxies.tasks import ResourceType

# Load environment variables from .env
load_dotenv()

# Get values from .env
HOST = os.getenv("CVAT_HOST")
USERNAME = os.getenv("CVAT_USERNAME")
PASSWORD = os.getenv("CVAT_PASSWORD")
TASK_NAME = os.getenv("CVAT_TASK_NAME")
LABEL_NAME = os.getenv("CVAT_LABEL_NAME")
IMAGE_DIR = os.getenv("IMAGE_DIR")
ANNOTATION_FILE = os.getenv("ANNOTATION_FILE")

def gather_image_paths(image_dir):
    """
    Returns sorted list of image paths in the given directory.
    """
    return sorted([
        os.path.join(image_dir, f)
        for f in os.listdir(image_dir)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])

def load_annotation_schema(annotation_file):
    """
    Loads annotation schema from a JSON file (COCO format).
    """
    with open(annotation_file, 'r') as f:
        return json.load(f)

def create_task_on_cvat(host, username, password, task_name, label_name, image_paths, annotation_schema):
    """
    Connects to CVAT and creates a task with uploaded images and COCO schema.
    """
    with make_client(host=host) as client:
        client.login((username, password))

        task = client.tasks.create_from_data(
            spec=annotation_schema,
            annotation_format='COCO 1.0',
            resource_type=ResourceType.LOCAL,
            resources=image_paths,
            data_params={'image_quality': 100}
        )

        print(f"✅ Task '{task_name}' created with ID: {task.id}")
        print("✅ Images uploaded successfully.")

def main():
    """
    Main entry point for creating and uploading a CVAT task.
    """
    print("📦 Starting CVAT task creation...")
    image_paths = gather_image_paths(IMAGE_DIR)
    annotation_schema = load_annotation_schema(ANNOTATION_FILE)
    create_task_on_cvat(HOST, USERNAME, PASSWORD, TASK_NAME, LABEL_NAME, image_paths, annotation_schema)

if __name__ == "__main__":
    main()
