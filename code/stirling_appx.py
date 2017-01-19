import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set up factorials.
n_array = np.arange(0, 15, 1)
n_factorial = []
for n in n_array:
    n_factorial.append(np.math.factorial(n))

appx = n_array * np.log(n_array) - n_array

plt.figure()
plt.plot(n_array, np.log(n_factorial), label='factorial')
plt.plot(n_array, appx, label='approximation')
plt.xlabel('n')
plt.ylabel('n!')
plt.show()
