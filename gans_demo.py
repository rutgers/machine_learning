import os
import os.path
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import time

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Reshape
from keras.layers.core import Activation
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import UpSampling2D
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten
from keras.optimizers import SGD
from keras.datasets import mnist
import numpy as np
from PIL import Image
import argparse
import math

# Timer Object
class ElapsedTimer(object):
    def __init__(self):
        self.start_time = time.time()
    def elapsed(self,sec):
        if sec < 60:
            return str(sec) + " sec"
        elif sec < (60 * 60):
            return str(sec / 60) + " min"
        else:
            return str(sec / (60 * 60)) + " hr"
    def elapsed_time(self):
        print("Elapsed: %s " % self.elapsed(time.time() - self.start_time) )

def generator_model():
    """
    Visit keras.io/layers/convolutional/ and keras.io/layers/core/
    to learn more about how to use these functions properly

    Functions to use:
    model.add()
    Sequential()
    Dense(input_dim=x, output_dim=x), & Dense(output_dim)
    Activation('')
    BatchNormalization()
    Reshape((outputSize), input_shape=(x))
    UpSampling2D(size = (x))
    Conv2D(features, (kernal size), padding = 'x')
    """

    # Create a Sequential model
    # Add a Dense layer with an input of 100 and output of 1024 to the model
    # Add a 'tanh' Activation layer
    # Add a Dense layer with an output of 128*7*7
    # Add a BatchNormalization layer
    # Add a 'tanh' Activation layer
    # Add a Reshape layer with an output of (7,7,128) and an input shape of (128*7*7,)
    # Add an UpSampling2D layer with a size of (2,2)
    # Add a Conv2D layer with 64 features, a kernal size of (5,5), and 'same' padding
    # Add a 'tanh' Activation layer
    # Add an UpSampling2D layer with a size of (2,2)
    # Add a Conv2D layer with 1 feature, a kernal size of (5,5), and 'same' padding
    # Add a 'tanh' Activation layer

    # Return your model
    model = #
    model.add()
    model.add()
    # ...
    model.add()
    return model


def discriminator_model():
    """
    Visit keras.io/layers/convolutional/ keras.io/layers/pooling and keras.io/layers/core/
    to learn more about how to use these functions properly

    Functions to use:
    model.add()
    Sequential()
    Dense(input_dim=x, output_dim=x), & Dense(output_dim)
    Activation('')
    Conv2D(features, (kernal size), padding = 'x', input_shape = (input size))
    Conv2D(features, (kernal size))
    Flatten()
    MaxPooling2D(pool_size = (size))
    """

    # Create a Sequential model
    # Add a Conv2D layer with 64 features, a kernal size of (5,5), 'same' padding, and an input_shape of (28,28,1)
    # Add a 'tanh' Activation layer
    # Add a MaxPooling2D layer with a pool_size of (2,2)
    # Add a Conv2D layer with 128 features, and a kernal size of (5,5)
    # Add a 'tanh' Activation layer
    # Add a MaxPooling2D layer with a pool_size of (2,2)
    # Add a Flatten layer
    # Add a Dense layer with an output of 1024
    # Add a 'tanh' Activation layer
    # Add a Dense layer with an output of 1
    # Add a 'sigmoid' Activation layer

    # Return your model

    model = #
    model.add()
    model.add()
    # ...
    model.add()
    return model



def generator_containing_discriminator(g, d):
    """
    Functions to use:
    model.add()
    Sequential()
    x.trainable = False
    """
    # Create a Sequential Model
    # Add your Generator g to your Model
    # Make your Discriminator d untrainable
    # Add your Disciminator d to your Model
    # Return your Model

    model = #
    # ...
    return model


def combine_images(generated_images):
    num = generated_images.shape[0]
    width = int(math.sqrt(num))
    height = int(math.ceil(float(num)/width))
    shape = generated_images.shape[1:3]
    image = np.zeros((height*shape[0], width*shape[1]),
                     dtype=generated_images.dtype)
    for index, img in enumerate(generated_images):
        i = int(index/width)
        j = index % width
        image[i*shape[0]:(i+1)*shape[0], j*shape[1]:(j+1)*shape[1]] = \
            img[:, :, 0]
    return image


def train(BATCH_SIZE, path = ""):
        """
        Functions used:
        mnist.load_data()
        np.astype(type)
        discriminator_model()
        generator_model()
        generator_containing_discriminator()
        SGD(lr = learningrate, momentum = momentum, nesterov = True/False)
        compile(loss = 'model', optimizer = optimizer)
        trainable = True/False
        predict(input, verbose = 0/1)
        np.concatenate( (array1,array2) )
        train_on_batch(inputs, labels)
        """

    timer = ElapsedTimer()


    # Load (X_train, y_train) from mnist
    # Turn X_turn into the float32 type, then normalize by subtracting 127.5 then dividing by 127.5
    # Turn X_train from a 4D dataset to a 3D dataset using X_train[:,:,:,None]

    (X_train, y_train) = #
    X_train = #
    X_train = #

    # Create a Disccriminator d from your discriminator_model
    # Create a Generator g from your generator_model
    # Create an Adverserial model d_on_g from your generator_containing_discriminator, using g and d

    d = #
    g = #
    d_on_g = #

    # Set up the Discrimnator Optimizer d_optim using Standard Gradient Descent (SGD), with a learning rate of 0.0005,a momentum of 0.9, and a nesterov = True parameter
    # Set up the Generator Optimizer g_optim using the exact same function and parameters
    # Compile your Generator g with a loss of 'binary_crossentropy' and an optimizer = 'SGD'
    # Compile your d_on_g with a loss of 'binary_crossentropy' and with g_optim as the optimizer
    # Make your Discrimnator d untrainable
    # Compile your Discriminator d with a loss of 'binary_crossentropy' and with d_optim as the optimizer

    d_optim = #
    g_optim = #
    # ...
    d.compile()

    # Use a consistent noise input for testing purposes
    noise_sample = np.random.uniform(-1.0, 1.0, size=(BATCH_SIZE, 100))

    # For each epoch from 0-n
    for epoch in range(100):
        print("Epoch is", epoch)
        print("Number of batches", int(X_train.shape[0]/BATCH_SIZE))

        # For each set of BATCH_SIZE images from the training set
        for index in range(int(X_train.shape[0]/BATCH_SIZE)):

            # Create a random noise input based on the BATCH_SIZE
            # Get a batch of images to train on from X_train
            noise = np.random.uniform(-1, 1, size=(BATCH_SIZE, 100))
            image_batch = X_train[index*BATCH_SIZE:(index+1)*BATCH_SIZE]

            # Generate images using your Generator g to predict using noise and the parameter verbose = 0
            generated_images = #

            # Plot the Generator Output from the Noise Output
            # Every 20'th cycle...
            if index % 20 == 0:

                # Generate a sample using the Generator G to predict using the noise_sample and the parameter verbose = 0
                generated_sample = #

                # Format and save the image
                image = combine_images(generated_sample)
                image = image*127.5+127.5
                Image.fromarray(image.astype(np.uint8)).save(
                    path + "/" + str(epoch)+"_"+str(index)+".png")

            # Concatenate your image_batch and generated_images into an array X
            # Create an array, y, which has the value 1 for the first BATCH_SIZE elements and 0 for another BATCH_SIZE elements
            # Calculate the disciminator loss, d_loss, from the Disciminator d's train_on_batch function on X and y
            X = #
            y = #
            d_loss = #

            print("Batch %d" % (index))
            print("D_Loss = %f" % (d_loss))

            # Create another set of noise to grain the generator
            noise = np.random.uniform(-1, 1, (BATCH_SIZE, 100))

            # Make the Disciminator d untrainable
            # Calculate the generator loss, g_loss, from d_on_g's train_on_batch function on noise and an array of BATCH_SIZE 1's
            # Make the Disciminator d trainable
            d.trainable = #
            g_loss = #
            d.trainable = #


            print("G_Loss: %f" % (g_loss))
            timer.elapsed_time()
            print()

            # Periodically save the model
            if index % 10 == 9:
                g.save_weights('generator', True)
                d.save_weights('discriminator', True)


def generate(BATCH_SIZE, nice=False):
    """
    Functioned used:

    generator_model()
    compile(loss = 'model', optimizer = 'model')
    load_weights('filename')
    predict(input, verbose = 0/1)
    """
    # Create a generator g from generator_model()
    # Compile g with a loss of 'binary_crossentropy' and an optimizer of 'SGD'
    # Load the weights from the saved file 'generator'
    g = #
    g.compile()
    g.load_weights()

    # Create noise and make a prediction with g from the noise, with a parameter verbose = 1
    noise = np.random.uniform(-1, 1, (BATCH_SIZE, 100))
    generated_images = #

    # Format and save the image
    image = combine_images(generated_images)
    image = image*127.5+127.5
    Image.fromarray(image.astype(np.uint8)).save(
        "generated_image.png")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str)
    parser.add_argument("--path", type=str)
    parser.add_argument("--batch_size", type=int, default=128)
    parser.add_argument("--nice", dest="nice", action="store_true")
    parser.set_defaults(nice=False)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    if args.mode == "train":
        train(BATCH_SIZE=args.batch_size, path = args.path)
    elif args.mode == "generate":
        generate(BATCH_SIZE=args.batch_size, nice=args.nice)
