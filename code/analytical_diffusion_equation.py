# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# In this script we will plot the analytical solution of the process of
# one-dimensional diffusion as a function of time. In class, we derived that
# the concentration of molecules at position x at time t can be written as
#
#         c(x, t) = N / sqrt(4 * pi * D * t) * exp(-x^2 / 4 * D * t)
#
# where D is the diffuision constant of the molecule, N is the number of
# molecules, and t is the time. Assuming we have a large spike of molecules
# positioned at the origin at time 0, let's see how the concentration profile
# canges with time.

N = 100  # number of molecules.
D = 0.1  # Diffusion constant in square microns per second
time_steps = [1, 5, 10, 50]
x = np.linspace(-10, 10, 1000)  # Diffusion distance in units of microns.

# Now we can loop through each time step to and evaluate our equation.
plt.figure()
for t in time_steps:
    c_t = N / np.sqrt(4 * np.pi * D * t) * np.exp(-x**2 / (4 * D * t))

    # Plot the profile as a funxiton of x position
    plt.plot(x, c_t, '-', label='time = ' + str(t) + ' seconds')

plt.xlabel(r'x position ($\mu$m)')
plt.ylabel(r'$c (x, t)$ (number of molecules)')
plt.legend()
plt.show()

# We see that the profile is gaussian and widens with a longer period of time.