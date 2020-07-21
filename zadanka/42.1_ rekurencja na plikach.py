import os



def print_files_path(path: str):
    for element in os.listdir(path):
        if os.path.isdir(os.path.join(path, element)):
            print_files_path(os.path.join(path, element))
        else:
            print(os.path.join(path, element))

print_files_path(r"C:\projekty\python\dir_test")