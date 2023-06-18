# opening a file
with open("Python_Scripting\\File_Operations\\test2.txt", "rb") as fHandle:
    fileContentString = str(fHandle.read(13))[2:-1]
    fName = fHandle.name[fHandle.name.index('test'):]
    print(f"Reading 13 bytes from the \"{fName}\" file:\n{fileContentString}")

    # check current position of file read pointer
    fReadCurrentPosition = fHandle.tell()
    print(f"Current position of read in file \"{fName}\": {fReadCurrentPosition}")

    # set current position to byte 25 from byte 13 of file content
    fNewPosition = fHandle.seek(25, 1)
    print(f"Reser position of read in file \"{fName}\": {fNewPosition}")
    fileNewContentString = str(fHandle.read(20))[2:-1]
    print(f"Reading 20 bytes from the \"{fName}\" file from {fNewPosition}:\n{fileNewContentString}")

with open("Python_Scripting\\File_Operations\\test2.txt", "r") as fHandle2:
    # set current position to byte 38 from byte 0 of file content
    fNewPosition = fHandle2.seek(38, 0)
    fName = fHandle2.name[fHandle2.name.index('test'):]
    print(f"Reser position of read in file \"{fName}\": {fNewPosition}")
    fileNewContentString = fHandle2.read(20)
    print(f"Reading 20 bytes from the \"{fName}\" file from {fNewPosition}:\n{fileNewContentString}")