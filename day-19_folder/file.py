# Read and Process a Text File

try:
    with open("practice.txt", "r") as o:

        line = 0
        word = 0
        character = 0

        for i in o:
            line += 1
            word += len(i.split())
            character += len(i)

        print("Number of lines:", line)
        print("Number of words:", word)
        print("Number of characters:", character)

except FileNotFoundError:
    print("File isn't found")