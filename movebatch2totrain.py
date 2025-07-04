import os
import shutil

# Paths
batch2_images = r'C:/Users/bhagy/OneDrive - sfc.edu/Desktop/Project/batch2_upload/images'
batch2_labels = r'C:/Users/bhagy/OneDrive - sfc.edu/Desktop/Project/batch2_upload/labels'
train_images = r'C:/Users/bhagy/OneDrive - sfc.edu/Desktop/Project/Pot-Hole-Detection/Data/images/train'
train_labels = r'C:/Users/bhagy/OneDrive - sfc.edu/Desktop/Project/Pot-Hole-Detection/Data/labels/train'

# Ensure destination exists
os.makedirs(train_images, exist_ok=True)
os.makedirs(train_labels, exist_ok=True)

# Move & rename files
counter = len(os.listdir(train_images))  # start numbering after existing files
for fname in os.listdir(batch2_images):
    name, ext = os.path.splitext(fname)
    label_file = f"{name}.txt"
    image_path = os.path.join(batch2_images, fname)
    label_path = os.path.join(batch2_labels, label_file)

    if os.path.exists(label_path):
        new_name = f"img_{counter}"
        shutil.copy(image_path, os.path.join(train_images, new_name + ext))
        shutil.copy(label_path, os.path.join(train_labels, new_name + ".txt"))
        counter += 1

print("✅ Batch2 files moved and renamed into training dataset.")
