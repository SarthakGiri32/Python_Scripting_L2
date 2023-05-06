import math

#Syntax of Lamda Expressions: lambda [arg1 [,arg2,.....argn]]:expression

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
print(higherOrderLambda(564354, lambda x: x // 4533))

print((lambda x: (x % 2 and 'odd' or 'even'))(234))
print((lambda x: (x % 2 and 'odd' or 'even'))(4564219))

# Argument types in lambda
print((lambda x, y, z=342342: x / y * z)(131232, 98786))
print((lambda x, y, z=243121: x / y * z)(y=232, x=11231))
print((lambda *numbers: sum(numbers))(23432, 987876, 65461, 684774))
print((lambda **numbers: sum(numbers.values()))(n1 = 234242, n2 = 651146, n3 = 5346867, n4 = 56487, n5 = 5646867, n6 = 357744))


