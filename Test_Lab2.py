import Lab2

print("Test Lab2")

def test_find_min_max():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test = (90, 11)

    result = Lab2.find_min_max(input_arr)

    assert (result == test)
    print("returned: " + str(result))

def test_calc_average():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_result = 36.86

    result = Lab2.calc_average(input_arr)

    assert (result == test_result)
    print("returned: " + str(result))

def test_calc_median_temperature():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_result = 12

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == test_result)
    print("returned: " + str(result))

