import os
from dotenv import load_dotenv
import yaml
import ast

def generate_data_yaml():
    load_dotenv()

    data_yaml_path = os.getenv("DATA_YAML_PATH")
    train_dir = os.getenv("IMAGE_DIR")
    val_dir = os.getenv("IMAGE_DIR")  # assuming same folder for both
    class_names = ['pothole']  # you can replace this with more classes if needed

    data = {
        "train": train_dir,
        "val": val_dir,
        "nc": len(class_names),
        "names": class_names
    }

    with open(data_yaml_path, "w") as f:
        yaml.dump(data, f)

    print(f"✅ data.yaml created at: {data_yaml_path}")

# Run when called directly
if __name__ == "__main__":
    # Generates data.yaml for YOLO training
    generate_data_yaml()
