import zipfile
import os

zip_path = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Downloads\task1_coco_annot.zip"
extract_to = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Downloads\task1_coco_extracted"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("✅ ZIP extracted to:", extract_to)
