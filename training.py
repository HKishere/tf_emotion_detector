#!/usr/bin/python
import tensorflow as tf
print(tf.__version__)

model = tf.keras.Sequential([
                              tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(48, 48, 1)),
                              tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
                              tf.keras.layers.MaxPooling2D(3,3),
                              tf.keras.layers.Flatten(),
                              tf.keras.layers.Dense(1024, activation='relu'),
                              tf.keras.layers.Dense(512, activation='relu'),
                              tf.keras.layers.Dense(7, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(ds)
