import os
import shutil

def organize_files(directory_path):
    # Mapping of extensions to folder names
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css', '.cpp', '.java']
    }

    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} does not exist.")
        return

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Find the extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Move the file based on its extension
        moved = False
        for folder, ext_list in extensions.items():
            if ext in ext_list:
                target_folder = os.path.join(directory_path, folder)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} -> {folder}/")
                moved = True
                break
        
        # If extension is unknown, move to 'Others'
        if not moved:
            others_folder = os.path.join(directory_path, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} -> Others/")

if __name__ == "__main__":
    path = input("Enter the directory path to organize (or press Enter for current directory '.'): ").strip()
    if not path:
        path = "."
    
    organize_files(path)
    print("Optimization Complete!")
