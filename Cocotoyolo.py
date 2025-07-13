import os
import json
from PIL import Image
from dotenv import load_dotenv
from cvat_sdk import make_client
from cvat_sdk.core.proxies.tasks import ResourceType

# === Load .env values ===
load_dotenv()

HOST = os.getenv("CVAT_HOST")
USERNAME = os.getenv("CVAT_USERNAME")
PASSWORD = os.getenv("CVAT_PASSWORD")

TASK_NAME = os.getenv("UPLOAD_TASK_NAME")
LABEL_NAME = os.getenv("UPLOAD_LABEL_NAME")

IMAGE_FOLDER = os.getenv("UPLOAD_IMAGE_DIR")
OUTPUT_JSON = os.getenv("UPLOAD_OUTPUT_JSON")

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
        "info": {"description": "Pothole Dataset"},
        "licenses": [],
        "images": images,
        "annotations": annotations,
        "categories": categories
    }

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w") as f:
        json.dump(coco_dict, f, indent=4)
    print(f"✅ COCO JSON saved at: {output_json}")

def upload_to_cvat(image_dir, json_path):
    image_paths = sorted([
        os.path.join(image_dir, f)
        for f in os.listdir(image_dir)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])

    with open(json_path, "r") as f:
        annotations = json.load(f)

    with make_client(host=HOST) as client:
        client.login((USERNAME, PASSWORD))
        task = client.tasks.create_from_data(
            spec=annotations,
            annotation_format='COCO 1.0',
            resource_type=ResourceType.LOCAL,
            resources=image_paths,
            data_params={'image_quality': 100}
        )
        print(f"📤 Task '{TASK_NAME}' uploaded successfully (ID: {task.id})")

if __name__ == "__main__":
    convert_yolo_to_coco(IMAGE_FOLDER, OUTPUT_JSON)
    upload_to_cvat(IMAGE_FOLDER, OUTPUT_JSON)
