import numpy as np


def calculate():
  list = [0,1,2,3,4,5,6,7,8]
  matrix = np.array(list).reshape(3,3)
  print(matrix)
  calculations = {
    'mean': [matrix.mean(axis=0), matrix.mean(axis=1), matrix.mean()],
    'variance': [matrix.var(axis=0), matrix.var(axis=1), matrix.var()],
    'standard deviation': [matrix.std(axis=0), matrix.std(axis=1), matrix.std()],
    'max': [matrix.max(axis=0), matrix.max(axis=1), matrix.max()],
    'min': [matrix.min(axis=0), matrix.min(axis=1), matrix.min()],
    'sum': [matrix.sum(axis=0), matrix.sum(axis=1), matrix.sum()]
  }
  return calculations