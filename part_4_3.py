"""
The function `get_noisy_values` is hard to test because the values keep changing
every time you re-run the test.

Re-write `test_get_noisy_values` so that we still test some of the functionality
of `get_noisy_values`, but avoid the issue of tests failing randomly.

There are several acceptable solutions to this problem.

It should be possible to run the test in this file using PyTest
eg.
    pytest part_4_3.py

"""
import numpy as np


def get_noisy_values():
    signal = np.array([1, 2, 3, 4, 5])
    noise = np.random.random(5)
    return signal + noise

def test_get_noisy_values():
    values = get_noisy_values()
    expected = np.array([1, 2, 3, 4, 5])
    # This will fail most of the time.
    
    """
    To verify if the get_noisy_values function is working, we need to
    check if the function's output differs from the expected values.
    
    To achieve this, we need to check if the deviation of the
    function output from expected value is greater than zero.
    
    The bellow assert statement can help do this. Hence proving that 
    the function works.
    """
    
    assert ((values-expected) > np.zeros_like(expected)).all()
