"""
Using pandas:
    - load the CSV file specified by CSV_FILE
    - using the data in the file, create a plot where 
        - the x axis is time (ascending)
        - the y axis is the number of daily infections (per age group)
    - save the plot to the file "part_2_3.png"

You don't need to get fancy with labelling plot axes or adding titles or anything like that.
If you cannot figure out how to do all of this, then plot something else.
"""


"""
Running Instructions:
Open a terminal and run the following command;

python part_2_3.py

to execute this file
"""

import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "data/report_2_3.csv"

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

# Seperating time and number of daily infections arrays based on age groups
time_array_sep = []
daily_infections_array_sep = []
for i in range(len_age_group):
    temp_time_array = []
    temp_infections_array = []
    for j in range(len(data["time"])):
        if age_groups[i] == data["age"][j]:
            temp_time_array.append(data["time"][j])
            temp_infections_array.append(data["daily_infections"][j])
    time_array_sep.append(temp_time_array)
    daily_infections_array_sep.append(temp_infections_array)

# plotting based on age groups
legend_array = []
for i in range(len_age_group):
    plt.plot(time_array_sep[i], daily_infections_array_sep[i])
    legend_array.append("age group: "+str(age_groups[i]))

plt.xlabel('time')
plt.ylabel('number of daily infections')
plt.title('daily infections v/s time')
plt.legend(legend_array)

# Saving the plot
plt.savefig('part_2_3.png', dpi=300, bbox_inches='tight')