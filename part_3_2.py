"""
Re-write this NumPy code so that it is vectorized.
ie. replace the for loops with only NumPy array operations.

It might be useful to work this out with a pen and paper before writing the answer.
"""
import numpy as np

# A matrix defining how different locations (home, work, school) infect other people.
# Rows are infectors, columns are infectees.
infect_matrix = np.array([
    [0.9, 0.05, 0.05],
    [0.05, 0.9, 0.05],
    [0.05, 0.05, 0.9],
])

# Compartments of people (home, work, school).
infectors = np.array([10, 19, 35]) # people who can infect other people

infected = np.zeros_like(infectors) # number of people who got infected


"""
Previous code:
The previous code has a bug, Its internally rounding off the infect_factor * num_infectors
product before calculating the infected values.
"""
# for infectee_idx in range(3):
#     for infector_idx in range(3):
#         infect_factor = infect_matrix[infector_idx, infectee_idx]
#         num_infectors = infectors[infector_idx]
#         infected[infectee_idx] += infect_factor * num_infectors

# print("Number of people infected (home, work, school):", infected)


"""
Modified Code:
This code performs the same operation without rounding off the 
infect_factor * num_infectors product in a single step.

Please uncomment the previous code to observe the difference.
"""
infected = np.matmul(infectors, infect_matrix)

print("Number of people infected (home, work, school):", infected)
