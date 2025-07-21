import unittest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from src.model import train_model

class TestModel(unittest.TestCase):
    def test_model_training(self):
        data = load_iris()
        X_train, _, y_train, _ = train_test_split(data.data, data.target)
        model = train_model(X_train, y_train)
        self.assertTrue(hasattr(model, "predict"))
