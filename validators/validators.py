from abc import ABC, abstractmethod
import re


class AbstractValidator(ABC):

    @abstractmethod
    def validate(self, arg):
        pass


class StringLengthValidator(AbstractValidator):

    def __init__(self, max_len, less=True):
        self.max_len = max_len
        self.less = less

    def validate(self, arg: str):
        return len(arg) <= self.max_len if self.less else len(arg) >= self.max_len


class RegexValidator(AbstractValidator):

    def __init__(self, pattern):
        self.pattern = pattern

    def validate(self, arg: str):
        return re.fullmatch(self.pattern, arg) is not None


class MinNumberValidator(AbstractValidator):

    def __init__(self, min_num):
        self.min_num = min_num

    def validate(self, arg):
        return self.min_num < arg
