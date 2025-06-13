from ultralytics import YOLO

# Load the model
model = YOLO("yolov8s.pt")  

# Train the model
model.train(data="D:/Cheating-Surveillance-System/data.yaml", epochs=30, imgsz=640)

