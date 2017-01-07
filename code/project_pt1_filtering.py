# Import the necessary modules.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Image processing utilities
import skimage.io
import skimage.morphology
import skimage.filters

# In this script, we'll learn some basic facts about images, how to read them
# in Python, and the basic principles of thresholding. On the course website,
# (rpgroup-pboc.github.io/gist_pboc_2017), you will find a large image set
# that we will use for the whole project. Before we begin, let's talk a bit
# about the nature of the image set.

# These images are of  E. coli cells with a variety of different copy numbers
# of the LacI repressor molecule. This set is composed of three different LacO
# sequences (O1, O2, and O3), and a variety of different repressor copy numbers
# (indicated by the `R` in the image file name).  In these strains (and the #
# `wt` strain), the LacI repressor molecule represses the expression of a
# Yellow Fluorescent Protein molecule. With more repressor around, less YFP
# molecules are made. There are three strains without an `R` label. These are
# `auto` which is expressing no YFP at all, `delta` which is constitutively
# expressing YFP (has no repressors), and `wt` which has the wild-type number
# of LacI repressors, 22 per cell. Every strain is constitutively expressing
# an mCherry molecule off of a plasmid carried in the cell. This was used to
# make the image segmentation more simple.

# In our project, we will quantify the fold-change in gene expression under
# different repressor copy numbers. To do so, we will need to make measurements
# of the single-cell fluorescence intensities in our images. We'll start by
# learning about images and how to process them in the Python programming
# language.

# It is important to remember that an image is nothing but data -- it is an
# array of points with a specific value. These points are called 'pixels'. The
# values that these pixels can take is related to the construction of the
# camera and is measured as 'bit depth'. To determine the range of pixel
# values in an N bit image ca take, we simply need to compute 2^N - 1. This
# subtraction of 1 is because 0 can be a pixel value as well. For example,
# a 16-bit image can have pixels on the range of 0 -> (2^16 -1 ) = 0 -> 65535.
#  Let's begin by loading an example image into Python.

# Define the image name. We'll look at a constitutively expressing case.
image = skimage.io.imread('data/lacI_titration/O2_delta_position_00.tif*')

# Let's look at the values of the image.
np.shape(image)

# We see that this is a 512 x 512 x 3 image. This means it is 512 pixels wide,
# 512 pixels tall, and has three channels. These three channels correspond to
# the phase contrast image, the mCherry image, and the YFP image. Let's take a
# a look at the image and split it up by the channel.

plt.figure()
plt.imshow(image)
plt.show()

# Split the image.
phase = image[:, :, 0]
mch = image[:, :, 1]
yfp = image[:, :, 2]

# To start, let's take a look at the phase contrast image.
plt.figure()
plt.imshow(phase, cmap=plt.cm.Greys_r)
plt.show()

# We see that bacterial cells are black against a light colored background.
# We can take our 'cross' tool in python and hover over the images to see that
# the pixels with in the bacerium are lower than those of the background. We
# could select only the pixels of the bacterium by drawing a threshold at some
# value and saying anything below that value is 'bacterial'. To figure out
# what this threshold should be, we can look at the image histogram and pick a
# value.

# Generate the image histogram.
plt.figure()
plt.hist(phase.flatten(), bins=1000)
plt.xlabel('pixel value')
plt.ylabel('frequency')
plt.show()
