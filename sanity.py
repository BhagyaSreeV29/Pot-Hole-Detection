import os

img_dir = r'C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Data\Train\Images'
label_dir = r'C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Data\Train\Labels'

img_files = [os.path.splitext(f)[0] for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
label_files = [os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.endswith('.txt')]

missing_labels = [f for f in img_files if f not in label_files]

print(f"Total images: {len(img_files)}")
print(f"Missing labels for: {missing_labels}")
