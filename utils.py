import numpy as np


def estimate_gaussian(feature):
    n = np.size(feature, 1)
    m = np.size(feature, 0)
    mu = np.zeros((n, 1))
    sigma2 = np.zeros((n, 1))

    mu = np.reshape((1 / m) * np.sum(feature, 0), (1, n))
    sigma2 = np.reshape((1 / m) * np.sum(np.power((feature - mu), 2), 0), (1, n))

    return mu, sigma2