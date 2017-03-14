# -*- coding: utf-8 -*-
# import argument variable from the sys module
from sys import argv

# assign the scriptname and first parameter to variables using argv
script, filename = argv
# open the file specified in the previous line and store into txt
txt = open(filename)

# print a little message to user
print(f"Here's your file {filename}:")
# print the contents of the txt file by using the .read() command with no inputs
print(txt.read())
# close the opened text file as is best practice
txt.close()
# # print a small message to the user again
# print("Type the filename again:")
# # get input from the user using the input command with the "> " arguments
# file_again = input("> ")

# # open the file specified using the previous input command and store into txt_again
# txt_again = open(file_again)
# # print out the contents of the file using .read() command of the txt_again variable with no arguments
# print(txt_again.read())
# # close the opened text file as is best practice
# txt_again.close()