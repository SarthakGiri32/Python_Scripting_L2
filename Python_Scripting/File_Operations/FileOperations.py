# opening and reading from a file, then closing the file
try:
    file1 = open("Python_Scripting\\File_Operations\\test.txt")
    readContent = file1.read()
    print(f"Reading contents from \"test.txt\":\n{readContent}")
finally:
    file1.close()

with open("Python_Scripting\\File_Operations\\test.txt", "r") as fHandle:
    readCon = fHandle.read()
    print(f"Reading contents from \"test.txt\":\n{readCon}")

# writing to a file
with open("Python_Scripting\\File_Operations\\test2.txt", "w") as fwHandle:

    # write contents to the test2.txt file
    fwHandle.write("Progamming is fun, especially with file operations.")
    fwHandle.write("\nLets see how far we can go today.")

