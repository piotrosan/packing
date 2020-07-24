import unittest

from packing import packing_order
from packing import check_integer_amount
from packing import check_mod_amount
from packing import check_up_to_ten
from packing import do_if_big


class TryPacking(unittest.TestCase):

    def test_packing_order_100(self):
        result = packing_order(100)
        assert result["big_box"] == 11
        assert result["medium_box"] == 0
        assert result["small_box"] == 1

    def test_packing_order_10(self):
        result = packing_order(10)
        assert result["big_box"] == 1
        assert result["medium_box"] == 0
        assert result["small_box"] == 1

    def test_packing_order_22(self):
        result = packing_order(22)
        assert result["big_box"] == 2
        assert result["medium_box"] == 1
        assert result["small_box"] == 0

    def test_check_integer_amount_22(self):
        result = check_integer_amount(22)
        assert result == 2

    def test_check_integer_amount_100(self):
        result = check_integer_amount(100)
        assert result == 11

    def test_check_mod_amount(self):
        result = check_mod_amount(22)
        assert result == 4

    def test_check_up_to_ten_2(self):
        big, medium, small = check_up_to_ten(2)
        assert big == 0
        assert medium == 0
        assert small == 1

    def test_check_up_to_ten_4(self):
        big, medium, small = check_up_to_ten(4)
        assert big == 0
        assert medium == 1
        assert small == 0

    def test_check_up_to_ten_9(self):
        big, medium, small = check_up_to_ten(9)
        assert big == 1
        assert medium == 0
        assert small == 0

    def do_if_big(self):
        result = do_if_big(3, 11)
        assert result["big_box"] == 11
        assert result["medium_box"] == 0
        assert result["small_box"] == 1


if __name__ == '__main__':
    unittest.main()
