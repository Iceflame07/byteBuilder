import unittest
import getpassword

class Test(unittest.TestCase):

    def test_that_getpassword_function_exist(self):
	    getpassword("")

    def test_that_digits_has_minimum_length_function(self):
	    self.assertEqual(getpassword("@Sem&iCh90%B57A$"))

    def test_that_digits_has_lowercase_function(self):
	    self.assertEqual(getpassword("@Sem&iCh90%B57A$"))

    def test_that_digits_has_uppercase_function(self):
	    self.assertEqual(getpassword("@Sem&iCh90%B57A$"))

    def test_that_digits_has_symbols_function(self):
	    self.assertEqual(getpassword("@Sem&iCh90%B57A$"))

    def test_that_digits_are_sixteen_function(self):
	    self.assertEqual(getpassword("@Sem&iCh90%B57A$"))

    def test_that_digits_are_present_function(self):
	    self.assertEqual(getpassword("@Sem&iCh90%B57A$"))