# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# In this script, we will plot the probability of the states of a simple
# repression promoter. You can imagine that we have one promoter on a bacterial
# chromosome which can bind either a polymerase, a repressor, or be completely
# unbound. By writing out all of the microstates and computing the statistical
# weights, we can arriave at the probability of any state being the weight of
# a single state divided by the sum of weights of all of the possible states.
# We will explore this by plotting the probabiity of all states.

# Define the number of polymerases
P = 5E3  # Number of polymerases
R = np.logspace(-2, 4, 1000)  # Number of repressors
de_p = -8  # In units of kT
de_r = -16  # In units of kT
Nns = 5E6  # Thof e number of nonspecific binding sites for the polymerase and
           # and repressors.

# To make our calculations a bit easier, we will define the partition
# function separately.
Z = 1 + (P / Nns) * np.exp(-de_p) + (R / Nns) * np.exp(-de_r)

# With the partition function defined, we can compute the probabilities of
# observing each state.
p_empty = 1 / Z  # No polymerase bound to the promoter
p_repressor = (R / Nns) * np.exp(-de_r) / Z
p_polymerase = (P / Nns) * np.exp(-de_p) / Z

# We can prove that these are the correct probabilities by making sure they
# all sum to 1.
print(p_empty + p_repressor + p_polymerase)

# We can now plot the probability of each state as a function of repressor
# copy number
plt.figure()
plt.plot(R, p_empty, label='nothing bound')
plt.plot(R, p_repressor, label='repressor bound')
plt.plot(R, p_polymerase, label='polymerase bound')

# To make things easier to understand, we can change the xscale to log.
plt.xscale('log')

# Now we can just add some labels and we are finished!
plt.xlabel('number of repressors')
plt.ylabel('probability')

# And add a legend.
plt.legend()
plt.show()

# We can see that when the number of repressors in the cell increases, the
# probability of having transcription (being a bound polymerase) is very low.
