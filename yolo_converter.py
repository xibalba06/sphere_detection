import json
import numpy as np
from pathlib import Path
import os

def convert_isaac_to_yolo(input_folder, output_folder):
    """
    input_folder: Folder containing Isaac Sim outputs
    output_folder: Folder where YOLO format .txt files will be saved
    """
    # Create the output folder
    os.makedirs(output_folder, exist_ok=True)

    # Find all label files
    label_files = list(Path(input_folder).glob("*labels*.json"))
    print(f"Total number of files to process: {len(label_files)}")

    for label_file in label_files:
        try:
            # Get the file number (e.g., 0000)
            file_num = label_file.stem.split('_')[-1]

            # Create the path for the corresponding .npy file
            npy_file = Path(input_folder) / f"bounding_box_2d_tight_{file_num}.npy"

            if not npy_file.exists():
                print(f"Warning: {npy_file} not found, skipping this file.")
                continue

            # Read the NPY file
            bbox_data = np.load(npy_file)

            # Convert (1,) shaped data to a tuple
            bbox = bbox_data.item()

            if len(bbox) != 6:
                print(f"Unexpected data length ({file_num}): {len(bbox)}")
                continue

            # Create the output file
            output_file = Path(output_folder) / f"{file_num}.txt"

            # Image dimensions (default is 512x512)
            image_width = 512
            image_height = 512

            with open(output_file, 'w') as f:
                # bbox format: (class_id, x_min, y_min, x_max, y_max, confidence)
                class_id = int(bbox[0])
                x_min, y_min = float(bbox[1]), float(bbox[2])
                x_max, y_max = float(bbox[3]), float(bbox[4])

                # Convert to YOLO format
                x_center = (x_min + x_max) / (2 * image_width)
                y_center = (y_min + y_max) / (2 * image_height)
                width = (x_max - x_min) / image_width
                height = (y_max - y_min) / image_height

                # Clamp values to the range [0, 1]
                x_center = min(max(x_center, 0), 1)
                y_center = min(max(y_center, 0), 1)
                width = min(max(width, 0), 1)
                height = min(max(height, 0), 1)

                # Write in YOLO format
                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

            if int(file_num) % 100 == 0:
                print(f"Processed file: {file_num}")

        except Exception as e:
            print(f"Error occurred ({file_num}): {str(e)}")
            print(f"bbox_data content: {bbox_data}")

    print("Conversion completed!")

# Usage
input_folder = "your/project/path/data"  # Folder containing Isaac Sim outputs
output_folder = "your/project/path/txt_files"  # Folder where YOLO labels will be saved

convert_isaac_to_yolo(input_folder, output_folder)
