def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    integer_dictionary = {}
    result = []
    num_lists = len(arrays)
    for int_list in arrays:
        
        for list_int in int_list:
            if list_int in integer_dictionary:
                integer_dictionary[list_int] += 1
            else:
                integer_dictionary[list_int] = 1

    
    sorted_integer_dictionary_list = sorted(integer_dictionary.items(), key=lambda x: x[1], reverse=True)

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

