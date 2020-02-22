import unittest
import sum

class sumTest(unittest.TestCase):

    def testSum(self):
        ans = sum.add(2,3)
        self.assertEqual(5, ans)
        

if __name__ == '__main__':
    unittest.main()