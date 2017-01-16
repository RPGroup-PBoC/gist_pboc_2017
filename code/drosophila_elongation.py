# Import the necessary modules.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For getting file names.
import glob

# For image processsing.
import skimage.io
import skimage.filters
import skimage.segmentation
import skimage.measure

# In this exercise, we will measure the rate of transcription in a nuclear
# cycle 14 of a developing Drosophila melanogaster embryo. Specificially, we
# are watching the beginning and end of transcription of the Hunchback
# morphogen. This was done in a particularly clever way by using the MS2 system
# to tag the 5' and 3' ends of the mRNA in separate embryos. In this
# experimental systems, fluorescent puncta appear when that region of the mRNA
# is properly transcribed. By watching the appearance of the relevant spots, we
# can make a measurement of the rate of transcription and investigate whether
# the timing makes sense, given the time in between nuclear divisions.

# In this exercise, we will measure the rate of transcription in a nuclear
# cycle 14 of a developing Drosophila melanogaster embryo. Specificially, we
# are watching the beginning and end of transcription of the Hunchback
# morphogen. This was done in a particularly clever way by using the MS2 system
# to tag the 5' and 3' ends of the mRNA in separate embryos. In this
# experimental systems, fluorescent puncta appear when that region of the mRNA
# is properly transcribed. By watching the appearance of the relevant spots, we
# can make a measurement of the rate of transcription and investigate whether
# the timing makes sense, given the time in between nuclear divisions.

# To begin with, let's take a look at an image somewhere in the middle of the
# movie for the 5' labeled mRNA case.
im = skimage.io.imread('data/fly_elongation/5Loops0200.tif')
plt.figure()
plt.imshow(im, cmap=plt.cm.viridis)
plt.show()

# How can we count? It seems like we would be able to threshold
# the images to find the spots. To pick a threshold, let's take a look at the
# histogram.
plt.figure()
plt.hist(im.flatten(), bins=1000)
plt.xlabel('pixel value')
plt.ylabel('counts')

# We see that we have a very large peak which corresponds to the background
# pixels and a long tail to the right which likely corresponds to our spots.
# Let's try applying a threshold of 0.11 and see how we've done.
im_thresh = im > 900
plt.figure()
plt.imshow(im_thresh, cmap=plt.cm.viridis)
plt.show()

# That seems to do a pretty good job! But we still have some spots right on the edge which are unclear if they are spots or not. To prevent our selves from overcounting, we can remove any spots touching the border.
im_border = skimage.segmentation.clear_border(im_thresh)

#We can individually label each spot and count them to double check our segmentation.
im_lab, num_spots = skimage.measure.label(im_border, return_num=True)
print('There are ' + str(num_spots) + ' mRNA spots in this image.')


# That is pretty good, it matches our count by eye exactly!  Our goal is to
# count the number of spots per frame and plot their arrival as a function of
# time. With about 300 frames, this is too much to do by hand. Let's write a
# function so this can be automated.
def spot_counter(im, threshold):
    """Counts the number of puncta in an image"""

    # Threshold the image.
    im_thresh = im > threshold

    # Clear the border.
    im_border = skimage.segementation.clear_border(im_thresh)

    # Label the image and return the number of spots.
    im_lab, num_spots = skimage.measure.label(im_border)
    return num_spots


# Now let's iterate over all of the 5' labeled images. We can get all of the
# files through using glob.
spots_5p =
