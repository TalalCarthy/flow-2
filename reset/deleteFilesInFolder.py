

import os


def deleteFilesInFolder(folder_path):
    # Iterate over files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Check if the path corresponds to a file
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)


__all__ = ['deleteFilesInFolder']
