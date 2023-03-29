import os

# Set the path to the main directory
main_dir = r'C:\Users\PTCL\projects\audio\the50classes'

# Iterate over each subdirectory in the main directory
for subdir, dirs, files in os.walk(main_dir):
    # Iterate over each file in the subdirectory
    for file in files:
        # Check if the file contains the word "mixed" in its name
        if 'mixed' in file:
            # Create the full path to the file
            file_path = os.path.join(subdir, file)
            
            # Delete the file
            os.remove(file_path)