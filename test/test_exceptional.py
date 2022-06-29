import unittest
from count_occurrences import count_word
from calculator import calculator
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_type_error_at_count_word(self):
        test_obj = TestUtils()
        try:
            count_word("sentence")
            test_obj.yakshaAssert("TestTypeErrorAtCountWord", False, "exception")
            print("TestTypeErrorAtCountWord = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorAtCountWord", True, "exception")
            print("TestTypeErrorAtCountWord = Passed")

    def test_type_error_at_calculator(self):
        test_obj = TestUtils()
        try:
            calculator(1,'3',5)
            test_obj.yakshaAssert("TestTypeErrorAtCalculator", False, "exception")
            print("TestTypeErrorAtCalculator = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorAtCalculator", True, "exception")
            print("TestTypeErrorAtCalculator = Passed")
