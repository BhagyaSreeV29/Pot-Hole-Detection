import os
from cvat_sdk import make_client
from dotenv import load_dotenv

# === Load environment variables ===
load_dotenv()

# === Configuration ===
HOST = os.getenv("CVAT_HOST")
USERNAME = os.getenv("CVAT_USERNAME")
PASSWORD = os.getenv("CVAT_PASSWORD")
TASK_ID = int(os.getenv("CVAT_TASK_ID"))
EXPORT_FORMAT = os.getenv("CVAT_EXPORT_FORMAT")
EXPORT_DIR = os.getenv("EXPORT_DIR")
EXPORT_FILENAME = os.getenv("EXPORT_FILENAME")

# === Output Path Configuration ===
output_path = os.path.join(EXPORT_DIR, EXPORT_FILENAME)
os.makedirs(EXPORT_DIR, exist_ok=True)

def export_annotations():
    """Download annotations for a CVAT task and save to disk."""
    with make_client(host=HOST) as client:
        client.login((USERNAME, PASSWORD))

        print(f"\ud83d\udce6 Downloading annotations for task ID: {TASK_ID} ...")
        result = client.tasks.api.export_download(task_id=TASK_ID, format=EXPORT_FORMAT)

        with open(output_path, "wb") as f:
            f.write(result)

        print(f"\u2705 Annotations successfully saved to: {output_path}")

if __name__ == "__main__":
    export_annotations()
