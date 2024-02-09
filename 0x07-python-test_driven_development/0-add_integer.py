#!/usr/bin/python3
def add_integer(a, b=98):
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Return the addition of a and b
    return a + b

