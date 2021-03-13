"""
Write some code to print the SHA256 hash of the string "This is a string"
"""


"""
Running Instructions:
Open a terminal and run the following command;

python part_2_5.py

to execute this file
"""

from hashlib import sha256

s = "This is a string"

# Your code goes here
hash_value = sha256(s.encode('utf-8')).hexdigest()
print("SHA256 Hash of the string = " + str(hash_value))