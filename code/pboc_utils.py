"""
This script contains an array of functions for use in the physical biology of
the cell course at the Gwangju Institute of Science and Technology in Gwangju,
PRK. These functions were written by Griffin Chure and carry an MIT license.
"""
import numpy as np
import matplotlib.pyplot as plt
import skimage.io
import skimage.segmentation
import skimage.filters
import skimage.measure


# We'll start with the segmentation function.
def phase_segmentation(image, threshold, area_bounds=[0.5, 6.0],
                       ip_dist=0.160):
    """
    Segement a phase image and return the mask.

    Parameters
    ----------
    image : 2d-array
        The phase image to be segmented. This image will be converted to a
        float type.
    threshold : float
        Threshold value for the segmentation. This function will select objects
        below this threshold value.
    area_bounds : list, default=[0.5, 6.0]
        Area bounds for identified objects. This should be a list of two entries.
    ip_dist : int or float, default = 0.160
        Interpixel distance for the camera. This should be in units of microns
        per pixel.

    Returns
    -------
    final_seg : 2d-array
        Final, labeled segmentation mask.
    """

    # First is to convert the image to a float.
    im_float = (image - image.min()) / (image.max() - image.min())

    # Do a background subtraction.
    im_blur = skimage.filters.gaussian(im_float, sigma=50.0)
    im_sub = im_float - im_blur

    # Apply the threshold.
    im_thresh = im_sub < threshold  # Note that we are using the provided arg

    # Label the image and apply the area bounds.
    im_lab = skimage.measure.label(im_thresh)
    props = skimage.measure.regionprops(im_lab)
    approved_objects = np.zeros_like(im_lab)
    for prop in props:
        area = prop.area * ip_dist**2
        if (area > area_bounds[0]) & (area < area_bounds[1]):
            approved_objects += im_lab == prop.label

    # Clear the border and relabel.
    im_border = skimage.segmentation.clear_border(approved_objects > 0)
    final_seg = skimage.measure.label(im_border)

    # Return the final segmentation mask
    return final_seg


# Now let's try writing one for to extract the mean intensities.
def extract_intensity(seg, fluo_im):
    """
    Extracts the mean intensity of objects in a segmented image.

    Parameters
    ----------
    seg : 2d-array, int
        Segmentation mask with labeled objects.
    fluo_im : 2d-array, int
        Fluorescence image to extract intensities from.

    Returns
    -------
    cell_ints : 1d-array
        Vector of mean cell intensities. This has a length the same as the
        number of objects in the provided segmentation mask.
    """

    # Get the region props of the fluorescence image using the segmentation
    # mask.
    props = skimage.measure.regionprops(seg, intensity_image=fluo_im)
    cell_ints = []
    for prop in props:
        cell_ints.append(prop.mean_intensity)

    # Convert the cell_ints to an array and return.
    return np.array(cell_ints)



def bar3(data, xlabel, ylabel, zlabel, bin_step=1):
    return True
