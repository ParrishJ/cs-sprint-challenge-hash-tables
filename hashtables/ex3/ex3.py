""" UNDERSTAND
We will look through a list of lists and find which numbers occur on each list

PLAN 

we will initiate a dictionary as well as a num_lists value to find the length of our nested list list
We'll then loop through every integer in all the lists and add unique integers to the dictionary as well as
keep track of how man occurances there are of each integer. Lastly, we'll sort our dictionary and will push the integers
that have occured as many times equal to the num_lists variable to form our final answer """


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    integer_dictionary = {}
    result = []
    num_lists = len(arrays)

    # Enter integers into dictionary
    for int_list in arrays:
        for list_int in int_list:
            if list_int in integer_dictionary:
                integer_dictionary[list_int] += 1
            else:
                integer_dictionary[list_int] = 1

    #Order dictionary
    sorted_integer_dictionary_list = sorted(integer_dictionary.items(), key=lambda x: x[1], reverse=True)

    #Append final items to answer list
    for item in sorted_integer_dictionary_list:
        if item[1] == num_lists:
            result.append(item[0])
        else:
            break

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

