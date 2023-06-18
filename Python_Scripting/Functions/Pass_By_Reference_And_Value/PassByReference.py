# demo of "passing by value" in Python, but python actually Passes by assignment
def square(n):
    n *= n


def main_function():
    num = 7667
    square(num)
    print(num)


main_function()


# explaining the above demo by using id() on a different demo. id() displays the memory address of a variable passed
# to it
def main():
    n = 98927864
    print(f"Initial address of n: {id(n)}")
    print("Initial value of n:", n)
    increment(n)
    print(f"Final address of n: {id(n)}")
    print("Final value of n:", n)


def increment(m):
    print(f"Initial address of m: {id(m)}")
    print("Initial value of m:", m)
    m += 1
    print(f"Final address of m: {id(m)}")
    print("Final value of m:", m)


main()
