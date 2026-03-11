import os
import shutil

# Define your categories
DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".tar", ".rar"],
    "Scripts": [".py", ".js", ".html"]
}

def organize_folder(target_path):
    for filename in os.listdir(target_path):
        filepath = os.path.join(target_path, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
            
        # Get extension and move
        extension = os.path.splitext(filename)[1].lower()
        for category, extensions in DIRECTORIES.items():
            if extension in extensions:
                dest_dir = os.path.join(target_path, category)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_dir, filename))
                print(f"Moved: {filename} -> {category}")

if __name__ == "__main__":
    # Change this to your actual Downloads path
    path = os.path.expanduser("~/Downloads")
    organize_folder(path)
