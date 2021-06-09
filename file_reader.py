filename = 'text_files/pi_million_digits.txt'

### reads whole file and prints it

#with open(filename) as file_object:
#    contents = file_object.read()
#print(contents.rstrip())

### opens file, reads the whole thing and stores it in the variable *lines*

with open(filename) as file_object:
    lines = file_object.readlines()

### for each line in the file, it prints the line and removes the whitespace at the end

#for line in lines:
#        print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")