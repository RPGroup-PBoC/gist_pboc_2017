# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pboc_utils as pboc



# infinite monomer pool

# Define some parameters.
r = 20
dt = 1/50
gamma = 3
tot_length = 50
tot_time = 50

# Set up the array
prob = np.zeros((tot_length + 1, tot_time))
prob[0, 0] = 1.0
for t in range(1, tot_time):
    # deal with the initial condition.
    #prob[0, t] = prob[0, t-1] - r * dt * prob[0, t-1] + gamma * dt * prob[1, t-1] - gamma * dt * prob[0, t-1]
    # do the rest of the steps
    for ell in range(tot_length):
        prob[ell, t] = prob[ell, t-1] - r * dt * prob[ell, t-1] + gamma * dt * prob[ell + 1, t - 1] - gamma * dt * prob[ell, t - 1]
        if ell > 0:
            prob[ell, t] = prob[ell, t] + r * dt * prob[ell-1, t-1]
# plot it
pboc.bar3(prob)
plt.show()

# Finite monomer pool
prob = np.zeros((tot_length + 1, tot_time))
# Severing proteins
