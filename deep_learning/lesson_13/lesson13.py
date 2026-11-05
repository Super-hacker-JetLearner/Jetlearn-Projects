import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt


(x_train, _), (x_test, _) = fashion_mnist.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

x_train = x_train.reshape((-1,28,28))
x_test = x_test.reshape((-1,28,28))

noise_factor = 0.5

np.random.seed(55)

x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape)
x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape)

x_train_noisy = np.clip(x_train_noisy, 0., 1.)
x_test_noisy = np.clip(x_test_noisy, 0., 1.)

input_seq = layers.Input(shape=(28,28))

encoded = layers.LSTM(32, activation='relu', return_state=True)(input_seq)

encoded_state = encoded[1]

encoder = models.Model(input_seq, encoded_state)

latent_input = layers.Input(shape=(32,))

decoded = layers.RepeatVector(28)(latent_input)

decoded = layers.LSTM(32, activation='relu', return_sequences=True)(decoded)

decoded = layers.TimeDistributed(
    layers.Dense(28, activation='sigmoid')
)(decoded)

decoder = models.Model(latent_input, decoded)

autoencoder = models.Model(input_seq, decoder(encoder(input_seq)))

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

autoencoder.fit(
    x_train_noisy, x_train,
    epochs=10,
    batch_size=256,
    shuffle=True,
    validation_data=(x_test_noisy, x_test)
)


encoded_imgs = encoder.predict(x_test)

decoded_imgs = autoencoder.predict(x_test_noisy)

n = 10

plt.figure(figsize=(20,6))
for i in range(n):
    ax = plt.subplot(3, n, i+1)
    plt.imshow(x_test[i], cmap='gray')
    ax.set_title("Original")
    ax.axis('off')

    ax = plt.subplot(3, n, i + 1 +n)
    plt.imshow(x_test_noisy[i],cmap='gray')
    ax.set_title("Noisy")
    ax.axis('off')

    ax = plt.subplot(3, n, i+1+2*n)
    plt.imshow(decoded_imgs[i],cmap='gray')
    ax.set_title("Reconstructed")
    ax.axis('off')


plt.tight_layout()
plt.show()