filename = 'text_files/programming.txt'

with open(filename, 'a') as file_object:  #filename is variable set above, 'w' means we open file in *write* mode, 'r' read mode, 'a' append mode, 'r+' read and write mode
    file_object.write("I love programming.\n")
