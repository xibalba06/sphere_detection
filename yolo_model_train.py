from ultralytics import YOLO
import os
from pathlib import Path

def train_model(yaml_path, epochs=100, imgsz=512, batch=16):
    """
    Trains a YOLOv8 segmentation model.

    Parameters:
        yaml_path: Path to the dataset configuration file
        epochs: Number of training epochs
        imgsz: Image size
        batch: Batch size
    """
    try:
        # Load the YOLOv8s-seg model
        model = YOLO('yolov8s.pt')  # For segmentation, use yolov8s-seg.pt

        # Start model training
        results = model.train(
            data=yaml_path,          # Dataset configuration file
            epochs=epochs,           # Total number of epochs
            imgsz=imgsz,             # Image size
            batch=batch,             # Batch size
            name='train',            # Folder name for training results
            device='0',              # Use '0' for GPU, 'cpu' for CPU
            patience=20,             # Patience value for early stopping
            save=True,               # Save the best model
            plots=True               # Save training plots
        )

        print("Model training completed!")
        return results

    except Exception as e:
        print(f"An error occurred during model training: {str(e)}")
        return None

def main():
    # Path to the dataset configuration file
    yaml_path = r"your/project/path/dataset.yaml"

    # Check if the file exists
    if not os.path.exists(yaml_path):
        print(f"Error: {yaml_path} not found!")
        return

    print("Starting model training...")
    results = train_model(
        yaml_path=yaml_path,
        epochs=100,          # Number of training epochs
        imgsz=512,           # Image size
        batch=16             # Batch size
    )

if __name__ == "__main__":
    main()
