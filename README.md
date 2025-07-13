<!-- Updated project documentation for clarity -->
# 🕳️ Pothole Detection using YOLO & CVAT

This project detects potholes in road images using object detection with YOLO. It includes image annotation with CVAT, format conversion, and model training.

---

## 💡 Overview

- Annotate images using CVAT (COCO format)
- Convert COCO annotations to YOLO format
- Prepare training data
- Run sanity checks
- Train the model using YOLO

---

## 📁 Project Structure

Pot-Hole-Detection/
├── main.py
├── Create_Task_Cvat.py
├── export_annotations.py
├── Cocotoyolo.py
├── sanity.py
├── Upload_Cvat.py
├── generate_data_yaml.py
├── data.yaml
├── .env.template
└── README.md

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Pot-Hole-Detection.git
cd Pot-Hole-Detection

2. Clone the YOLOv5 repository (for training)
git clone https://github.com/ultralytics/yolov5.git
cd yolov5

3.Create a .env file
Copy .env.template and rename it to .env
Fill in your local paths and CVAT credentials

4. Install required libraries
pip install -r requirements.txt

5. Run the pipeline
python main.py