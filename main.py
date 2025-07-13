from Create_Task_Cvat import create_cvat_task
from export_annotations import export_annotations
from Cocotoyolo import convert_coco_to_yolo
from sanity import check_annotation_integrity
from Upload_Cvat import upload_inference_results
from generate_data_yaml import generate_data_yaml

def main():
    print("\n🚀 Starting Pothole Detection Workflow\n")

    # Step 1: Create and upload task to CVAT
    create_cvat_task()

    # Step 2: Export annotations from CVAT in COCO format
    export_annotations()

    # Step 3: Convert annotations from COCO to YOLO format
    convert_coco_to_yolo()

    # Step 4: Sanity check labels and images
    check_annotation_integrity()

    # Step 5: Generate YOLO data.yaml file
    generate_data_yaml()

    # Step 6: Upload inference results back to CVAT (optional)
    upload_inference_results()

    print("\n✅ Workflow completed successfully\n")

if __name__ == "__main__":
    main()
