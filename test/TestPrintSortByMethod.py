
import unittest
from unittest import mock
import sys
sys.path.append('../data')
from Organizer import printSortBy
from unittest.mock import patch
import io

class TestPrintSortedByMethod(unittest.TestCase):
    def test_outValue(self):
        
        post_data=[['POSTOP', '02afc5d1-9129-46c8-812b-63f9cf408399', '33', 'female', 70.0, 65.0], 
                ['POSTOP', 'dd36dd00-ca2f-4e46-816a-aa4c14f3a40b', '22', 'male', 90.0, 55.0], 
                ['POSTOP', '4776da07-75e0-45ef-b9ce-6fb83169b074', '22', 'female', 50.0, 80.0], 
                ['POSTOP', '801408de-c828-49b2-bdf4-da51fee5cc89', '58', 'male', 60.0, 25.0]]
        
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            printSortBy(post_data, ["age", "lateral"], reverse=False)
        
        assert fake_stdout.getvalue() == "Post op by age and throw:\n4776da07-75e0-45ef-b9ce-6fb83169b074 22 50.0\ndd36dd00-ca2f-4e46-816a-aa4c14f3a40b 22 90.0\n02afc5d1-9129-46c8-812b-63f9cf408399 33 70.0\n801408de-c828-49b2-bdf4-da51fee5cc89 58 60.0\n"


if __name__ == '__main__':
    unittest.main()