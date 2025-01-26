import os
from pathlib import Path

def rename_png_files(directory):
    """Renames PNG files in the specified directory."""
    # List all PNG files in the directory
    png_files = sorted([f for f in os.listdir(directory) if f.endswith('.png')])

    print(f"Found {len(png_files)} PNG files.")
    print("\nRenaming files...")

    # For each file
    for png_file in png_files:
        # Current file path
        old_path = os.path.join(directory, png_file)

        # Create new name (remove 'rgb_' prefix)
        new_name = png_file.replace('rgb_', '')  # Remove 'rgb_' prefix

        # New file path
        new_path = os.path.join(directory, new_name)

        try:
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {png_file} -> {new_name}")
        except Exception as e:
            print(f"Error: {png_file} could not be renamed - {str(e)}")

    print("\nProcess completed!")

def main():
    # Directory containing PNG files
    png_directory = r"your/project/path/png_files"

    # Check if the directory exists
    if not os.path.exists(png_directory):
        print(f"Error: {png_directory} directory not found!")
        return

    # Show an example file name
    example_files = os.listdir(png_directory)[:1]
    if example_files:
        print(f"Example file name: {example_files[0]}")

    # Get confirmation from the user
    response = input("\nAre you sure you want to rename the files? (yes/no): ")
    if response.lower() != 'yes':
        print("Operation canceled.")
        return

    # Rename the files
    rename_png_files(png_directory)

if __name__ == "__main__":
    main()
