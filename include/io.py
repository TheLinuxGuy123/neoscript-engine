import sys

def NewFunction(funcname, implementation_func):
    """
    Dynamically creates a new named function that accepts arguments and 
    injects it directly into the caller's main script workspace on the fly.
    """
    # 1. Grab the global environment workspace of the file calling this (e.g., test.geo)
    caller_globals = sys._getframe(1).f_globals
    
    # 2. Build a dynamic wrapper that carries over any arguments (*args) and returns values
    def dynamic_func(*args, **kwargs):
        # Executes the custom logic code block and forwards what it calculates back
        return implementation_func(*args, **kwargs)
    
    # 3. Permanently bind and inject your custom function name into the user's file space
    caller_globals[funcname] = dynamic_func






"""
Just 134





"""







def getUserInput(input1):
    return input(input1)