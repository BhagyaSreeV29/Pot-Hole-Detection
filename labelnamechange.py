import os

# Set your paths
image_dir = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Data\Train\Images"
label_dir = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Data\Train\Labels"

# Rename image files
for filename in os.listdir(image_dir):
    if ".jpg.rf." in filename:
        base = filename.split(".jpg")[0]  # Extract 'img-100'
        new_name = base + ".jpg"
        os.rename(os.path.join(image_dir, filename), os.path.join(image_dir, new_name))

# Rename label files
for filename in os.listdir(label_dir):
    if ".jpg.rf." in filename:
        base = filename.split(".jpg")[0]
        new_name = base + ".txt"
        os.rename(os.path.join(label_dir, filename), os.path.join(label_dir, new_name))

print("✅ All files renamed successfully.")
