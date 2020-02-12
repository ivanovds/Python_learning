import unittest

def factorize(x):
    """ 
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
	"""
	Test class for testing factorize(x) function

	"""
	def test_wrong_types_raise_exception(self):
		for i in ['string', 1.5]:
			with self.subTest(x=i):
				self.assertRaises(TypeError, factorize, i)

	def test_negative(self):
		for i in [-1,  -10,  -100]:
			with self.subTest(x=i):
				self.assertRaises(ValueError, factorize, i)

	def test_zero_and_one_cases(self):
		for i in [0, 1]:
			with self.subTest(x=i):
				self.assertEqual(i, (i,))

	def test_simple_numbers(self):
		for i in [3, 13, 29]:
			with self.subTest(x=i):
				self.assertEqual(i, (i,))

	def test_two_simple_multipliers(self):
		cases = [[2, 2, 11], [3, 13, 11]]
		for i in range(3):
			with self.subTest(x=cases[0][i] * cases[1][i]):
				self.assertEqual(cases[0][i] * cases[1][i], (cases[0][i], cases[1][i]))

	def test_many_multipliers(self):
		res = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
		cases = [1001, 9699690]
		for i in range(2):
			with self.subTest(x=cases[i]):
				self.assertEqual(cases[i], res[i])



if __name__ == '__main__':
	unittest.main()