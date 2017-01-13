# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Define some parameters.
alpha = 3
u_vec = np.linspace(0, 5, 100)
v_vec = np.linspace(0, 5, 100)

# Plot the null clines.
u_null = alpha / (1 + v_vec**2)
v_null = alpha / (1 + u_vec**2)
plt.figure()
plt.plot(u_vec, u_null, '-', label='u')
plt.plot(v_null, v_vec, '-', label='v')
plt.xlabel('u')
plt.ylabel('v')


# Now plot the phase portrait
U, V = np.meshgrid(u_vec[1::5], v_vec[1::5])

# Compute the derivatives.
du_dt = -U + alpha / (1 + V**2)
dv_dt = -V + alpha / (1 + U**2)

plt.quiver(U, V, du_dt, dv_dt, linewidth=1, headwidth=2)
plt.show()
