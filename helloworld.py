import os

def print_all_files_in_folder(folder):
    available_files = os.listdir(folder)
    for filename in available_files:
        filename_without_extension = os.path.splitext(filename)[0]
        with open(f"{folder}/{filename}") as f:            
            print(f"{f.read().rstrip()} - by {filename_without_extension}")


print_all_files_in_folder("helloworld")