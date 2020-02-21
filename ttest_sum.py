import unittest
import sum
class ttest_sum(unittest.TestCase):

    def testSum(self):
        ans = sum.add(2,3)
        self.assertEqual(6, ans)
        

if __name__ == '__main__':
    unittest.main()