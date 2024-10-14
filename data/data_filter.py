import os

# Folder path (the folder containing the images to be checked and deleted)
folder_path = '../data_test'

# Path to the train_list file (the file that contains the filenames to keep)
train_list_file = './train_list.txt'

# Read the train_list file and get the list of filenames to keep
with open(train_list_file, 'r') as f:
    train_list = f.read().splitlines()

# Loop through the files in the folder
for filename in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, filename)

    # Check if the file is not in the train_list, and if so, delete it
    if filename not in train_list:
        try:
            os.remove(file_path)
            print(f'Deleted: {filename}')
        except Exception as e:
            print(f'Failed to delete {filename}, error: {e}')

print("Cleanup completed!")
