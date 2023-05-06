#Syntax of Lamda Expressions: lambda [arg1 [,arg2,.....argn]]:expression
addition = lambda n1, n2: n1 + n2

print(f"4564 + 354 = {addition(4564, 354)}")

loopMultiplication = lambda n1, *numbers: n1 + numbers[len(numbers) - 2]

print(loopMultiplication(12312, 566564, 5656, 76777))
print(loopMultiplication(12312, 566564, 5656, 76777, 456465, 21121233))
