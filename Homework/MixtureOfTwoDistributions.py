import scipy.stats as scs
import numpy as np

# consider a random variable that is a mixture of two distributions:
# with a probability of 0.95, its implementation
# is obtained from the distribution N(0, 1),
# and with a probability of 0.05 — from the distribution N(3.9)
selection = scs.bernoulli(0.95).rvs(size=100000)
xs = []
for var in selection:
    if var == 1:
        xs.append(scs.norm.rvs(size=1)[0])
    else:
        xs.append(scs.norm(loc=3, scale=3).rvs(size=1)[0])

# let's calculate the standard deviation of this random variable
var = np.std(xs)
