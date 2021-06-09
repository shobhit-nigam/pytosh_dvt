import unittest

def add(la, lb):
    return la+lb

class FirstTest(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add(10, 12), 22)
        
unittest.main()
