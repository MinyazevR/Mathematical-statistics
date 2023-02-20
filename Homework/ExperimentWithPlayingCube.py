import scipy.stats as scs
import numpy as np

x_k = np.arange(1, 7)
p_k = [1 / 6] * 6
counter = 0
for i in range(1000000):
    if scs.rv_discrete(values=(x_k, p_k)).rvs(size=6).sum() == 21:
        counter += 1
answer = counter / 1000000
