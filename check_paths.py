from pathlib import Path
import os

def check_paths():
    """
    Check folder paths and provide detailed information
    """
    # Define folder paths
    base_dir = Path(r"your/main/project/path")
    image_dir = base_dir / "png_files"
    label_dir = base_dir / "txt_files"
    output_dir = base_dir / "dataset"

    # List folders to check and their descriptions
    paths_to_check = {
        "Base folder": base_dir,
        "Image folder": image_dir,
        "Label folder": label_dir,
        "Output folder": output_dir
    }

    # Check each folder
    for description, path in paths_to_check.items():
        print(f"\nChecking: {description}")
        print(f"Path: {path}")

        if path.exists():
            print("✓ Folder exists")

            # Check folder contents
            if description in ["Image folder", "Label folder"]:
                files = list(path.glob('*.*'))
                print(f"- Number of files: {len(files)}")
                if files:
                    print(f"- Example files: {', '.join(str(f.name) for f in files[:3])}")

            # Check write permissions
            if os.access(path, os.W_OK):
                print("✓ Write permission available")
            else:
                print("✗ No write permission!")
        else:
            print("✗ Folder not found!")

if __name__ == "__main__":
    try:
        check_paths()
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
