# Create a file and write your name in it

# file = open("exploring.txt","a")
# file.write("Santosh")
# file.close()


# file = open("exploring.txt","r")
# print(file.read())
# file.close()

# with -- best practice

with open("exploring.txt","a") as file:
    file.write("Santosh\n")

with open("exploring.txt","r") as file:
    print(file.read() )