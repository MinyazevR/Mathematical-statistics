import scipy.stats as scs
import numpy as np

xk = np.arange(1, 7)
pk = [1/6] * 6
counter = 0
for i in range(1000000):
    if scs.rv_discrete(values=(xk, pk)).rvs(size=6).sum() == 21:
        counter += 1
print(counter / 1000000)
