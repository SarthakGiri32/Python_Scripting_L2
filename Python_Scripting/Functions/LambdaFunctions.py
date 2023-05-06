import math

#Syntax of Lamda Expressions: lambda [arg1 [,arg2,.....argn]]:expression
addition = lambda n1, n2: n1 + n2

print(f"4564 + 354 = {addition(4564, 354)}")

loopMultiplication = lambda n1, *numbers: n1 + numbers[len(numbers) - 2]

print(loopMultiplication(12312, 566564, 5656, 76777))
print(loopMultiplication(12312, 566564, 5656, 76777, 456465, 21121233))

# applying lambda function to an argument
print((lambda x: x + 34542)(24332))
print((lambda x, y: x + y)(24332, 67655))

# Lambda with multiple arguments
bodmasExpression = lambda n1, n2, n3, n4: (n1 // n2) * n1 - n3 + (n4 % n2) // n1 + n2 * 3
print(bodmasExpression(34, 31, 20, 19))

# higher order lambda functions
higherOrderLambda = lambda x, func: x * func(x)
print(higherOrderLambda(243/545, math.sin))
print(higherOrderLambda(564354, lambda x: x * 4533))