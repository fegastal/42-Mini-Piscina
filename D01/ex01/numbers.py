#!/usr/bin/python3

def open_file():
    #Accessing a text file numbers.txt
    #Opens a file in read only mode

    with open("numbers.txt","r") as file:

        #Let's split the line into an array called "fields" using the "," as a separator:
        numbers = file.read()
        fields = numbers.split(",")

        #Repeat for each elements in the field
        for elements in fields:
            print(elements)

if __name__ == '__main__':
    open_file()