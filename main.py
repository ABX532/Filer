import os
import shutil
import time

print("\033[33m")
print(r"""
███████╗██╗██╗     ███████╗██████╗ 
██╔════╝██║██║     ██╔════╝██╔══██╗
█████╗  ██║██║     █████╗  ██████╔╝
██╔══╝  ██║██║     ██╔══╝  ██╔══██╗
██║     ██║███████╗███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ by ABX
""")
print("\033[0m")


extensions = {
    ".py": "Scripts",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".xlsx": "Documents",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".xz": "Archives",
    ".tgz": "Archives",
    ".cpp": "Scripts",
    ".c": "Scripts",
    ".java": "Scripts",
    ".js": "Scripts",
    ".html": "Scripts",
    ".css": "Scripts",
    ".php": "Scripts",
    ".json": "Scripts",
    ".xml": "Scripts",
    ".exe": "Executables",
    ".AppImage": "Executables",
    ".x86_64": "Executables",
    ".deb": "Packages",
    ".rpm": "Packages",
    ".apk": "Packages",
    ".sh": "Scripts",
    ".iso": "ISOs",
    ".img": "IMGs"
}

file_dir = input("Please put the Folder's path: ")

choise = input("""-Select an option-
1. Organize Folder
2. Dry run(Preview)
3. Exit
Please insert the number of option you want: """)

if choise == "1":
    confirm = input("Process in " + file_dir + " will be started. are you sure you want to continue? (y/n) ").lower()

    moved = 0
    skipped = 0

    if confirm == "y":
        start_time = time.perf_counter()
        time.sleep(0.5)
        print("Process in " + file_dir + " started...")
        time.sleep(1)
        print("Ordering files...")

        folder_files = os.listdir(file_dir)

        for index, file in enumerate(folder_files, start=1): # the original was for file in folder_files: but for moving output i made it like this
            name, ext = os.path.splitext(file)
            if ext in extensions:
                folder_name = extensions.get(ext)
                destination_folder = os.path.join(file_dir, folder_name)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder, exist_ok=True)
                source = os.path.join(file_dir, file)
                shutil.move(source, destination_folder)
                moved += 1
                print(f"[{index}/{len(folder_files)}] ✔ {file} -> {folder_name}")
            else:
                skipped += 1

        end_time = time.perf_counter()
        print("=====================================")
        print("✔ Process finished successfully!")
        print("✔ Moved: " + str(moved) + " files")
        print("✔ Skipped: " + str(skipped) + " files")
        print(f"✔ Time: {end_time - start_time:.2f} seconds")
        print("=====================================")
        print("If there was any files didin't organized. that because it's not supported.") # because not all extensions available in the dictionary
    elif confirm == "n":
        exit() # if user chose no
    else:
        print("You choosed an unavailable option. Please try again.") # if the user didin't chose an available option
elif choise == "2":
    folder_files = os.listdir(file_dir)
    for filee in folder_files:
        namee, exten = os.path.splitext(filee)
        if exten in extensions:
            folder_name = extensions[exten]
            print(filee, "->", folder_name)
    print("Nothing was changed to your system.")
elif choise == "3":
    exit()
else:
    print("You choosed an unavailable option. Please try again.")
