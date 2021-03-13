"""
This code calculates and prints a value called "sum_norm".

It takes a long time to run, approximately 10s or so.
It contains some inefficient calculations which can be improved.

Re-write the block inside the Timer so that it runs at least 10x faster, 
while producing the same result.

You can do this without importing any additional libraries.
"""
from timer import Timer

ITEMS = list(range(30000))

with Timer("Calculating sum of normalized items"):
    
    """
    Previous code
    """
    # norm_items = []
    # for i in ITEMS:
    #     max_item = max(ITEMS)
    #     norm_item = i / max_item
    #     norm_items.append(norm_item)
    #     sum_norm = sum(norm_items)
    
    """
    Note: I had to change the print statements in timer.py file a bit, as the previous
    print statements are not compatible with ubuntu.
    """
    
    """
    We could tackle this problem in two ways
    Method1: Improving the existing code by restructuring it.
    """
    norm_items = []
    max_item = max(ITEMS)
    for i in ITEMS:
        norm_item = i / max_item
        norm_items.append(norm_item)
    sum_norm = sum(norm_items)
    
    
    """
    Method 2: Rewriting the existing code into a single line as
    shown below
    Note: uncomment the line below to see it's performance
    """
    # sum_norm = sum(ITEMS)/max(ITEMS)

"""
Both the approches took close to zero seconds to execute.
"""

print("The sum of norm items is", sum_norm)
