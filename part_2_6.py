"""
Write a short docstring for the function below,
so that other people reading this code can quickly understand what this function does.

You may also rename the functions if you can think of clearer names.
"""



"""
Step Function generator:

The Function below can be used to generate step and uniform distribution functions.

This function has wide range of applications, for example; signal filtering, signal
amplification, data sampling and data segmenting.

The inputs to this function are upper and lower bounds along with the amplitude.

Function parameters:
start_time - lower bound of the step function
end_time - upper bound of the step function
value - amplitude value of the step function

"""
def step_function_maker(start_time, end_time, value):
    def my_function(time):
        if start_time <= time <= end_time:
            y = value
        else:
            y = 0.0
        return y

    return my_function
