
#   This reads and prints the whole document.
#           It does not prt a blank line after each line of the file

name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

line_counter = 0

line = file_input.readline()
line = file_input.readline()



while line != '':                      # while not end of file
    line_counter += 1
    print(line_counter , line, end = '')              # don't print another new line
    line = file_input.readline()

file_input.close()
