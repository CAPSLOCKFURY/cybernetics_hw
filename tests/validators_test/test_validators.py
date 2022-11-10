from validators.validators import *
import unittest


class TestValidators(unittest.TestCase):

    def test_StringLengthValidator_validates_string(self):
        validator = StringLengthValidator(50)
        res = validator.validate("1234567890")
        self.assertTrue(res)

    def test_StringLengthValidator_rejects_non_valid_string(self):
        validator = StringLengthValidator(2)
        res = validator.validate("123")
        self.assertFalse(res)

    def test_StringLength_validator_validates_string_length_more_than_given_number(self):
        validator = StringLengthValidator(2, less=False)
        res = validator.validate("123")
        self.assertTrue(res)

    def test_StringLength_validator_rejects_string_with_less_chars_than_in_validator(self):
        validator = StringLengthValidator(2, less=False)
        res = validator.validate("1")
        self.assertFalse(res)

    def test_RegexValidator_validates_string(self):
        validator = RegexValidator("Hello")
        res = validator.validate("Hello")
        self.assertTrue(res)

    def test_RegexValidator_rejects_invalid_string(self):
        validator = RegexValidator("Hello")
        res = validator.validate("Hel")
        self.assertFalse(res)

    def test_MinNumberValidator_validates_number(self):
        validator = MinNumberValidator(10)
        res = validator.validate(11)
        self.assertTrue(res)

    def test_MinNumberValidator_rejects_number_that_less_than_value(self):
        validator = MinNumberValidator(10)
        res = validator.validate(1)
        self.assertFalse(res)
