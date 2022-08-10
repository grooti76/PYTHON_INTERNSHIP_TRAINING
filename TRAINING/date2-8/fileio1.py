def readFile(x):
    try:
        y = open(x, "r")
        print(y.read())
    except FileNotFoundError:
        print("File not Found")


def writeFile(x):
    y = open(x, "w")
    print(y.write(input()))


readFile("file1.txt")
readFile("file2.txt")
readFile("file3.txt")
writeFile("file1.txt")
writeFile("file2.txt")
writeFile("file3.txt")
# myFile = open("file1.txt", "r")
# myFile2 = open("file2.txt", "r")
# myFile3 = open("file3.txt", "r")
# text = myFile.read()
# text2 = myFile2.read()
# text3 = myFile3.read()
# print(text)
# print(text2)
# print(text3)
# myFile.close()
# myFile2.close()
# myFile3.close()
