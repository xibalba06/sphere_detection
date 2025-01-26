import cv2
from ultralytics import YOLO

def live_camera_inference(model_path, camera_index=0, conf_threshold=0.6):
    """
    Object detection on live camera feed using YOLO model.

    Parameters:
        model_path: Path to the trained YOLO model (e.g., 'best.pt')
        camera_index: Index of the camera to use (default: 0)
        conf_threshold: Minimum confidence threshold for detection (default: 0.5)
    """
    # Load YOLO model
    model = YOLO(model_path)

    # Start the camera
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Failed to open the camera!")
        return

    print("Camera feed started. Press 'q' to exit.")

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame, closing camera...")
            break

        # Run YOLO model on the frame
        results = model(frame)

        # Draw detection results
        annotated_frame = results[0].plot()  # Draw detection results

        # Display the frame
        cv2.imshow("YOLOv8 Live Detection", annotated_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to the trained model
    model_path = r"your/project/path/runs/detect/train/weights/best.pt"  # Replace with the path to your trained model file

    # Start live camera feed
    live_camera_inference(model_path)
