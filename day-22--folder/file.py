from pathlib import Path
import shutil

# Test folder
source_folder = Path("test_directory")

# File extension categories
categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".docx": "Documents",
    ".csv": "Data",
    ".xlsx": "Data",
    ".py": "Python",
    ".pptx": "Presentations",
    ".zip": "Archives",
    ".rar": "Archives"
}

# Check if the folder exists
if not source_folder.exists():
    print("Test directory does not exist.")
else:
    # Scan all items in the folder
    for file in source_folder.iterdir():

        # Process files only
        if file.is_file():

            # Get the file extension
            extension = file.suffix.lower()

            # Select category
            folder_name = categories.get(extension, "Others")

            # Create destination folder
            destination_folder = source_folder / folder_name
            destination_folder.mkdir(exist_ok=True)

            # Destination file path
            destination = destination_folder / file.name

            # Handle duplicate filenames safely
            if destination.exists():
                print(f"Skipped duplicate file: {file.name}")
                continue

            # Move the file
            shutil.move(str(file), str(destination))

            print(f"Moved: {file.name} -> {folder_name}")

    print("\nFile organization completed!")