import sys
import os

# Get the parent directory of the Lab2 folder
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

import Lab2


def test_find_min_max():
    result = []
    input_arr = [3, 65, 6, 25, 9, 1]
    test_arr = (1, 65)
    
    result = Lab2.calc_min_max(input_arr)

    assert (result == test_arr)


def test_calc_average():
    result = []
    input_arr = [4, 66, 94, 3]
    test_value = 41.75

    result = Lab2.calc_average(input_arr)

    assert (result == test_value)


def test_calc_median_temperature():
    result = []
    input_arr = [55, 8, 44, 24, 2, 75]
    test_value = 34

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == test_value)