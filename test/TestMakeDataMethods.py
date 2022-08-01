import unittest
import sys
sys.path.append('../data')
from Organizer import makeData

class TestMakeDataMethods(unittest.TestCase):

    def test_makeData(self):
        ansList=["POSTOP", "02afc5d1-9129-46c8-812b-63f9cf408399", "33", "female", 70.0, 65.0]
        self.assertEqual(makeData(1, "POSTOP",), ansList)

    def test_makeDataLowercase(self):
        ansListFemale=["PREOP", "4776da07-75e0-45ef-b9ce-6fb83169b074", "22", "female", 50.0, 80.0]
        self.assertEqual(makeData(5, "PREOP"), ansListFemale)
        ansListMale=["POSTOP", "dd36dd00-ca2f-4e46-816a-aa4c14f3a40b", "22", "male", 90.0, 55.0]
        self.assertEqual(makeData(3, "POSTOP"), ansListMale)

    def test_consistentDelimiter(self):
        ansList=["PREOP", "02afc5d1-9129-46c8-812b-63f9cf408399", "33", "female", 40.0, 33.0]
        self.assertEqual(makeData(2, "PREOP"), ansList)

    def test_considerBounces(self):
        ansListCorrect=["POSTOP", "dd36dd00-ca2f-4e46-816a-aa4c14f3a40b", "22", "male", 90.0, 55.0]
        ansListIncorrect=["POSTOP", "dd36dd00-ca2f-4e46-816a-aa4c14f3a40b", "22", "male", 110.0, 55.0]
        self.assertEqual(makeData(3, "POSTOP"), ansListCorrect)
        self.assertFalse(makeData(3, "POSTOP") == ansListIncorrect)

if __name__ == '__main__':
    unittest.main()