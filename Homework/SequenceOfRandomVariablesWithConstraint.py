import scipy.stats as scs
import numpy as np

xs = []
# K : sum x_i <= 10, 1 <= i <= K
K = 0
i = 0

for var in range(1000000):
    ans = 0
    a = scs.expon.rvs(size=1000, scale=1)
    for i in range(len(a)):
        if ans + a[i] <= 10:
            ans += a[i]
            K = i
        else:
            break
    xs.append(K)

var = np.array(xs)
print(np.std(var)/scs.skew(var))
