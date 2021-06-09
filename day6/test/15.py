import unittest
import time
import timeout_decorator

def add(la, lb):
    return la+lb

class FirstTest(unittest.TestCase):
    ca = 10
    cb = 12

    @timeout_decorator.timeout(4)
    def test_add_1(self):
        for i in range(6):
            time.sleep(1)
        self.assertEqual(add(self.ca, self.cb), 22)
        

        

if __name__ == '__main__':
    unittest.main()
