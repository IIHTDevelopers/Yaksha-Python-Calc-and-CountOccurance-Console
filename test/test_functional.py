import unittest
from count_occurrences import count_word
from calculator import calculator
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_count_word(self):
        test_obj = TestUtils()
        result=count_word("Python is easy. Python developed by Guido","Python")
        if result==2:
            test_obj.yakshaAssert("TestCountWord", True, "functional")
            print("TestCountWord = Passed")
        else:
            test_obj.yakshaAssert("TestCountWord", False, "functional")
            print("TestCountWord = Failed")

    def test_count_nonaval_word(self):
        test_obj = TestUtils()
        result=count_word("Python is easy. Python developed by Guido","Java")
        if result==0:
            test_obj.yakshaAssert("TestCountNonavalWord", True, "functional")
            print("TestCountNonavalWord = Passed")
        else:
            test_obj.yakshaAssert("TestCountNonavalWord", False, "functional")
            print("TestCountNonavalWord = Failed")

    def test_calculator_add(self):
        test_obj = TestUtils()
        result=calculator(1,5,3)
        if result==8:
            test_obj.yakshaAssert("TestCalculatorAdd", True, "functional")
            print("TestCalculatorAdd = Passed")
        else:
            test_obj.yakshaAssert("TestCalculatorAdd", False, "functional")
            print("TestCalculatorAdd = Failed")

    def test_calculator_sub(self):
        test_obj = TestUtils()
        result=calculator(2,5,3)
        if result==2:
            test_obj.yakshaAssert("TestCalculatorSub", True, "functional")
            print("TestCalculatorSub = Passed")
        else:
            test_obj.yakshaAssert("TestCalculatorSub", False, "functional")
            print("TestCalculatorSub = Failed")

    def test_calculator_mul(self):
        test_obj = TestUtils()
        result=calculator(3,5,3)
        if result==15:
            test_obj.yakshaAssert("TestCalculatorMul", True, "functional")
            print("TestCalculatorMul = Passed")
        else:
            test_obj.yakshaAssert("TestCalculatorMul", False, "functional")
            print("TestCalculatorMul = Failed")

    def test_calculator_div(self):
        test_obj = TestUtils()
        result=calculator(4,5,3)
        if result==1.6666666666666667:
            test_obj.yakshaAssert("TestCalculatorDiv", True, "functional")
            print("TestCalculatorDiv = Passed")
        else:
            test_obj.yakshaAssert("TestCalculatorDiv", False, "functional")
            print("TestCalculatorDiv = Failed")

    def test_calculator_floor_div(self):
        test_obj = TestUtils()
        result=calculator(5,5,3)
        if result==1:
            test_obj.yakshaAssert("TestCalculatorFloorDiv", True, "functional")
            print("TestCalculatorFloorDiv = Passed")
        else:
            test_obj.yakshaAssert("TestCalculatorFloorDiv", False, "functional")
            print("TestCalculatorFloorDiv = Failed")

    def test_calculator_pow(self):
        test_obj = TestUtils()
        result=calculator(6,2,3)
        if result==8:
            test_obj.yakshaAssert("TestCalculatorPow", True, "functional")
            print("TestCalculatorPow = Passed")
        else:
            test_obj.yakshaAssert("TestCalculatorPow", False, "functional")
            print("TestCalculatorPow = Failed")
