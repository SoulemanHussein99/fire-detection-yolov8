# Fire Detection System using YOLOv8

A deep learning-based fire detection system built using Ultralytics YOLOv8.  
The model is trained on a custom dataset to detect fire in images.

---

## Features

- Custom-trained YOLOv8 model
- Real-time fire detection
- Bounding box visualization
- Inference on images
- High accuracy object detection

---

## Model Details

- Model: YOLOv8 (Ultralytics)
- Training: Custom dataset
- Classes: Fire (1 class)
- Framework: PyTorch backend

---

## Dataset

- Train images: `/Dataset/train/images`
- Validation images: `/Dataset/val/images`
- Labels: Fire only
- Format: YOLO format annotations

---

## Training

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640 batch=2
