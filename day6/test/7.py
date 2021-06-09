import unittest

lista = [3, 4]
listb = []

def add(la, lb):
    return la+lb

class FirstTest(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add(10, 12), 22)

    def test_add_2(self):
        self.assertTrue(listb, "list is empty")
        

if __name__ == '__main__':
    unittest.main()
