import unittest

lista = [3, 4]
listb = ["hello", "hi", "namaste"]

def add(la, lb):
    return la+lb

class FirstTest(unittest.TestCase):
    ca = 10
    cb = 12

    def setUp(self):
        self.ca = 11       #fails
    
    def test_add_1(self):
        self.assertEqual(add(self.ca, self.cb), 22)

    def test_add_2(self):
        self.assertTrue(listb, "list is empty")

    def test_namaste(self):
        self.assertIn("namaste", listb)

        

if __name__ == '__main__':
    unittest.main()
