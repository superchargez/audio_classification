import librosa
from tensorflow import keras
import pandas as pd
model = keras.models.load_model('new_environment50classes.hdf5')

# Classes
CSV_FILE_PATH = r"C:\Users\PTCL\projects\audio\esc50.csv"
df = pd.read_csv(CSV_FILE_PATH)
classes = df['category'].unique()
# class_dict = {i:x for x,i in enumerate(classes)}
class_dict = {x:i for x,i in enumerate(classes)}

# Load audio file
y, sr = librosa.load(r"C:\Users\PTCL\projects\audio\archive\audio\audio\1-977-A-39.wav")

# Set segment length and hop length (in samples)
# segment_length = int(0.5 * sr) # 0.5 seconds
hop_length = int(0.5 * sr) # 0.5 seconds
segment_length = int(5 * sr) # 0.5 seconds

# Split audio into segments
segments = librosa.util.frame(y, frame_length=segment_length, hop_length=hop_length)

# Run classifier on each segment
for i, segment in enumerate(segments.T):
    # mfccs = librosa.feature.mfcc(y = segment, sr=sr)
    mfccs = librosa.feature.mfcc(y= segment , sr=sr, n_mfcc=40)
    # my attempt to reshape
    mfccs = mfccs.reshape(1, mfccs.shape[0], mfccs.shape[1], 1)
    # Run your classifier on mfccs here
    prediction = model.predict(mfccs)
    id = max(enumerate(prediction[0]),key=lambda x: x[1])[0]
    # If sound is detected:
    # timestamp = i * 0.5 # Calculate timestamp in seconds
    timestamp = i * 5 # Calculate timestamp in seconds
    print(f'Sound of {class_dict[id]} detected at {timestamp} seconds')

mfcc2 = librosa.feature.mfcc(y = y, sr=sr, n_mfcc=40)
x = mfcc2.reshape(1, 40, 216, 1)
model.predict(x)
