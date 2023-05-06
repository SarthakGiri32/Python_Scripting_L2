def printStatement(str):
    "This function prints the values passed as a string"
    print(str)
    return

printStatement("Testing functions in python")
printStatement("Starting my journey in PythonScriptingL2")

''' 
Demonstrating the original list value changing after appending another list to the original list inside a function, both inside and
outside the function
'''
def changeListValues(origList):
    "This function demonstrates passing by reference"
    origList.append([1, 2, 765, 91])
    print("List values inside the change function:", origList)

originalList = [124, 456, 9861]
print("List values before calling change function", originalList)
changeListValues(originalList)
print("List values outside the change function", originalList)

''' 
Demonstrating the original list value not changing after changing the value of the list passed inside the function
'''
def changeListValues2(origList):
    "This function demonstrates passing by value"
    origList = [1, 2, 765, 91]
    print("List values inside the change function:", origList)

originalList = [124, 456, 9861]
print("List values before calling change function", originalList)
changeListValues2(originalList)
print("List values outside the change function", originalList)

