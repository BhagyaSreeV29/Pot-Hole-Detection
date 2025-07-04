import os

# Paths to your folders
images_dir = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Data\images\train"
labels_dir = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\Pot-Hole-Detection\Data\labels\train"

# Get all image filenames without extension
image_files = [os.path.splitext(f)[0] for f in os.listdir(images_dir)
               if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Get all label filenames without extension
label_files = [os.path.splitext(f)[0] for f in os.listdir(labels_dir)
               if f.lower().endswith('.txt')]

# Compare sets
missing_labels = [img for img in image_files if img not in label_files]
extra_labels = [lbl for lbl in label_files if lbl not in image_files]

# Print results
if not missing_labels and not extra_labels:
    print("✅ All images have corresponding label files. Ready to train!")
else:
    if missing_labels:
        print("❌ Missing label files for these images:")
        for name in missing_labels:
            print(f"- {name}")
    if extra_labels:
        print("\n⚠️ Unused label files (no corresponding image):")
        for name in extra_labels:
            print(f"- {name}")
