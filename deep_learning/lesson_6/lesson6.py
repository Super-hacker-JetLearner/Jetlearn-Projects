import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

vehicle_classes = [0,1,8,9]
animal_classes = [2,3,4,5,6,7]

y_train_binary = [(1 if label in vehicle_classes else 0) for label in y_train.flatten()]
y_test_binary = [(1 if label in vehicle_classes else 0) for label in y_test.flatten()]

y_train_binary = to_categorical(y_train_binary, 2)
y_test_binary = to_categorical(y_test_binary, 2)

x_train, x_test = x_train / 255.0, x_test / 255.0

model = models.Sequential([
    layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32,32,3)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3,3),activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(2, activation='softmax')
])


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train_binary, epochs=10,
                    validation_data=(x_test, y_test_binary))

test_loss, test_acc = model.evaluate(x_test, y_test_binary, verbose=2)
print(f"\nTest accuracy: {test_acc:.2f}")

import numpy as np
import matplotlib.pyplot as plt

predictions = model.predict(x_test)

def display_prediction(index):
    plt.imshow(x_test[index])
    plt.axis('off')
    actual_label = "Vehicle" if np.argmax(y_test_binary[index]) == 1 else "Animal"
    predicted_label = "Vehicle" if np.argmax(predictions[index]) == 1 else "Animal"
    plt.title(f"Actual: {actual_label}, Predicted: {predicted_label}")
    plt.show()

for i in [0,10,25,50,100]:
    display_prediction(i)
    

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay



predicted_classes = np.argmax(predictions, axis=1)
actual_classes = np.argmax(y_test_binary, axis=1)

def is_wrong(index):
    if np.argmax(y_test_binary[index]) != np.argmax(predictions[index]):
        return True
    
wrongs = 0
for i in range(len(predictions)):
    if is_wrong(i):
        wrongs += 1
        display_prediction(i)
    if wrongs == 5:
        break



cm = confusion_matrix(actual_classes, predicted_classes)
ConfusionMatrixDisplay(cm, display_labels=["Animal", "Vehicle"]).plot()
plt.show()

