# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Define some parameters.
r = 20
gamma = 1/30
k_d = 200

# Plot the nullclines.
num_R = 600
R1 = np.linspace(0, num_R, 500)
R2 = np.linspace(0, num_R, 500)
R1_null = (r / gamma) * 1 / (1 + (R2 / k_d)**2)
R2_null = (r / gamma) * 1 / (1 + (R1 / k_d)**2)


# Plot the nullcline for R2
plt.figure()
plt.plot(R1, R1_null, label='dR1/dt = 0')
plt.plot(R2_null, R2, label='dR2/dt = 0')
plt.xlabel('R1')
plt.ylabel('R2')
plt.legend()

# Generate the phase portrait
# For this, we will need to generate a matrix of values to compute
# the derivatives over. We can do this through the numpy meshgrid function
R1_m, R2_m = np.meshgrid(R1[1::30], R2[1::30])  # only generating every 5th.

# Evaluate teh derivatives
dR1_dt = -gamma * R1_m + r / (1 + (R2_m / k_d)**2)
dR2_dt = -gamma * R2_m + r / (1 + (R1_m / k_d)**2)

# Now plot the vector fields.
plt.quiver(R1_m, R2_m, dR1_dt, dR2_dt)
plt.show()


# Choose a random starting position.
N = 300
R1_init = np.random.rand(N) * num_R
R2_init = np.random.rand(N) * num_R


# Now track the evolution as a function of time.
total_time = 200
R1 = R1_init
R2 = R2_init
colors = sns.color_palette('deep', n_colors=N)
for t in range(total_time):
    dR1 = -gamma * R1 + r / (1 + (R2 / k_d)**2)
    dR2 = -gamma * R2 + r / (1 + (R1 / k_d)**2)
    R1 += dR1
    R2 += dR2

    # Now we'll plot the curve.
    plt.plot(R1, R2, 'r.')
    plt.show()
    plt.draw()
    # Now we'll tell it to wait
    plt.pause(0.005)

#alpha = 3

#u_vec = np.linspace(0, 5, 100)
#v_vec = np.linspace(0, 5, 100)
#
## Plot the null clines.
#u_null = alpha / (1 + v_vec**2)
#v_null = alpha / (1 + u_vec**2)
#plt.figure()
#plt.plot(u_vec, u_null, '-', label='u')
#plt.plot(v_null, v_vec, '-', label='v')
#plt.xlabel('u')
#plt.ylabel('v')jj
#
#
## Now plot the phase portrait
#U, V = np.meshgrid(u_vec[1::5], v_vec[1::5])
#
## Compute the derivatives.
#du_dt = -U + alpha / (1 + V**2)
#dv_dt = -V + alpha / (1 + U**2)
#
#plt.quiver(U, V, du_dt, dv_dt, linewidth=1, headwidth=2)
#plt.show()
