# renaming a file
import os

with open("testFileOps.txt", "w") as fHandle:
    lines = ["Python is great.\n", "Lets fucking go!!!"]
    fHandle.writelines(lines)

os.rename("testFileOps.txt", "testFileOperations.txt")
