def swapFileData():
    fileName1 = input("This is text from file1")

    fileName2 = input("This is text from file2")

    with open(fileName1, 'r') as a:
        data_a = a.read()

    with open(fileName2, 'r') as a:
        data_b = a.read()

    with open(fileName1, 'w') as a:
        a.write(data_b)

    with open(fileName2, 'w') as a:
        a.write(data_a)
    
    
    



swapFileData()