import numpy as np
import config as config

from Utility.Regressions.Regression import Regression
from sklearn.neighbors import KNeighborsRegressor


class NearestNeighbors1D(Regression):

    def __init__(self, param=config.default["num_neighbor"]):
        super().__init__(param)
        self.param = param

    def fit(self, coord, target):
        knnr = KNeighborsRegressor(n_neighbors=self.param)
        knnr.fit(np.array(coord).reshape(-1, 1), target)
        return lambda x: knnr.predict([[x]])[0]

    def can_fit(self, coord, targets):
        return len(coord) > self.param

    def get_name(self):
        return "kNN"
