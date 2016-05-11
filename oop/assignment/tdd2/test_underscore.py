import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
        self.test_list = [1,2,3,4,5]


    def testMap(self):
        self.assertEqual([1,4,9,16,25], self._.map(self.test_list, lambda x: x*x))
        self.assertNotEqual([1,4,9,16,25], self._.map(self.test_list, lambda x: x*3))



    def testReduce(self):
        self.assertEqual(15, self._.reduce(self.test_list, lambda x,y: x+y, 0))
        self.assertNotEqual(15, self._.reduce(self.test_list, lambda x,y: x*y, 0))

    def testFind(self):
        self.assertEqual(4, self._.find(self.test_list, lambda x: x==4))
        self.assertFalse(self._.find(self.test_list, lambda x: x==8))

    def testFilter(self):
        self.assertEqual([3], self._.filter(self.test_list, lambda x: x%3==0))
        self.assertEqual([2,4], self._.filter(self.test_list, lambda x: x%2==0))

    def testReject(self):
        self.assertEqual([1,2,4,5], self._.reject(self.test_list, lambda x: x%3==0))
        self.assertEqual([1,3,5], self._.reject(self.test_list, lambda x: x%2==0))


if __name__ == "__main__":
    unittest.main()
