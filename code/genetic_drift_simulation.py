import numpy as np
import matplotlib.pyplot as plt
import seaborn

# set the alleles:
p = 0.5

# set the population size.
N = 50
num_gen = 100

plt.close('all')
# Think of one-by-one example.
freq_a = []
for i in range(num_gen):
    draw = np.random.rand(N)
    num_a = (draw < p)
    # count how many A's.
    freq = np.sum(num_a) / len(num_a)
    freq_a.append(freq)
    p = freq


gen_vec = np.arange(0, len(freq_a), 1)
plt.figure()
plt.plot(gen_vec, freq_a)
plt.show()

# Now do it a bunch of times.

plt.figure()
num_simulations = 10
for j in range(num_simulations):
    p = 0.5
    freq_a = []
    for i in range(num_gen):
        if (p < 1.0) and (p > 0):
            draw = np.random.rand(N)
            num_a = (draw < p)
            # count how many A's.
            freq = np.sum(num_a) / len(num_a)
            freq_a.append(freq)
            p = freq
    gen_vec = np.arange(0, len(freq_a), 1)
    plt.plot(gen_vec, freq_a)

plt.xlabel('number of generations')
plt.ylabel('allele A frequency')
plt.show()

## Find when first fixation occurs.
#freq_a = np.array(freq_a)
#fixation = np.where((freq_a==1.0) | (freq_a==0))[0]
#
# Now we want to find out the time to fixation.
mean_fixation_time = []
population = [2, 40, 60, 80, 100, 120, 200]
num_simulations = 100
for N in population:
    fixation_time = []
    for i in range(num_simulations):
        p = 0.5
        time = 0
        while (p < 1.0) & (p > 0):
            draw = np.random.rand(N)
            num_a = (draw < p)
            # Count how many a's.
            p = np.sum(num_a) / len(num_a)
            time += 1
        fixation_time.append(time)

    # Compute the mean.
    mean_time = np.mean(fixation_time)
    mean_fixation_time.append(mean_time)

plt.figure()
plt.plot(population, mean_fixation_time, 'o')
plt.xlabel('size of population')
plt.ylabel('time to fixation (generations)')
plt.show()
