with open("test2.txt") as fileHandle:
    fLine = fileHandle.readline(38)
    print(f"fLine: {fLine}")

    fReset = fileHandle.seek(0, 0)
    i = 1
    for line in fileHandle.readlines():
        print(f"line {i}: {line.strip()}")
        i += 1

    fReset = fileHandle.seek(0, 0)
    lines2 = [line2.strip() for line2 in fileHandle]
    print(f"List of lines in file: {lines2}")
