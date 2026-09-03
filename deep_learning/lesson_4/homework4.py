import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.callbacks import EarlyStopping, LearningRateScheduler
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)



y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# datagen = ImageDataGenerator(
#     rotation_range=10,
#     width_shift_range=0.1,
#     height_shift_range=0.1,
#     zoom_range=0.1,
#     # brightness_range=[0,1],
#     # shear_range=0.1
# )
# datagen.fit(x_train)

initial_learning_rate = 0.01
batch_size=64
epochs=20

x_train, y_train = x_train[:5000], y_train[:5000]

print(len(x_train), 'train samples')


def lr_schedule(epoch, lr):
    if epoch > 0 and epoch % 3 == 0:
        return lr * 0.5
    return lr

model = Sequential([
    Flatten(input_shape=(28,28,1)),
    Dense(512, activation='relu'),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(10, activation='softmax')
])

model2 = Sequential([
    Flatten(input_shape=(28,28,1)),
    Dense(512, activation='relu'),
    Dense(512, activation='relu'),
    Dense(512, activation='relu'),
    Dense(256, activation='relu'),
    Dense(256, activation='relu'),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(128, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(10, activation='softmax')
])


optimizer = SGD(learning_rate=initial_learning_rate)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# early_stopping = EarlyStopping(monitor='val_loss', patience=0, restore_best_weights=True)
lr_scheduler = LearningRateScheduler(lr_schedule)

history = model.fit(x_train, y_train, batch_size=batch_size,
                    epochs=epochs,
                    validation_data=(x_test, y_test),
                    callbacks=[lr_scheduler])
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"\nTest accuracy: {(test_accuracy*100):.2f}%")


optimizer = SGD(learning_rate=initial_learning_rate)
model2.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# early_stopping = EarlyStopping(monitor='val_loss', patience=0, restore_best_weights=True)
lr_scheduler = LearningRateScheduler(lr_schedule)

history2 = model2.fit(x_train, y_train, batch_size=batch_size,
                    epochs=epochs,
                    validation_data=(x_test, y_test),
                    callbacks=[lr_scheduler])
test_loss, test_accuracy = model2.evaluate(x_test, y_test)
print(f"\nTest accuracy 2: {(test_accuracy*100):.2f}%")


# # Accuracy
# plt.plot(history.history['accuracy'], label='Train Accuracy')
# plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
# plt.title('Training and Validation Accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.show()

# #Loss
# plt.plot(history.history['loss'], label='Train Loss')
# plt.plot(history.history['val_loss'], label='Validation Loss')
# plt.title('Training and Validation Loss')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()
plt.plot(history2.history['accuracy'], label='train Accuracy model2')
plt.plot(history2.history['val_accuracy'], label='validation accuracy model2')
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.title('training and validation accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
plt.show()