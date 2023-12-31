def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    i = input()
    splitinput = i.split(",")
    num_list = [float(item) for item in splitinput]
    return num_list


def find_min_max(l):
    maxtemp = max(l)
    mintemp = min(l)
    return maxtemp, mintemp


def sort_temperature(l):
    s = sorted(l)
    return s


def calc_average(l):
    average = sum(l)/len(l)
    return round(average, 2)


def calc_median_temperature(s):

    n = len(s)

    if n % 2 == 1:
        median = s[n // 2]
    else:
        middle1 = s[(n - 1) // 2]
        middle2 = s[n // 2]
        median = (middle1 + middle2) / 2

    return median



def main():
    display_main_menu()
    num_list = get_user_input()
    max_temp, min_temp = find_min_max(num_list)
    sort_ascending = sort_temperature(num_list)
    average = calc_average(num_list)
    median = calc_median_temperature(sort_ascending)
    print("Maximum Temp= " + str(max_temp))
    print("Minimum Temp= " + str(min_temp))
    print("Ascending Order= " + str(sort_ascending))
    print("Average= " + str(average))
    print("Median= " + str(median))

if __name__ == "__main":
    main()



