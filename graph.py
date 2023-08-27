import matplotlib.pyplot as plt
import numpy as np
import warnings

# Function that will draw a linear graph of the expresion in the form y=mx + c provided by the parameter "equation"
def draw_graph(equation):

    # Ignoring UserWarning
    warnings.filterwarnings("ignore", category=UserWarning)
    
    # Axis range
    # Generating a list of sequential number from 0 to 9 for the range of the axis
    x = np.arange(0, 10)
    y = np.arange(0, 10)

    # Seperating each element of the equation
    # And adding then to a list
    element_list = []
    for element in equation:
        element_list.append(element)

    # Checking if the first element of the list is x, that is the coefficient of x is 1
    if element_list[0] == "x":
        # Setting the value of m to 1
        m = 1
    else:
        # If the first element is not x, then it is a number
        # Setting the number to m
        # The coefficient of x will be represented by that number
        m = int(element_list[0])

    # Checking if the last element is not an x
    if element_list[-1] != "x":
        # If it is not, take the last 2 element of the list (sign and magnitude) and assigning it to c
        c = int("".join(element_list[-2:]))
    else:
        # Else x is the last element, c is assigned to 0
        c = 0

    # Calculating the value of y = mx + c with the range of values of x, m and c to get the new values of y
    y = m * x + c

    # Plot coordinates (x,y) on graph of y = mx +c
    plt.plot(x, y, color='red', linestyle='solid')

    # Add a title
    plt.title(f"Graph of {str(equation)}")

    # Add X and Y Label
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    # Show grid on the graph scale
    plt.grid()
    # Showing the graph
    plt.show()