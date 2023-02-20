import numpy as np
import scipy.stats as scs

def fun(x: float, y: str) -> None:
    print("median of the", y, "distribution :", np.median(x))
    print("average value of the", y, "distribution :", np.std(x))
    print("interquartile range of the", y, "distribution :",
          np.quantile(x, 0.75) - np.quantile(x, 0.25))


# exponential distribution with an intensity of 1
fun(scs.expon.rvs(size=10000), "exponential")

# student distribution with 3 degrees of freedom, with expectation 3 and variance 9
fun(scs.t(df=3, loc=3, scale=3).rvs(size=10000000), "student")


