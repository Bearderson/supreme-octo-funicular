# A few things need addressing: 
# How much of the address is required? Do address components need to be kept separate?
# How are we separating multiple items in the order when adding to CSV doc? (Products in list would be nice.)
# Refactor into functions when we know what to do with data.

import re

filename = 'sampleOrder.xml'
name = ""
address = ""
products = ""
# Opens file, reads the whole thing and stores it in the variable *lines*, then closes file.

with open(filename) as file_object:
    lines = file_object.readlines()

# Find the name, address and productOrdered (Address is only street address at this point. Wasn't sure how much data to provide.)
# Below blocks can be refactored into functions when output and output format are more precise.

for line in lines:
    if '<Name>' in line:
        get_start = re.search(r'(<Name>)', line)
        get_start = get_start.end()
        get_end = re.search(r'(</Name>)', line)
        get_end = get_end.start()
        name = line[get_start:get_end]
        break

for line in lines:
    if '<Street>' in line:
        get_start = re.search(r'(<Street>)', line)
        get_start = get_start.end()
        get_end = re.search(r'(</Street>)', line)
        get_end = get_end.start()
        address = line[get_start:get_end]
        break

for line in lines:
    if '<ProductName>' in line:
        get_start = re.search(r'(<ProductName>)', line)
        get_start = get_start.end()
        get_end = re.search(r'(</ProductName>)', line)
        get_end = get_end.start()
        products += f".{line[get_start:get_end]}" #This adds a period in between ordered items, to make recall easier.
        

with open('orderlog.csv', 'w') as file_object:  #writes to a new file. Will always re-write over old file.
    file_object.write(f"{name},{address},{products}\n")