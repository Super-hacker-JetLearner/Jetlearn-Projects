# GAN - generative adversarial networks
# creates new data - like images, music, or text
# it consists of generator and discrimantor
# generator generates data
# discriminator evaluates if it is real or not


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.layers import Input, Conv2D, LeakyReLU, Concatenate, Conv2DTranspose, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import plot_model
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from tensorflow.keras.models import Model

BATCH_SIZE = 16
IMG_SIZE = 128

import kagglehub

path = kagglehub.dataset_download("shravankumar9892/image-colorization")

print("Path to dataset files:", path)


gray_path = "/Users/s932172@aics.espritscholen.nl/.cache/kagglehub/datasets/shravankumar9892/image-colorization/versions/4/l/gray_scale.npy"

df_gray = np.load(gray_path)[:100]
print(df_gray.shape)


def load_images(colorful_images, gray):

    if gray.ndim == 3:
        gray = np.expand_dims(gray,axis=-1)
    
    colorful_images_resized = np.array([cv2.resize(img, (128,128)) for img in colorful_images])
    gray_resized = np.array([cv2.resize(img,(128,128)) for img in gray])

    images = np.zeros(shape=(100,128,128,3), dtype="uint8")

    images[:, :, :, 1:] = colorful_images_resized[:, :, :, 1:]
    images[:, :, :, 0] = gray_resized.squeeze()

    images = np.stack([cv2.cvtColor(img, cv2.COLOR_LAB2RGB) for img in images])
    gray_resized.resize((gray_resized.shape[0], gray_resized.shape[1], gray_resized.shape[2], 1))
    return images, gray_resized

for i in range(1):
    path = path+f'/ab/ab/ab{i+1}.npy'
    color = np.load(path)
    df, df_gray = load_images(color[:100], df_gray[:100])

n_rows, n_cols = 4, 2
fig, axs = plt.subplots(n_rows, n_cols, figsize=(10, 15))

for ax in axs.flatten():
    ax.axis('off')

for i in range(n_rows):
    random_sample = np.random.randint(low=0, high=df.shape[0])
    axs[i, 0].imshow(df[random_sample])
    axs[i, 1].imshow(df_gray[random_sample], cmap='gray')

plt.show()

print(f"The size of colorful images {df.shape}")
print(f"The size of BW images {df_gray.shape}")

X_train, X_test, y_train, y_test = train_test_split(df_gray, df, test_size=0.2)
X_train = X_train / 255.0
X_test = X_test / 255.0
y_train = y_train / 255.0
y_test = y_test / 255.0

dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
dataset.batch(BATCH_SIZE)

def get_generator():
    inputs = Input(shape=(IMG_SIZE, IMG_SIZE, 1))

    conv1 = Conv2D(16, kernel_wize=(5,5), strides=1)(inputs)
    conv1 = LeakyReLU()(conv1)
    conv1 = Conv2D(32, kernel_wize=(3,3), strides=1)(conv1)
    conv1 = LeakyReLU()(conv1)
    conv1 = Conv2D(32, kernel_wize=(3,3), strides=1)(conv1)
    conv1 = LeakyReLU()(conv1)

    conv2 = Conv2D(32, kernel_size=(5,5),strides=1)(conv1)
    conv2 = LeakyReLU()(conv2)
    conv2 = Conv2D(64, kernel_size=(3,3),strides=1)(conv2)
    conv2 = LeakyReLU()(conv2)
    conv2 = Conv2D(64, kernel_size=(3,3),strides=1)(conv2)
    conv2 = LeakyReLU()(conv2)

    conv3 = Conv2D(64, kernel_size=(5,5),strides=1)(conv2)
    conv3 = LeakyReLU()(conv3)
    conv3 = Conv2D(128, kernel_size=(3,3),strides=1)(conv3)
    conv3 = LeakyReLU()(conv3)
    conv3 = Conv2D(128, kernel_size=(3,3),strides=1)(conv3)
    conv3 = LeakyReLU()(conv3)

    bottleneck = Conv2D(
        128, kernel_size=(3,3), strides=1, activation='tanh',padding='same'
    )(conv3)

    concat_1 = Concatenate()([bottleneck, conv3])
    conv_up_3 = Conv2DTranspose(128, kernel_size=(3,3), strides=1, activation='relu')(concat_1)
    conv_up_3 = Conv2DTranspose(128, kernel_size=(3,3), strides=1, activation='relu')(conv_up_3)
    conv_up_3 = Conv2DTranspose(64, kernel_size=(5,5), strides=1, activation='relu')(conv_up_3)

    concat_2 = Concatenate()([conv_up_3, conv2])
    conv_up_2 = Conv2DTranspose(64, kernel_size=(3,3), strides=1, activation='relu')(concat_2)
    conv_up_2 = Conv2DTranspose(64, kernel_size=(3,3), strides=1, activation='relu')(conv_up_2)
    conv_up_2 = Conv2DTranspose(32, kernel_size=(5,5), strides=1, activation='relu')(conv_up_2)

    concat_3 = Concatenate()([conv_up_2, conv1])
    conv_up_1 = Conv2DTranspose(32, kernel_size=(3,3), strides=1, activation='relu')(concat_3)
    conv_up_1 = Conv2DTranspose(32, kernel_size=(3,3), strides=1, activation='relu')(conv_up_1)
    conv_up_1 = Conv2DTranspose(3, kernel_size=(5,5), strides=1, activation='relu')(conv_up_1)

    model = Model(inputs, conv_up_1)
    return model

    
    
