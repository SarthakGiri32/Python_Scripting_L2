total = 0  # This is global variable.


# Function definition is here
def summation(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2  # Here total is local variable.
    print("Inside the function local total :", total)
    print(f"Memory address of total (local): {id(total)}")
    return total


# Now you can call sum function
summation(10, 20)
print("Outside the function global total :", total)
print(f"Memory address of total (global): {id(total)}")
