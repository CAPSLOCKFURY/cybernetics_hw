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

    def test_DatesNotEqualValidator_validates_dates(self):
        validator = DatesNotEqualValidator()
        date1 = datetime.strptime("08-11-2022", "%d-%m-%Y")
        date2 = datetime.strptime("11-11-2022", "%d-%m-%Y")
        res = validator.validate(date1, date2)
        self.assertTrue(res)

    def test_DatesNotEqualValidator_rejects_equal_dates(self):
        validator = DatesNotEqualValidator()
        date1 = datetime.strptime("08-11-2022", "%d-%m-%Y")
        date2 = datetime.strptime("08-11-2022", "%d-%m-%Y")
        res = validator.validate(date1, date2)
        self.assertFalse(res)

    def test_DateGTETodayValidator_validates_dates(self):
        validator = DateGTETodayValidator()
        date = datetime.strptime("08-11-2111", "%d-%m-%Y")
        res = validator.validate(date)
        self.assertTrue(res)

    def test_DateGTETodayValidator_validates_today_date(self):
        validator = DateGTETodayValidator()
        date = datetime.today()
        res = validator.validate(date)
        self.assertTrue(res)

    def test_DateGTETodayValidator_rejects_date_that_less_than_today(self):
        validator = DateGTETodayValidator()
        date = datetime.strptime("08-11-1999", "%d-%m-%Y")
        res = validator.validate(date)
        self.assertFalse(res)

    def test_Date1BeforeDate2Validator_validates_two_dates(self):
        validator = Date1BeforeDate2Validator()
        date1 = datetime.strptime("08-11-2022", "%d-%m-%Y")
        date2 = datetime.strptime("11-11-2022", "%d-%m-%Y")
        res = validator.validate(date1, date2)
        self.assertTrue(res)

    def test_Date1BeforeDate2Validator_rejects_given_date1_after_date_2(self):
        validator = Date1BeforeDate2Validator()
        date1 = datetime.strptime("11-11-2022", "%d-%m-%Y")
        date2 = datetime.strptime("08-11-2022", "%d-%m-%Y")
        res = validator.validate(date1, date2)
        self.assertFalse(res)

    def test_Date1BeforeDate2Validator_rejects_given_same_dates(self):
        validator = Date1BeforeDate2Validator()
        date1 = datetime.strptime("11-11-2022", "%d-%m-%Y")
        res = validator.validate(date1, date1)
        self.assertFalse(res)
