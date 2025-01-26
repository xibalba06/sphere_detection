import os
import shutil
import random
import yaml

def create_yolov8_structure_and_move_files(png_folder, txt_folder, base_path, class_names, val_split=0.2):
    """
    Creates the necessary folder structure for YOLOv8 and moves files.

    Args:
        png_folder (str): Folder containing PNG files.
        txt_folder (str): Folder containing TXT files (labels).
        base_path (str): Base path for the YOLOv8 dataset.
        class_names (list): List of class names.
        val_split (float): Proportion of files to be used for validation (0.2 = 20%).
    """
    # Define necessary folder paths
    train_images_path = os.path.join(base_path, "train", "images")
    train_labels_path = os.path.join(base_path, "train", "labels")
    val_images_path = os.path.join(base_path, "val", "images")
    val_labels_path = os.path.join(base_path, "val", "labels")

    # Create necessary folders
    for path in [train_images_path, train_labels_path, val_images_path, val_labels_path]:
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    # Match PNG and TXT files
    png_files = sorted([f for f in os.listdir(png_folder) if f.endswith(".png")])
    txt_files = sorted([f for f in os.listdir(txt_folder) if f.endswith(".txt")])

    if len(png_files) != len(txt_files):
        print("Warning: The number of PNG and TXT files does not match!")
        print(f"PNG files: {len(png_files)}, TXT files: {len(txt_files)}")

    # Pair and shuffle files
    paired_files = list(zip(png_files, txt_files))
    random.shuffle(paired_files)

    # Number of files for validation set
    val_count = int(len(paired_files) * val_split)

    # Split into validation and training files
    val_files = paired_files[:val_count]
    train_files = paired_files[val_count:]

    # Move training files
    for png_file, txt_file in train_files:
        shutil.copy(os.path.join(png_folder, png_file), os.path.join(train_images_path, png_file))
        shutil.copy(os.path.join(txt_folder, txt_file), os.path.join(train_labels_path, txt_file))

    # Move validation files
    for png_file, txt_file in val_files:
        shutil.copy(os.path.join(png_folder, png_file), os.path.join(val_images_path, png_file))
        shutil.copy(os.path.join(txt_folder, txt_file), os.path.join(val_labels_path, txt_file))

    print(f"Moved {len(train_files)} files to training set.")
    print(f"Moved {len(val_files)} files to validation set.")

    # Create YAML file
    yaml_data = {
        "path": base_path,  # Base dataset path
        "train": "train/images",  # Training images folder
        "val": "val/images",      # Validation images folder
        "names": class_names      # Class names
    }

    yaml_path = os.path.join(base_path, "dataset.yaml")
    with open(yaml_path, "w") as yaml_file:
        yaml.dump(yaml_data, yaml_file, default_flow_style=False)
    print(f"YAML file created: {yaml_path}")

# Usage
if __name__ == "__main__":
    # Folders containing PNG and TXT files
    png_folder = r"your/project/path/png_files"  # Folder containing PNG files
    txt_folder = r"your/project/path/txt_files"  # Folder containing TXT files

    # Base path for YOLOv8 dataset
    base_path = r"your/project/path"  # Base folder for YOLOv8 dataset

    # Class names
    class_names = ["Sphere"]  # Enter class names here

    # Validation set proportion (20%)
    val_split = 0.2

    # Create folder structure and move files
    create_yolov8_structure_and_move_files(png_folder, txt_folder, base_path, class_names, val_split)
