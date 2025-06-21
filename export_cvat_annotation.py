import os
from cvat_sdk import make_client

# === Configuration ===
HOST = "http://localhost:8080"
USERNAME = "bhagyasrivemavarapu09"
PASSWORD = "Bhagya@12345"
TASK_ID = 1  # Replace this with your actual task ID
EXPORT_FORMAT = "COCO 1.0"

# === Output Path Configuration ===
output_dir = r"C:/Users/bhagy/OneDrive - sfc.edu/Desktop/Project/data/trine/labels"
output_filename = "batch_1.json"
output_path = os.path.join(output_dir, output_filename)

# === Make sure the output directory exists ===
os.makedirs(output_dir, exist_ok=True)

# === Download annotations and save ===
def export_annotations():
    with make_client(host=HOST) as client:
        client.login((USERNAME, PASSWORD))

        print(f"📦 Downloading annotations for task ID: {TASK_ID} ...")
        result = client.tasks.api.export_download(task_id=TASK_ID, format=EXPORT_FORMAT)

        with open(output_path, "wb") as f:
            f.write(result)

        print(f"✅ Annotations successfully saved to:\n{output_path}")

# === Run the function ===
if __name__ == "__main__":
    export_annotations()
