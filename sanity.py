import os
import argparse

def check_image_label_consistency(images_dir, labels_dir):
    image_files = [os.path.splitext(f)[0] for f in os.listdir(images_dir)
                   if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    label_files = [os.path.splitext(f)[0] for f in os.listdir(labels_dir)
                   if f.lower().endswith('.txt')]

    missing_labels = [img for img in image_files if img not in label_files]
    extra_labels = [lbl for lbl in label_files if lbl not in image_files]

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

if __name__ == "__main__":
    # Validates dataset and annotation quality
    parser = argparse.ArgumentParser(description="Sanity check: image-label consistency for YOLO training.")
    parser.add_argument("--images", default="Data/images/train", help="Path to image folder")
    parser.add_argument("--labels", default="Data/labels/train", help="Path to label folder")
    args = parser.parse_args()

    check_image_label_consistency(args.images, args.labels)
