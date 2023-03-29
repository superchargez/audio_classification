import os
import random
from pydub import AudioSegment
import pandas as pd

# Set the paths
save_path = r'C:\Users\PTCL\projects\audio\the50classes'
audio_file_path = r'C:\Users\PTCL\projects\audio\archive\audio\audio\44100'
csv_file_path = r'C:\Users\PTCL\projects\audio\archive\esc50.csv'

# Read the CSV file using pandas
df = pd.read_csv(csv_file_path)

# Group the DataFrame by category
grouped = df.groupby('category')

# Iterate over each group
for category, group in grouped:
    # Get the list of filenames for this category
    filenames = group['filename'].tolist()
    
    # Create the full path to the destination directory
    dest_dir = os.path.join(save_path, category)
    
    # Create the destination directory if it doesn't already exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Iterate over each filename in the list
    for filename in filenames:
        # Create the full path to the source audio file
        source_path = os.path.join(audio_file_path, filename)
        
        # Load the audio file using pydub
        sound1 = AudioSegment.from_wav(source_path)
        
        # Randomly select two other filenames from the same category
        other_filenames = random.sample(filenames, 2)
        
        # Load the other two audio files using pydub
        sound2 = AudioSegment.from_wav(os.path.join(audio_file_path, other_filenames[0]))
        # sound3 = AudioSegment.from_wav(os.path.join(audio_file_path, other_filenames[1]))
        
        # Mix the three audio files together
        mixed = sound1.overlay(sound2)#.overlay(sound3)
        
        # Create the full path to the destination file
        dest_path = os.path.join(dest_dir, f'mixed_{filename}')
        
        # Export the mixed audio file to the destination directory
        mixed.export(dest_path, format='wav')