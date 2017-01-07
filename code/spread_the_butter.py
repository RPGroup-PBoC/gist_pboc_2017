import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

plt.close('all')
# In this tutorial, we will expand upon our numerical integration of the mean
# mRNA copy number by solving for the complete mRNA copy number distribution as
# a function of time.

# As is dervied in class, the equation we want to integrate is as follows.
#  dP(m,t)/dt = rP(m -1 ,t) + y(m + 1)P(m+1, t) - rP(m, t) - ymP(m, t)
# where m is the number of mRNAs, t is the timepoint, r is the productionj
# rate of mRNA, y is the degradation rate of the mRNA, and P(m,t) is the
# probability of mRNAs at time t.

# We'll begin our integration by first defining a few parameters.
r = 1  # Production rate of mRNA in 1/min.
gamma = 1 / 3  # Degradation rate of mRNA in 1/min
dt = 0.05  # Time step in units of min
time = 10  # Total time of integration in units of min.
num_steps = int(time / dt)  # Total number of time steps.
upper_bound = 20  # in units of mRNA per cell

# We want to keep track of the probability of each number of mRNAs at each
# individual timepoint. To do so, we'll keep them in a two-dimensional array
# in which each row corresponds to an mRNA and each column is a specific time
# point.

# Construct the two dimensional storage vector.
prob = np.zeros((upper_bound + 1, num_steps))
print(prob)
print(np.shape(prob))

# Now we just to set the initial condition and start the integration.
prob[0, 0] = 1

# Begin the integration.
for t in range(1, int(num_steps)):
    for m in range(upper_bound):
        # Compute P(m, t).
        prob[m, t] = prob[m, t-1] + gamma * dt * prob[m+1, t-1] -\
                     r * dt * prob[m, t-1] - gamma * dt * m * prob[m, t-1]
        # Now include the term if m > 0
        if m > 0:
            prob[m, t] = prob[m, t] + r * dt * prob[m-1, t-1]

# We can now show the distribution of copy numbers at the beginning and end
# of the integration.

# Make a vector of mRNAs.
mRNA_vec = np.arange(0, upper_bound + 1, 1)

# Make a new figure with two plotting axes.
fig, ax = plt.subplots(2, 1)

# Make a bar plot of the time 0 distribution
ax[0].bar(mRNA_vec, prob[:, 0], color='b', width=1)
ax[0].set_ylabel('probability')
ax[0].set_title('t=0 min')
ax[1].bar(mRNA_vec, prob[:, -1], color='g', width=1)
ax[1].set_title('t=5 min')
ax[1].set_ylabel('probability')
ax[1].set_xlabel('number of mRNAs')
plt.show()


# To get a better sense of how the distribution changes with time, let's make
# a bar plot for each point in time and plot it in three dimensions.
# Set up the plotting figure
fig = plt.figure()

# Add a three-dimensional axis.
ax = fig.add_subplot(1, 1, 1, projection='3d')
# The '1,1,1' sets up a single plotting axis in the figure.

# Generate a time vector.
time_vec = np.linspace(0, time, num_steps)

# Set a colormap that will corespond to time.
colors = sns.color_palette('viridis', n_colors=num_steps)

# Loop through each time step and plot the bar.
for i in range(num_steps):
    ax.bar(mRNA_vec, prob[:, i], time_vec[i], zdir='x', width=1, color=colors[i])

# Add axis labels.
ax.set_xlabel('time (min)')
ax.set_ylabel('number of mRNAs')
ax.set_zlabel('probability')

# Rotate the plot for viewing in this notebook.
ax.view_init(15, 15)
plt.show()
