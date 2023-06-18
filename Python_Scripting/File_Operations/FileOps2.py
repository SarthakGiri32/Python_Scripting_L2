while True:
    # reading partial file
    with open("test2.txt") as frHandle:
        numBytes = int(input(f"Enter the number of bytes you want to read from {frHandle.name}:\n"))
        readPartialContent = frHandle.read(numBytes)
        print(f"Reading {numBytes} bytes from file \"{frHandle.name}\":\n{readPartialContent}")
    if input("Enter No to stop:\n") == "No":
        break
