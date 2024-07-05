# import os
# print(os.listdir())



import os

def print_directory_contents(directory):
    # List all files and directories in the given directory
    contents = os.listdir(directory)
    
    # Print each item in the contents list
    for item in contents:
        print(item)

# Example usage:
if _name_ == "_main_":
    directory_path = "C:\Users\91971\kashupython"
    print(f"Contents of directory '{directory_path}':")
    print_directory_contents(directory_path)