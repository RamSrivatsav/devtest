"""
This code "normalises" two lists of numbers (POP and MASS).
That is: each element of the list is divided by the sum of the list.

This "normalisation" feature is duplicated twice in the code, and it is done in two different ways.

Refactor this code (by writing and re-using a function) so that this code is DRY (Don't Repeat Yourself).
"""


"""
Running Instructions:
Open a terminal and run the following command;

python part_2_2.py

to execute this file
"""


POP = [4e5, 4.2e5, 6e5, 12e5, 8e5, 3.1e5, 2e5, 1e5]
MASS = [14, 12.2, 4]


"""
Previous code, Commented
"""


# # Normalize population
# total_pop = 0
# for p in POP:
#     total_pop += p

# pop_normalised = []
# for p in POP:
#     fraction = p / total_pop
#     pop_normalised.append(fraction)


# # Normalize mass
# mass_normalised = [m / sum(MASS) for m in MASS]

# print(pop_normalised)
# print(mass_normalised)


"""
New Code
"""

# Normalizing function
def arrayNormaliser(ARRAY):
    return [a / sum(ARRAY) for a in ARRAY]

# Printing the normalized Population and Mass array
print(arrayNormaliser(POP))
print(arrayNormaliser(MASS))
