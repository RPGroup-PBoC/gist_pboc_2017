# Import the necessary modules.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For image processing.
import skimage.io

# For file management
import glob

# Utilities for our course.
import pboc_utils as pboc


# Plot the theory first.
ops = ['O1', 'O2', 'O3']
binding_energy = [-15.3, -13.9, -9.3]  # in units of kBT

def fold_change(R, binding_energy, Nns=5E6):
    """
    Computes fold change.
    """
    return 1 / (1 + (R/Nns) * np.exp(-binding_energy))
R = np.logspace(0, 4, 500)


plt.figure()
colors = ['r', 'g', 'b']
for i in range(len(binding_energy)):
    fc = fold_change(R, binding_energy[i])
    plt.plot(R, fc, '-', color=colors[i], label=ops[i] + ' theory')


plt.xlabel('number of repressors')
plt.ylabel('fold-change')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.show()


# Check our data. Get auto and delta data first.
rep_names = ['auto', 'delta', 'wt', 'R60', 'R124', 'R260', 'R1220', 'R1740']
rep_numbers = [11, 60, 124, 260, 1220, 1740]

auto_means = []
delta_means = []
thresh = -0.2
# Loop through each operator.
for i in range(len(ops)):
    for j in range(2):
        phase_names = glob.glob('data/lacI_titration/' + ops[i] + '_' + rep_names[j] + '_phase*.tif')
        fluo_names = glob.glob('data/lacI_titration/' + ops[i] + '_'  + rep_names[j] + '_yfp*.tif')

        # Do the image processing.
        intensities = []
        for k in range(len(phase_names)):
            phase_im = skimage.io.imread(phase_names[k])
            fluo_im = skimage.io.imread(fluo_names[k])
            seg = pboc.phase_segmentation(phase_im, thresh)
            ints = pboc.extract_intensity(seg, fluo_im)
            for val in ints:
                intensities.append(val)

        # Compute the mean.
        mean_int = np.mean(intensities)

        # Decide what vector to add this to.
        if rep_names[j] == 'auto':
            auto_means.append(mean_int)
        if rep_names[j] == 'delta':
            delta_means.append(mean_int)


# Now do this over the other samples except calculate fold-change.

for i in range(len(ops)):
    fc = []
    for j in range(2, len(rep_names)):
        phase_names = glob.glob('data/lacI_titration/' + ops[i] + '_' + rep_names[j] + '_phase*.tif')
        fluo_names = glob.glob('data/lacI_titration/' + ops[i] + '_' + rep_names[j] + '_yfp*.tif')
        # Do the image processing.
        intensities = []
        for k in range(len(phase_names)):
            phase_im = skimage.io.imread(phase_names[k])
            fluo_im = skimage.io.imread(fluo_names[k])
            seg = pboc.phase_segmentation(phase_im, thresh)
            ints = pboc.extract_intensity(seg, fluo_im)
            for val in ints:
                intensities.append(val)

        # Compute the mean intensity for this repressor copy number.
        mean_int = np.mean(intensities)

        # Compute the fold change
        fc.append((mean_int - auto_means[i]) / (delta_means[i] - auto_means[i]))

    # Add the fold change to the correct storage vector.
    if ops[i] == 'O1':
        O1_fc = fc
    if ops[i] == 'O2':
        O2_fc = fc
    if ops[i] == 'O3':
        O3_fc = fc


# Now Let's plot it on our figure.
plt.figure()
colors = ['r', 'g', 'b']
for i in range(len(binding_energy)):
    fc = fold_change(R, binding_energy[i])
    plt.plot(R, fc, '-', color=colors[i], label=ops[i] + ' theory')

# Now plot the experimental data.
plt.plot(rep_numbers, O1_fc, 'ro', label='O1 data')
plt.plot(rep_numbers, O2_fc, 'go', label='O2 data')
plt.plot(rep_numbers, O3_fc, 'bo', label='O3 data')

plt.xlabel('number of repressors')
plt.ylabel('fold-change')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.show()
