import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the range of values.
phi = np.linspace(0, 1.0, 500)
chi_values = [0.01, 0.1, 0.5, 0.8, 1.0, 2, 3, 10]
plt.close('all')
plt.figure()
for chi in chi_values:
    free_energy = phi * np.log(phi) + (1 - phi) * np.log(1 - phi) + chi * phi * (1 - phi)
    plt.plot(phi, free_energy, '-', label='$\chi$ = ' + str(chi))
plt.xlabel('$\phi$')
plt.ylabel('kT / $\chi$')
plt.legend(loc='upper center')
plt.show()
# phi log phi + 1 - log(phi) + chi * phi * (1 - phi)
