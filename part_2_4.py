"""
Using pandas:
    - load the CSV file specified by CSV_FILE
    - using the data in the file, create a plot where 
        - the x axis is time (ascending)
        - the y axis is the cumulative sum of daily infections for all people aged over 20
    - save the plot to the file "part_2_4.png"

An example of a "cumulative sum":
    input: [1, 2, 1, 1, 2, 3, 1, 1]
    cumulative sum: [1, 3, 4, 5, 7, 10, 11, 12]

You don't need to get fancy with labelling plot axes or adding titles or anything like that.
If you cannot figure out how to do all of this, then plot something else.
"""


"""
Running Instructions:
Open a terminal and run the following command;

python part_2_4.py

to execute this file
"""

import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "data/report_2_3.csv"  # Same CSV file as the last question

# Your code goes here

"""
Code
"""

# accessing data from csv file 
data = pd.read_csv(CSV_FILE) 

# identifying age groups
age_groups = []
for i in data["age"]:
    if i not in age_groups:
        age_groups.append(i)

len_age_group = len(age_groups)

"""
Seperating time array based on age groups along with the calculation of 
cummulative sum arrays for each age group.
"""
time_array_sep = []
daily_infections_array_sep = []
for i in range(len_age_group):
    temp_time_array = []
    temp_infections_array = []
    prevVal = 0
    for j in range(len(data["time"])):
        if age_groups[i] == data["age"][j]:
            temp_time_array.append(data["time"][j])
            if temp_infections_array != None:
                temp_infections_array.append(data["daily_infections"][j]+prevVal)
                prevVal = data["daily_infections"][j]+prevVal
            else:
                temp_infections_array.append(data["daily_infections"][j])
                prevVal = data["daily_infections"][j]
    time_array_sep.append(temp_time_array)
    daily_infections_array_sep.append(temp_infections_array)

# plotting based on age groups
legend_array = []
for i in range(len_age_group):
    if age_groups[i] > 20: # checking for people with age greater than 20
        plt.plot(time_array_sep[i], daily_infections_array_sep[i])
        legend_array.append("age group: "+str(age_groups[i]))

plt.xlabel('time')
plt.ylabel('cumulative sum of number of daily infections')
plt.title('cumulative sum of daily infections v/s time')
plt.legend(legend_array)

# Saving the plot
plt.savefig('part_2_4.png', dpi=300, bbox_inches='tight')