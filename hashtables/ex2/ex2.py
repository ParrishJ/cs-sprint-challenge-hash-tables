#  Hint:  You may not need all of these.  Remove the unused functions.

""" 
UNDERSTAND
Given an unordered list of plan "tickets", we are going to find the original order
of those plan tickets

PLAN
To achieve our goal, we will push the list of tickets to a dictionary and use their origin
as the key and their desination as their value. We'll then look up the first ticket by looking up
the entry where they key is "NONE", then successively push each destination to our answer by looking up
the previous entry on the results array 
"""


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    routeDict = {}
    route = []

    for ticket in tickets:
        if ticket not in routeDict:
            routeDict[ticket.source] = ticket.destination
    origin = routeDict["NONE"]
    
    #start with origin
    route.append(origin)

    # loop through remaining tickets, using last entry on route list to look up next destination on dictionary
    for i in range(length - 1):
        new_desination = routeDict[route[i]]
        route.append(new_desination)

    return route





