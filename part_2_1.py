"""
Fix up this code so that it is well formatted (eg. PEP 8 and similar good practices).
"""

"""
Running Instructions:
Open a terminal and run the following command;

python part_2_1.py

to execute this file
"""

import random


def print_average():
    """
    Prints the average of a random list 100 times
    """
    for i in range(100):

        values = [random.random() for item in range(20)]

        average = sum(values) / len(values);
        """
        Note: I had to change the print statement below a bit, as the 
        previous print statement is not compatible with ubuntu.
        """
        print( "The average of the random list is " + str(average))

if __name__ == "__main__":
    print_average()
    