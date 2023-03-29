import os
import librosa
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Set the path to the main directory
main_dir = r'C:\Users\PTCL\projects\audio\the50classes'

# Set the sample rate for the audio files (you can adjust this value)
sample_rate = 22050

# Set the number of mel frequency cepstral coefficients (MFCCs) to extract from each audio file (you can adjust this value)
n_mfcc = 40

# Initialize lists to store the data and labels
data = []
labels = []

# Iterate over each subdirectory in the main directory
for subdir, dirs, files in os.walk(main_dir):
    # Get the category name from the subdirectory name
    category = os.path.basename(subdir)

    # Iterate over each file in the subdirectory
    for file in files:
        # Create the full path to the file
        file_path = os.path.join(subdir, file)
        
        # Load the audio file using librosa
        y, sr = librosa.load(file_path, sr=sample_rate)
        
        # Extract MFCCs from the audio file
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        
        # Add the MFCCs and category to the data and labels lists
        data.append(mfccs)
        labels.append(category)

# Convert the data and labels lists to numpy arrays
data = np.array(data)
labels = np.array(labels)

# Encode the labels as integers
label_map = {label: i for i, label in enumerate(np.unique(labels))}
labels = np.array([label_map[label] for label in labels])

# One-hot encode the labels
num_classes = len(label_map)
labels = to_categorical(labels, num_classes=num_classes)

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# Reshape the data into the shape expected by a convolutional neural network (CNN)
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)

# Create a CNN model using Keras
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(n_mfcc, x_train.shape[2], 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model on the training data
model.fit(x_train, y_train, batch_size=32, epochs=10)

# Evaluate the model on the test data
score = model.evaluate(x_test, y_test)

print(f'Test loss: {score[0]}')
print(f'Test accuracy: {score[1]}')