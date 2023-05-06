# Demo of passing by reference in python by returning multiple values from a function
def greetingGenerator(name, ctr):
    ctr += 1
    return f"Hi, {name}", ctr

def main():
    counter = 0
    print(f"Original Counter value: {counter}")
    greeting1, counter = greetingGenerator("Alice", counter)
    print(f"{greeting1}\nIncremented Counter Value: {counter}")
    greeting1, counter = greetingGenerator("Bob", counter)
    print(f"{greeting1}\nIncremented Counter Value: {counter}")

main()

# Demo of returning multiple values from a function used in a condition
def tryIntegerParse(string, intBase = 10):
    try:
        return True, int(string, base=intBase)
    except:
        return False, None
    
isIntParsed, resultInt = tryIntegerParse("123")
print(f"{isIntParsed}, {resultInt}")

def tryIntegerParse2(string, intBase = 10):
    try:
        return int(string, base=intBase)
    except ValueError:
        return None

numberStr = input("Enter a string to be converted to a number:\n")

if (n := tryIntegerParse2(numberStr)) is not None:
    print(f"The parsed integer: {n}")
else:
    print(f"The integer conversion did not work for \"{numberStr}\"")

print(f"Multiplication: 10 * tryIntegerParse2('100')= {10 * tryIntegerParse2('100')}")
print(f"Multiplication: 10 * tryIntegerParse2('DAE', intBase=16)= {10 * tryIntegerParse2('DAE', intBase=16)}")

print(10 * (n if (n := tryIntegerParse2("3634534")) is not None else 1))
print(10 * (n if (n := tryIntegerParse2("777", intBase=8)) is not None else 1))
print(10 * (n if (n := tryIntegerParse2("sfdsfs")) is not None else 1999))