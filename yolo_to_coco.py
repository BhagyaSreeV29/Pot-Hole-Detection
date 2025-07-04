import os
import json
from PIL import Image
from cvat_sdk import make_client
from cvat_sdk.core.proxies.tasks import ResourceType

# === CONFIGURATION ===
HOST = "http://localhost:8080"
USERNAME = "bhagyasrivemavarapu09"  # Replace with your CVAT username
PASSWORD = "Bhagya@12345"  # Replace with your CVAT password

TASK_NAME = "Pothole Batch2 Upload"
LABEL_NAME = "pothole"

IMAGE_FOLDER = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Data\Train\Images\batch_2"
OUTPUT_JSON = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\batch2_upload\batch2_coco.json"

# === STEP 1: CONVERT YOLO TO COCO JSON ===
def convert_yolo_to_coco(image_dir, output_json):
    categories = [{"id": 1, "name": LABEL_NAME}]
    images, annotations = [], []
    ann_id = 1

    for img_id, filename in enumerate(sorted(os.listdir(image_dir)), 1):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(image_dir, filename)
            label_path = os.path.splitext(image_path)[0] + ".txt"

            if not os.path.exists(label_path):
                print(f"[⚠️] Skipping: No label for {filename}")
                continue

            with Image.open(image_path) as img:
                width, height = img.size

            images.append({
                "id": img_id,
                "file_name": filename,
                "width": width,
                "height": height,
            })

            with open(label_path, "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) != 5:
                        continue
                    class_id, x_center, y_center, w, h = map(float, parts)
                    x_min = (x_center - w / 2) * width
                    y_min = (y_center - h / 2) * height
                    bbox_width = w * width
                    bbox_height = h * height

                    annotations.append({
                        "id": ann_id,
                        "image_id": img_id,
                        "category_id": 1,
                        "bbox": [x_min, y_min, bbox_width, bbox_height],
                        "area": bbox_width * bbox_height,
                        "iscrowd": 0
                    })
                    ann_id += 1

    coco_dict = {
