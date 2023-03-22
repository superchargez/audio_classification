import librosa
from tensorflow import keras
import pandas as pd

model = keras.models.load_model(r"C:\Users\PTCL\projects\audio\environment50classes.hdf5")

# Classes
CSV_FILE_PATH = r"C:\Users\PTCL\projects\audio\esc50.csv"
df = pd.read_csv(CSV_FILE_PATH)
classes = df['category'].unique()

# get audio data and rate of recording
y, sr = librosa.load(r"C:\Users\PTCL\projects\audio\combined.wav")

# Set segment length and hop length (in samples)
hop_length = int(0.5 * sr) # 0.5 seconds
segment_length = int(5 * sr) # 5 seconds

# Split audio into segments
segments = librosa.util.frame(y, frame_length=segment_length, hop_length=segment_length)

def theOut(segment):
    mfcc2 = librosa.feature.mfcc(y = segment, sr=sr, n_mfcc=40)
    x = mfcc2.reshape(1, 40, 216, 1)
    mfcc_predicted = model.predict(x)
    prediction = classes[mfcc_predicted[0].argmax()]
    return prediction

for i, segment in enumerate(segments.T):
    print(f"Sound of {theOut(segment)} was heard in segment {i+1} at {(i*segment_length)/sr} seconds")
