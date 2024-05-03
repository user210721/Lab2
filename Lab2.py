
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    inputs = input()
    listinputs = inputs.split(", ")
    listinputs = [float(x) for x in listinputs]

    return listinputs
4, 66, 94, 3
          
def calc_average(list):
    total = sum(list)
    average = total/len(list)

    return average


def calc_min_max(list):

    min_temp = min(list)
    max_temp = max(list)

    return min_temp, max_temp


def sort_temperature(list):
    sorted_list = sorted(list)
    return sorted_list


def calc_median_temperature(sortedinputs):
    n = len(sortedinputs)
    if n % 2 == 0:
        # If the number of elements is even, average the middle two numbers
        mid = n // 2
        median = (sortedinputs[mid - 1] + sortedinputs[mid]) / 2
    else:
        # If the number of elements is odd, take the middle number
        mid = n // 2
        median = sortedinputs[mid]

    return median




def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()

    #prompt user to input 
    num_list = get_user_input()

    #calculate average then display
    average = calc_average(num_list)
    print("Average= " + str(average))

    #find min and max then display both
    min, max = calc_min_max(num_list)
    print("Minimum= " + str(min) + "  Maximum= "+ str(max))

    #Sort list in ascending order
    sorted_list = sort_temperature(num_list)

    #Find median in sorted list
    median = calc_median_temperature(sorted_list)
    print("Median= " + str(median))


if __name__ == "__main__":
    main()