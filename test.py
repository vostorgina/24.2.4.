import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) != 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply(self):
        assert self.calc.multiply(self, 1, 3) == 3

    def test_multiply_zero(self):
        assert self.calc.multiply(self, 1, 0) == 0

    def test_multiply_zero_first(self):
        assert self.calc.multiply(self, 0, 1) == 0

    def test_subtraction_first_zero(self):
        assert self.calc.subtraction(self, 0, 1) == -1

    def test_subtraction_second_zero(self):
        assert self.calc.subtraction(self, -50, 0) == -50

    def test_adding_negative_numbers(self):
        assert self.calc.adding(self, -1, -5) == -6

    def test_adding_one_negative_number(self):
        assert self.calc.adding(self, 10, -1) == 9

    def teardown(self):
        print('teardown completed')