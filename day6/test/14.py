import unittest


lista = [3, 4]
listb = ["hello", "hi", "namaste"]
listc = []

def add(la, lb):
    return la+lb

class FirstTest(unittest.TestCase):
    ca = 10
    cb = 12

    @unittest.skipIf(cb>ca, "skip is cb is greater than ca")
    def test_add_1(self):
        self.assertEqual(add(self.ca, self.cb), 25)
        
    @unittest.skipUnless(cb == 11, "skip if cb is equal to 12")
    def test_add_2(self):
        self.assertTrue(listc, "list is empty")
        
    @unittest.expectedFailure
    def test_namaste(self):
        self.assertIn("ola", listb)

        

if __name__ == '__main__':
    unittest.main()
