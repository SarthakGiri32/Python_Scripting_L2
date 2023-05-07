try:
    file1 = open("Python_Scripting\\File_Operations\\test.txt")
    readContent = file1.read()
    print(readContent)
finally:
    file1.close()

with open("Python_Scripting\\File_Operations\\test.txt", "r") as fHandle:
    readCon = fHandle.read()
    print(readCon)