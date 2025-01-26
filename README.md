# sphere_detection
 # YOLOv8n Object Detection Project

This project utilizes the **YOLOv8n** (You Only Look Once v8 Nano) model for object detection tasks. The dataset used for training and testing the model was generated using **Isaac Sim**, NVIDIA's physics-based simulation platform. Below, you will find detailed information about the project, including setup instructions, training process, evaluation, and usage examples.

---

## Project Description

The goal of this project is to perform object detection using the YOLOv8n model. YOLOv8n is the smallest and fastest model in the YOLOv8 family, making it ideal for real-time applications and devices with limited computational resources. The dataset was synthetically generated using Isaac Sim to improve the model's performance.

### Objectives

- Detect specific objects in images captured from a camera.
- Develop a model optimized for real-time object detection applications.
- Leverage synthetic data generated with Isaac Sim to enhance model accuracy.

---

## Technologies and Tools

- **YOLOv8n:** The object detection model used in this project.
- **Isaac Sim:** Used to generate synthetic data for training and testing.
- **Python:** Programming language used for development.
- **Ultralytics YOLOv8 Library:** For training and deploying YOLOv8 models.
- **OpenCV:** For image processing and visualization.
- **PyTorch:** For training and evaluating deep learning models.

---

## Setup Instructions

### 1. Install Dependencies

To set up the project, install the required Python libraries:

1. Ensure Python 3.8 or higher is installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install the required libraries:
  pip install -r req.txt

*Data Generation with Isaac Sim
The dataset for this project was generated using Isaac Sim. Isaac Sim is a powerful tool for physics-based simulations and synthetic data generation. The following steps were used to generate the dataset:

-A simulation environment was created.
-Objects were placed in the scene with random positions, lighting, and backgrounds to ensure diversity.(scripts file in isaac_sim folder)
RGB images and bounding box annotations were exported.
The data was then converted into YOLO format for training.(with yolo_converter.py file)

Training Process
1. Data Preparation
The dataset generated with Isaac Sim was converted into YOLO format:

Data Format: For each image, a .txt file was created. Each line in the file represents an object with the following format:
class_id x_center y_center width height
The dataset was split into training (80%), validation (10%), and testing (10%) sets.

2. Training the Model
main.py

3. Training Parameters:
Epochs: 100
Image Size: 512x512
Model: YOLOv8n (Nano)
I worked with a very weak model because my system has an rtx3050 laptop gpu. However, if you have a more powerful system, you can try more advanced models. It can only be done by changing the model name in the main.py.(yolov11,yolov10,yolov8x,yolov8l ...)

Results
The model performs well in detecting small objects.
Synthetic data generated with Isaac Sim significantly improved the model's performance.
The model is fast enough for real-time applications.

Dependencies
Python 3.8+
Ultralytics YOLOv8
OpenCV
Matplotlib
Isaac Sim (for data generation)
This project demonstrates how to train and use the YOLOv8n model with synthetic data generated using Isaac Sim. For more information or support, feel free to reach out! 😊
















  
   
