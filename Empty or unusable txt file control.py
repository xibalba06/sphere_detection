import os

def check_txt_files(txt_folder):
    """
    Checks .txt files and identifies empty or invalid format files.

    Args:
        txt_folder (str): Folder containing .txt files.

    Returns:
        dict: A dictionary containing lists of empty and invalid files.
    """
    empty_files = []  # Empty files
    invalid_files = []  # Invalid format files

    # Get all .txt files
    txt_files = [f for f in os.listdir(txt_folder) if f.endswith(".txt")]

    for txt_file in txt_files:
        txt_path = os.path.join(txt_folder, txt_file)

        # Read the content of the file
        with open(txt_path, "r") as f:
            lines = f.readlines()

        # Check for empty files
        if len(lines) == 0:
            empty_files.append(txt_file)
            continue

        # Check for invalid format files
        for line in lines:
            parts = line.strip().split()
            # YOLO format: Each line must have at least 5 elements (class_id, x_center, y_center, width, height)
            if len(parts) < 5:
                invalid_files.append(txt_file)
                break

    return {"empty_files": empty_files, "invalid_files": invalid_files}

# Usage
if __name__ == "__main__":
    txt_folder = r"your/project/path/txt_files"  # Folder containing .txt files

    # Check the files
    result = check_txt_files(txt_folder)

    # Print the results
    print("Empty files:")
    for file in result["empty_files"]:
        print(f"  - {file}")

    print("\nInvalid format files:")
    for file in result["invalid_files"]:
        print(f"  - {file}")
