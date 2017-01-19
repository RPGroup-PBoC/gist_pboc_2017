# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pboc_utils as pboc


plt.close('all')


# infinite monomer pool

# Define some parameters.
r = 20
dt = 1/50
gamma = 1/3
tot_length = 80
tot_time = 100

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
pboc.bar3(prob, bin_step=3)
plt.show()
r = np.logspace(0, -3, tot_length)
gamma = 5
# Finite monomer pool
prob = np.zeros((tot_length + 1, tot_time))
prob[0, 0] = 1.0
for t in range(1, tot_time):
    for ell in range(tot_length):
        prob[ell, t] = prob[ell, t-1] - r[ell] * dt * prob[ell, t-1] + gamma * dt * prob[ell + 1, t-1] - gamma * dt * prob[ell, t-1]
        if ell > 0:
            prob[ell, t] = prob[ell, t] + r[ell - 1] * prob[ell-1, t-1]

pboc.bar3(prob, xlabel='time (steps)', ylabel='length', zlabel='probability')
plt.show()
# Severing proteins
prob = np.zeros((tot_length + 1, tot_time))
r = 20
gamma = 1
prob[0, 0] = 1.0
for t in range(1, tot_time):
    for ell in range(tot_length):
        prob[ell, t] = prob[ell, t-1] - r * dt * prob[ell, t-1] + gamma * (ell + 1) * dt * prob[ell + 1, t-1] - gamma * ell * dt * prob[ell, t-1]
        if ell > 0:
            prob[ell, t] = prob[ell, t] + r * dt * prob[ell - 1, t-1]


pboc.bar3(prob, bin_step=3)
plt.show()
