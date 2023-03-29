import os
import random
from pydub import AudioSegment
from pydub.generators import WhiteNoise

# Set the path to the main directory
main_dir = r'C:\Users\PTCL\projects\audio\the50classes'

# Set the maximum volume of the noise in dBFS (you can adjust this value)
max_noise_volume = -20

# Iterate over each subdirectory in the main directory
for subdir, dirs, files in os.walk(main_dir):
    # Iterate over each file in the subdirectory
    for file in files:
        # Create the full path to the file
        file_path = os.path.join(subdir, file)
        
        # Load the audio file using pydub
        sound = AudioSegment.from_wav(file_path)
        
        # Generate random white noise with the same length as the audio file
        noise = WhiteNoise().to_audio_segment(duration=len(sound))
        
        # Set the volume of the noise to a random value between 0 and max_noise_volume
        noise_volume = random.uniform(0, max_noise_volume)
        noise = noise - (noise.dBFS - noise_volume)
        
        # Add the noise to the audio file
        noisy_sound = sound.overlay(noise)
        
        # Export the noisy audio file to a new file
        noisy_file_path = os.path.join(subdir, f'noisy_{file}')
        noisy_sound.export(noisy_file_path, format='wav')