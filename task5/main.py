import unittest


def factors(n):
    p = 2
    f = list()
    while n >= p*p :
        if n % p == 0:
            f.append(p)
            n = int(n / p)
        else:
            p = p + 1
        f.append(n)
    return f


def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
        else:
            return True


def vowels(text):
    v = list()
    for i in text:
        if i in 'aeiouAEIOU':
            v.append(i)
    return v


class TestFactors(unittest.TestCase):
    def test_type(self):
        fc_res = factors(16)
        self.assertIsInstance(fc_res, bool, "Wrong return type!")
    def test_wrong_arg(self):
        with self.assertRaises(TypeError):
            factors('1337')
    def test_number(self):
        fc_num = factors(6)
        self.assertEqual(fc_num, [2, 3])
    def test_zero(self):
        fc_zero = factors(0)
        self.assertEqual(fc_zero, [])
    def test_negative(self):
        fc_negative = factors(-6)
        self.assertEqual(fc_negative, [])

class TestPrimes(unittest.TestCase):
    def test_type(self):
        pr_res = is_prime(1)
        self.assertIsInstance(pr_res, bool)
    def test_wrong_arg(self):
        with self.assertRaises(TypeError):
            is_prime('1')
    def test_prime(self):
        pr_res = is_prime(1337)
        self.assertEqual(pr_res, True)
    def test_nonprime(self):
        pr_res = is_prime(42)
        self.assertEqual(pr_res, False)
    def test_negative(self):
        pr_res = is_prime(-322)
        self.assertEqual(pr_res, False)

class TestVowels(unittest.TestCase):
    def test_type(self):
        vw_res = vowels('Never gonna give you up')
        self.assertIsInstance(vw_res, list)
    def test_wrong_arg(self):
        with self.assertRaises(TypeError):
            vowels(1)
    def test_vowels(self):
        vw_res = vowels('Never gonna let you down')
        self.assertEqual(vw_res, ['e', 'e', 'o', 'a', 'e', 'o', 'u', 'o'])
    def test_consonants(self):
        vw_res = vowels('Nvr gnn rn rnd nd dsrt y')
        self.assertEqual(vw_res, [])

unittest.main()
