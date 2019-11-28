import func1
import func2
import func3
run = True
def menu():
    while run:
        print("What would you like to do?")
        print("1: Convert an image to grayscale, 2: Generate a bit-depth graph of a png image, 3: Add contrast to an image, 4: Exit the program ")
        userinput = int(input("Choose an option: "))
        if userinput == 1:
            oneinp = str(input("Enter the filename to convert to grayscale"))
            oneinp2 = str(input("Enter name of the new grayscale file"))
            func1.togrey(oneinp, oneinp2)
        if userinput == 2:
            twoinp = str(input("Enter filename to be read (MUST BE A .PNG FILE!): "))
            twoinp2 = str(input("Enter name of graph generated:"))
            func2.lum(twoinp, twoinp2)
        if userinput == 3:
            threeinp = str(input("Enter filename to add contrast to: "))
            func3.enhance(threeinp)
        if userinput == 4:
            exit(0)
menu()
