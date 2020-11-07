""" 
UNDERSTAND
Given a list of integers, we will find which positive integers have a negative counterpart.

PLAN
We'll initiate a dictionary, then looping through our list, we will use the absolute value
of the integer in our list to loop up a value in the dictionary. If that value exists and 
is the opposite (positive or negative) of the integer we are itterating through, we know that we 
have found a pair of integers that fit our criteria. We then push the positive of that integer to our answer list. 
If we try to retrieve the absolute value of the integer we are itterating over and it does not exist,
we push a key value pair to the dictionary where the key is the absoute value of the integer and the value is the integer itself. 

"""


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    positive_negative_dictionary = {}
    result = []
    
    # See if we can retrieve the absolute value of every integer in the list from our dictionary
    for integer in a:
        if positive_negative_dictionary.get(abs(integer)):
            # If it exists and is opposite (positive / negative) to the integer in the loop, we add the absolute value of that integer to our answer
            if positive_negative_dictionary.get(abs(integer)) > 0 and integer < 0 or positive_negative_dictionary.get(abs(integer)) < 0 and integer > 0:
                result.append(abs(integer))
        else:
            #otherwise we add the absolute val of the integer and the integer to our dictionary. 
            positive_negative_dictionary[abs(integer)] = integer

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))




