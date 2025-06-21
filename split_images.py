import os
import shutil
import math

# Source and destination paths
source_dir = r"C:\Users\bhagy\Downloads\Pothole.v1-raw.yolov5pytorch\train\images"
destination_dir = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Data\Train"

# Get all image files
images = sorted([f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
total_images = len(images)
batch_size = 20
num_batches = math.ceil(total_images / batch_size)
    
# Create destination directory and subfolders, then copy images
for i in range(num_batches):
    batch_folder = os.path.join(destination_dir, f"batch_{i+1}")
    os.makedirs(batch_folder, exist_ok=True)
    
    batch_images = images[i * batch_size : (i + 1) * batch_size]
    for img in batch_images:
        src_path = os.path.join(source_dir, img)
        dst_path = os.path.join(batch_folder, img)
        shutil.copy(src_path, dst_path)

print(f"Split {total_images} images into {num_batches} subfolders successfully.")