import numpy as np
from config import *
from sklearn.neighbors import KNeighborsRegressor


class Regression:

    def __init__(self, param=None):
        self.param = param

    def fit(self, coord, targets):
        pass

    def get_name(self):
        return self.__class__.__name__ + "(" + str(self.param) + ")"


class PolynomialRegression(Regression):

    def __init__(self, param=default["degree"]):
        super().__init__(param)
        self.param = param

    def fit(self, coord, targets):  # here param is the degree

        p = np.polynomial.Polynomial.fit(coord, targets, self.param)
        return lambda x: np.maximum(0, p(x))

    def is_fittable(self, coord, targets):
        return len(coord) > self.param


class NearestNeighbors1D(Regression):

    def __init__(self, param=default["num_neighbor"]):
        super().__init__(param)
        self.param = param

    def fit(self, coord, targets):
        knnr = KNeighborsRegressor(n_neighbors=self.param)
        knnr.fit(np.array(coord).reshape(-1, 1), targets)
        return lambda x: knnr.predict([[x]])[0]

    def is_fittable(self, coord, targets):
        return len(coord) > self.param
