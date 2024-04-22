
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    inputs = input()
    listinputs = inputs.split(", ")
    listinputs = [float(x) for x in listinputs]

    return listinputs

          
def calc_average(list):
    total = sum(list)
    average = total/len(list)

    return average


def calc_min_max(list):

    min_temp = min(list)
    max_temp = max(list)

    return min_temp, max_temp


def sort_temperature(sorted):
    
    return sorted


def calc_median_temperature(sorted):
    
    return median



def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    
    average = calc_average(num_list)
    print("Average= " + str(average))

    min, max = calc_min_max(num_list)
    print("Minimum= " + str(min) + "  Maximum= "+ str(max)) 


if __name__ == "__main__":
    main()