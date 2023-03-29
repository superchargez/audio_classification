import os
import shutil
import pandas as pd

# Set the paths
save_path = r'C:\Users\PTCL\projects\audio\the50classes'
audio_file_path = r'C:\Users\PTCL\projects\audio\archive\audio\audio\44100'
csv_file_path = r'C:\Users\PTCL\projects\audio\archive\esc50.csv'

# Read the CSV file using pandas
df = pd.read_csv(csv_file_path)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Get the category and filename from the row
    category = row['category']
    filename = row['filename']
    
    # Create the full path to the source audio file
    source_path = os.path.join(audio_file_path, filename)
    
    # Create the full path to the destination directory
    dest_dir = os.path.join(save_path, category)
    
    # Create the destination directory if it doesn't already exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Copy the file to the destination directory
    shutil.copy(source_path, dest_dir)

# """
# import os
# import shutil
# import csv
# save_path = r"C:\Users\PTCL\projects\audio\the50classes/"
# # Open the CSV file
# with open(r"C:\Users\PTCL\projects\audio\esc50.csv", 'r') as file:
#     reader = csv.DictReader(file)#, delimiter='\t')
    
#     # Iterate over each row in the CSV file
#     for danger in range(10):
#         for row in reader:
#             # Get the category and filename from the row
#             category = row['category']
#             filename = row['filename']
            
#             # Create a directory for the category if it doesn't already exist
#             # if not os.path.exists(category):
#             if not os.path.exists(os.path.join(save_path,category)):
#                 # os.makedirs(category)
#                 os.makedirs(os.path.join(save_path,category))
            
#             # Copy the file to the category directory
#             shutil.copy(filename, os.path.join(save_path+category, filename))
# """