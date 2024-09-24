import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense


# Step 1: Define XOR input and output
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input for XOR
y = np.array([[0], [1], [1], [0]])              # Expected output for XOR

# Step 2: Build the neural network model
model = Sequential()

# Input layer + hidden layer (2 neurons) with activation function 'relu'
model.add(Dense(2, input_dim=2, activation='relu'))

# Output layer with 1 neuron and 'sigmoid' activation function
model.add(Dense(1, activation='sigmoid'))

# Step 3: Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Step 4: Train the model
model.fit(X, y, epochs=1000, verbose=0)  # Train for 1000 epochs

# Step 5: Test the model
predictions = model.predict(X)

# Print the results
print("\nPredictions:")
for i in range(len(X)):
    print(f"Input: {X[i]} => Predicted Output: {np.round(predictions[i])}, Expected Output: {y[i]}")
