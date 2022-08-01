import unittest
from unittest import mock
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from Organizer import printLargestDifferent
from unittest.mock import patch
import io

class TestPrintLargestDifferentMethod(unittest.TestCase):

    def test_outValue(self):
        pre_data=[['PREOP', '02afc5d1-9129-46c8-812b-63f9cf408399', '33', 'female', 40.0, 33.0], 
                ['PREOP', 'dd36dd00-ca2f-4e46-816a-aa4c14f3a40b', '22', 'male', 45.0, 60.0], 
                ['PREOP', '4776da07-75e0-45ef-b9ce-6fb83169b074', '22', 'female', 50.0, 80.0], 
                ['PREOP', '801408de-c828-49b2-bdf4-da51fee5cc89', '58', 'male', 100.0, 55.0]]
        
        post_data=[['POSTOP', '02afc5d1-9129-46c8-812b-63f9cf408399', '33', 'female', 70.0, 65.0], 
                ['POSTOP', 'dd36dd00-ca2f-4e46-816a-aa4c14f3a40b', '22', 'male', 90.0, 55.0], 
                ['POSTOP', '4776da07-75e0-45ef-b9ce-6fb83169b074', '22', 'female', 50.0, 80.0], 
                ['POSTOP', '801408de-c828-49b2-bdf4-da51fee5cc89', '58', 'male', 60.0, 25.0]]

        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            printLargestDifferent(pre_data, post_data, "lateral")

        assert fake_stdout.getvalue()=="Patient dd36dd00-ca2f-4e46-816a-aa4c14f3a40b had the largest difference of 45.0\n"

    def test_otherFeatures(self):
        pre_data=[['PREOP', '02afc5d1-9129-46c8-812b-63f9cf408399', '33', 'female', 40.0, 33.0], 
                ['PREOP', 'dd36dd00-ca2f-4e46-816a-aa4c14f3a40b', '22', 'male', 45.0, 60.0], 
                ['PREOP', '4776da07-75e0-45ef-b9ce-6fb83169b074', '22', 'female', 50.0, 80.0], 
                ['PREOP', '801408de-c828-49b2-bdf4-da51fee5cc89', '58', 'male', 100.0, 55.0]]
        
        post_data=[['POSTOP', '02afc5d1-9129-46c8-812b-63f9cf408399', '33', 'female', 70.0, 65.0], 
                ['POSTOP', 'dd36dd00-ca2f-4e46-816a-aa4c14f3a40b', '22', 'male', 90.0, 55.0], 
                ['POSTOP', '4776da07-75e0-45ef-b9ce-6fb83169b074', '22', 'female', 50.0, 80.0], 
                ['POSTOP', '801408de-c828-49b2-bdf4-da51fee5cc89', '58', 'male', 60.0, 25.0]]

        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            printLargestDifferent(pre_data, post_data, "height")
        assert fake_stdout.getvalue()=="Patient 02afc5d1-9129-46c8-812b-63f9cf408399 had the largest difference of 32.0\n"


if __name__ == '__main__':
    unittest.main()