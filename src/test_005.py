#Import other files for complementing the testing
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from test_003 import AssertionsTest
from test_004 import SearchTests

#Creates an instance of the imported modules
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

#Defines a test suite
smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)