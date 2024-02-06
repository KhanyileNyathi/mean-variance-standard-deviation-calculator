import main
import numpy as np
import unittest


class TestMain(unittest.TestCase):

  def test_calculate(self):
    test_list = [0,1,2,3,4,5,6,7,8]
    test_matrix = np.array(test_list).reshape(3,3)
    print(test_matrix)
    calculations =  {
      'mean': [test_matrix.mean(axis=0), test_matrix.mean(axis=1), test_matrix.mean()],
      'variance': [test_matrix.var(axis=0), test_matrix.var(axis=1), test_matrix.var()],
      'standard deviation': [test_matrix.std(axis=0), test_matrix.std(axis=1),
                             test_matrix.std()],
      'max': [test_matrix.max(axis=0), test_matrix.max(axis=1), test_matrix.max()],
      'min': [test_matrix.min(axis=0), test_matrix.min(axis=1), test_matrix.min()],
      'sum': [test_matrix.sum(axis=0), test_matrix.sum(axis=1), test_matrix.sum()]
    }
    return calculations
    

    