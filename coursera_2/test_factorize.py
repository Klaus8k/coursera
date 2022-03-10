class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        case = ['string',  1.5]
        for i in case:
            with self.subTest(x=i):
                self.assertRaises(TypeError, factorize, i)

    def test_negative(self):
        case = [-1,  -10,  -100]
        for i in case:
            with self.subTest(x=i):
                self.assertRaises(ValueError, factorize, i)

    def test_zero_and_one_cases(self):
        case = [1, 0]
        for i in case:
            with self.subTest(x=i):
                self.assertEqual(factorize(i), (i,))

    def test_simple_numbers(self):
        case = [3, 13, 29]
        for i in case:
            with self.subTest(x=i):
                self.assertEqual(factorize(i), (i,))

    def test_two_simple_multipliers(self):
        case = [6, 26, 121]
        case_r = [(2, 3), (2, 13), (11, 11)]
        count = 0
        for i in case:
            with self.subTest(x=i):
                self.assertEqual(factorize(i), case_r[count])
            count += 1

    def test_many_multipliers(self):
        case = [1001, 9699690]
        case_r = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        count = 0
        for i in case:
            with self.subTest(x=i):
                self.assertEqual(factorize(i), case_r[count])
            count += 1
