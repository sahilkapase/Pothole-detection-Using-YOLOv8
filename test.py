from ultralytics import YOLO
import cv2

# Load the YOLOv8 model
model = YOLO("y8best.pt")  # Make sure the model file 'y8best.pt' is in the correct directory

# Perform prediction on the video file 'demo.mp4'
results = model.predict(source="demo.mp4", show=True)  # This will display the results

# Print the results
print(results)
