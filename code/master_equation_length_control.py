# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pboc_utils as pboc


plt.close('all')

def master_eq(prob, r, gamma, dt, tot_time, tot_length):
    """Compute the master equation"""
    for t in range(1, tot_time):
        for ell in range(tot_length):
            prob[ell, t] = prob[ell, t-1] - r * dt * prob[ell, t-1] + gamma * dt * prob[ell+1, t-1] - gamma * dt * prob[ell, t-1]
            # Now do the boundary conditions.
            if ell > 0:
                prob[ell, t] = prob[ell, t] + r * dt * prob[ell-1, t-1]
    return prob
# infinite monomer pool
# Define some parameters.
r = 29
dt = 1/50
gamma = 30
tot_length = 20
tot_time = 20

prob = np.zeros((tot_length + 1, tot_time))
prob[0, 0] = 1.0
#prob_inf = master_eq(prob, r, gamma, dt, tot_time, tot_length)


# Finite subunit.
fractional_r = np.logspace(0, -3, tot_length + 1)
prob = np.zeros((tot_length + 1, tot_time))
prob_fin = master_eq(prob, r)


# Make the plot
pboc.bar3(prob_inf, bin_step=3, xlabel='time (steps)', ylabel='length of polymer (monomers)', zlabel='probability')
plt.show()

## Set up the array
#prob = np.zeros((tot_length + 1, tot_time))
#prob[0, 0] = 1.0
#for t in range(1, tot_time):
#    # deal with the initial condition.
#    #prob[0, t] = prob[0, t-1] - r * dt * prob[0, t-1] + gamma * dt * prob[1, t-1] - gamma * dt * prob[0, t-1]
#    # do the rest of the steps
#    for ell in range(tot_length):
#        prob[ell, t] = prob[ell, t-1] - r * dt * prob[ell, t-1] + gamma * dt * prob[ell + 1, t - 1] - gamma * dt * prob[ell, t - 1]
#        if ell > 0:
#            prob[ell, t] = prob[ell, t] + r * dt * prob[ell-1, t-1]
#
## plot it
#pboc.bar3(prob)
#plt.show()
#r = 20
#r_frac = np.logspace(0, -3, tot_length)
#gamma = 5
## Finite monomer pool
#prob = np.zeros((tot_length + 1, tot_time))
#prob[0, 0] = 1.0
#for t in range(1, tot_time):
#    for ell in range(tot_length):
#        prob[ell, t] = prob[ell, t-1] - r * r_frac[ell] * dt * prob[ell, t-1] + gamma * dt * prob[ell + 1, t-1] - gamma * dt * prob[ell, t-1]
#        if ell > 0:
#            prob[ell, t] = prob[ell, t] + r * r_frac[ell - 1] * dt * prob[ell-1, t-1]
#
#pboc.bar3(prob, xlabel='time (steps)', ylabel='length', zlabel='probability', bin_step=5)
#plt.show()
## Severing proteins
#prob = np.zeros((tot_length + 1, tot_time))
#r = 5
#gamma_frac = np.linspace(0, 1, tot_length + 1)
#gamma = 20
#prob[0, 0] = 1.0
#for t in range(1, tot_time):
#    for ell in range(tot_length):
#        prob[ell, t] = prob[ell, t-1] - r * dt * prob[ell, t-1] + gamma * gamma_frac[ell + 1] * dt * prob[ell + 1, t-1] - gamma * gamma_frac[ell] * dt * prob[ell, t-1]
#        if ell > 0:
#            prob[ell, t] = prob[ell, t] + r * dt * prob[ell - 1, t-1]
#
#pboc.bar3(prob, bin_step=5)
#plt.show()
