import os

with open("testFile2.txt", "w") as fHandle:
    fHandle.write("New file to be deleted")

with open("testFile2.txt") as fHandle2:
    print(f"File data:\n{fHandle2.read()}")

os.remove("testFile2.txt")

print(f"Current Working Directory: {os.getcwd()}")