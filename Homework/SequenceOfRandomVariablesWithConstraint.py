import scipy.stats as scs
import numpy as np

xs = []

for var in range(1000000):
    ans = 0
    for index, element in enumerate(scs.expon.rvs(size=1000, scale=1)):
        if t := ans + element <= 10:
            ans += element
        else:
            xs.append(index)
            break

var = np.array(xs)
