import os

# Define paths
image_dir = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\batch2_upload\images"
label_dir = r"C:\Users\bhagy\OneDrive - sfc.edu\Desktop\Project\batch2_upload\labels"

# Get all image filenames (with extension)
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(".jpg")]

if not image_files:
    print("⚠️ No images found. Please check the path:", image_dir)
else:
    print(f"✅ Found {len(image_files)} images in the folder.")

# Check if label folder exists
if not os.path.exists(label_dir):
    print("❌ Label directory not found:", label_dir)
    exit()

found = 0
missing = 0

# Loop through image filenames and check for matching label
for img_file in image_files:
    label_file = img_file.replace(".jpg", ".txt")
    label_path = os.path.join(label_dir, label_file)

    if os.path.exists(label_path):
        print(f"✓ Label found for: {img_file}")
        found += 1
    else:
        print(f"✗ Missing label for: {img_file}")
        missing += 1

print("\nSummary:")
print(f"Total images: {len(image_files)}")
print(f"Labels found: {found}")
print(f"Labels missing: {missing}")
