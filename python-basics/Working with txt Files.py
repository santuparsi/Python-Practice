# Working with txt Files

# Text files are a built-in python feature. No import modules required
# Text files have the .txt format.
# Use either open or with open to either write or read a text file
# Use one of four modes for txt files:
#     - "w" for writing
#     - "r" for reading
#     - "r+" for both reading and writing
#     - "a" for appending new written lines


path = "D:\\Programming\\Python\\Python Training\\"
f = open(path +  "test.txt", "w")           # Open the file with given mode
f.write(" This is a test file....")
f.close()                                   # Close the opened file (Compulsory close after work done)

f1 = open(path + "test.txt", "a")
f1.write("\n Hello World !!!")
f.close()

with open(path + "test.txt", "a") as g:    # with open doesn't require close method to close file, does it automatically
    g.write("\n Another Test made....")


f = open(path + "test.txt", "r")
print(f.read())
f.close()
