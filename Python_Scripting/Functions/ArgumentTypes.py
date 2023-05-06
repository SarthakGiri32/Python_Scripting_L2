#Keyword arguments
def printinfo(name, age):
   "This prints a passed info into this function"
   print(f"Name: {name}")
   print(f"Age: {int(age)}")

printinfo(age="55", name="Dumbledore")

#Default arguments
def printinfo2(name, age = "117"):
   "This prints a passed info into this function"
   print(f"Name: {name}")
   print(f"Age: {int(age)}")

printinfo2(age="55", name="Nigel")
printinfo2("Sarthak")
printinfo2(age = "24", name= "Sarthak Giri")

#Variable-length Arguments
def multipleNumbersMultiplication(n = 17655, *numbers):
   multiply = n
   i = 1
   print(f"Number {i}= {n}")
   for num in numbers:
      i += 1
      print(f"Number {i}= {num}")
      multiply *= num
   
   print(f"Multiplication result= {multiply}")

multipleNumbersMultiplication()
multipleNumbersMultiplication(2453, 4354, 876, 112, 987987)
multipleNumbersMultiplication(4, 7, 1, 9, 11, 23)

