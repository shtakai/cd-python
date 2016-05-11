import unittest
from insert_value import insert_value_at

class InsertValueTest(unittest.TestCase):
    def setUp(self):
        self.test_list = [0,1,2,3,4]
        self.result = insert_value_at(2, self.test_list, 100)

    def testInsertAtIndexTwo(self):
        return self.assertEqual([0,1,100,2,3,4], self.result)

    def testReturnFalseForInvalidIndex(self):
        self.result = insert_value_at(-1, self.test_list, 100)
        return self.assertEqual(False, self.result)


if __name__ == "__main__":
    unittest.main()
