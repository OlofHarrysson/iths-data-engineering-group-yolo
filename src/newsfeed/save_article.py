import os
import shutil


# Function to take files from input directory and save to destination folder
def save_files(input_directory, destination_directory):
    # loop to iterate through input directory
    for filename in os.listdir(input_directory):
        filepath = os.path.join(input_directory, filename)

        try:  # using shutil to copy our files into a new directory and save them
            shutil.copy(filepath, destination_directory)
            print("Successfully copied file")
        except PermissionError:  # error handling in case we lack permission to handle folders
            print("Permission denied")
        except:  # error message for all other errors
            print("Error while copying file")
