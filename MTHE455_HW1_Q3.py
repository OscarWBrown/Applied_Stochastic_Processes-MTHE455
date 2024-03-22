import random
import numpy

# Q3
iterations = 10**5
n = random.randint(1, 100)
m = random.randint(1, 100)
red = n 
blu = m
flags = numpy.zeros(iterations, dtype = int)

# new iteration
for x in range(iterations):

    # new game
    while red + blu > 0:
        p_remove_red = red / (red + blu)
        p_remove_blu = blu / (red + blu)
        p = random.random()

        # red is removed if: 0 <= p <= p_remove_red
        # blue is removed if: p_remove_red < p <= 1
        if p <= p_remove_red:
            red = red - 1

        else:
            blu = blu - 1

        # set flags for when red balls >= blue balls
        if red >= blu:
            flags[x] = 1

        else:
            flags[x] = 0

p_n_ge_m = numpy.sum(flags) / iterations

print("For n = " + str(n) + ", and m = " + str(m) + ", for " + str(iterations) + " iterations,\nthe probability that n >= m is " + str(p_n_ge_m))
