import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# --- DATA PREPARATION ---
# Raw dataset: two numeric features + a binary label (0 or 1).
# This is the "input value" source we discussed — these numbers
# ARE the x_i values that will enter the first layer.
data = {
    'feature1': [0.1, 0.2, 0.3, 0.4, 0.5],
    'feature2': [0.5, 0.4, 0.3, 0.2, 0.1],
    'label': [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
X = df[['feature1', 'feature2']].values   # shape (5, 2) -> 5 samples, 2 inputs each
y = df['label'].values                     # shape (5,)  -> the true labels (ground truth)

# --- MODEL ARCHITECTURE (defines where weights/bias will live) ---
model = Sequential()

# Hidden layer: 8 neurons, each takes 2 inputs (input_dim=2).
# Internally Keras creates a weight matrix W1 of shape (2, 8)
# and a bias vector b1 of shape (8,) — one weight per (input, neuron)
# connection, one bias per neuron. All initialized RANDOMLY here,
# not meaningfully "important" yet — that comes from training.
model.add(Dense(8, input_dim=2, activation='relu'))

# Output layer: 1 neuron, takes the 8 hidden activations as its input.
# Weight matrix W2 shape (8, 1), bias b2 shape (1,).
# Sigmoid squashes the raw output z into a (0,1) probability —
# this is what makes it interpretable as "probability of class 1".
model.add(Dense(1, activation='sigmoid'))

# --- COMPILE (defines the loss function and the update rule) ---
# loss='binary_crossentropy' -> the function that measures how wrong
#   the prediction is vs. the true label (used in the loss step).
# optimizer='adam' -> the specific gradient descent VARIANT used to
#   update weights and bias during the backward pass (adaptive learning rate).
# metrics=['accuracy'] -> just for us to monitor, not used in the math.
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# --- TRAINING LOOP (forward -> loss -> backward -> update, repeated) ---
# epochs=100 -> the whole dataset is passed through 100 times.
# batch_size=1 -> weights/bias updated after EVERY single sample
#   (this is "online"/stochastic gradient descent, not batch GD).
# Per sample, per epoch, Keras internally does exactly the 6-step
# flow from before: forward pass -> prediction -> loss -> backprop
# (gradients for every weight/bias) -> gradient descent update.
model.fit(X, y, epochs=100, batch_size=1, verbose=1)

# --- INFERENCE (forward pass only, no learning) ---
# A brand-new input never seen during training.
test_data = np.array([[0.2, 0.4]])

# Only the FORWARD phase runs here: input -> hidden layer
# (weights+bias+relu) -> output layer (weights+bias+sigmoid) -> probability.
# No loss, no backprop, no weight update — the model is frozen.
prediction = model.predict(test_data)

# Thresholding: sigmoid gives a probability (e.g. 0.73).
# > 0.5 converts it into a hard class label (0 or 1).
predicted_label = (prediction > 0.5).astype(int)