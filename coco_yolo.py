import os
import json
from pathlib import Path

# Paths
coco_json_path = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Downloads\task1_coco_extracted\annotations\instances_default.json"
images_folder = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Downloads\task1_coco_extracted\images"
labels_output_folder = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\data\train\labels"

os.makedirs(labels_output_folder, exist_ok=True)

# Load COCO JSON
with open(coco_json_path, 'r') as f:
    coco = json.load(f)

# Map image IDs to file names and sizes
image_id_map = {
    img['id']: {
        'file_name': img['file_name'],
        'width': img['width'],
        'height': img['height']
    } for img in coco['images']
}

# Create YOLO-format .txt files
for ann in coco['annotations']:
    image_info = image_id_map[ann['image_id']]
    img_w, img_h = image_info['width'], image_info['height']
    x, y, w, h = ann['bbox']
    
    # Convert to YOLO format
    x_center = (x + w / 2) / img_w
    y_center = (y + h / 2) / img_h
    norm_w = w / img_w
    norm_h = h / img_h
    
    # YOLO class id (COCO uses 1-based indexing; YOLO uses 0-based)
    class_id = ann['category_id'] - 1

    # Output file path
    image_filename = Path(image_info['file_name']).stem
    txt_path = os.path.join(labels_output_folder, f"{image_filename}.txt")

    with open(txt_path, 'a') as out_file:
        out_file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {norm_w:.6f} {norm_h:.6f}\n")

print("✅ COCO annotations converted to YOLO format and saved to:", labels_output_folder)
