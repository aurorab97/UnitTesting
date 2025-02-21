import unittest
from math_utils import MathUtils
# from scriptDoveAveteMessoLaClasse Import NomeClasse

class TestMathUtils(unittest.TestCase):
    """
    """
    def test_add(self):
        """
        """
        # è un metodo di TestMathUtils, è derivata da unittest.TestCase
        # se tutti questi 4 test passano allora il metodo passa
        # se solo uno non passa allora il metodo fallisce
        self.assertEqual(MathUtils.add(1, 2), 3)  # se sommo (1 e 2) viene 3
        self.assertEqual(MathUtils.add(1.5, 2.5), 4.0)
        self.assertEqual(MathUtils.add(-1, 1), 0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0.0)


