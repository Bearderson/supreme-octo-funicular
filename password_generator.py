import random  #BecAuSE We NEED RandOMnESs In oUR PaSsWOrDs

#initializing variables 
uppernum = 1    #number of upper case characters required for the password
lowernum = 1   #number of lower case characters required for the password
numbernum = 1   #number of numbers required for the password
character = 1   #number of special characters required
minimumamount = 8   #minimum number of characters in the finished password
maximumamount = 14   #maximum number of characters in the finished password

#above character requirements could be changed to be input by user 
#(using above default values if user declines input or inputs non-number values or values outside of range)
#if user input becomes a thing: (minimum < sum(all mandatory characters) < max). will have to user proof all inputs.

lowerset = "abcdefghijklmnopqrstuvwxyz"    #initializing character sets used for each individual requirement
upperset = lowerset.upper()
numberset = "0123456789"
characterset = "!@#$%^&*"
monty = lowerset + upperset + numberset + characterset #this will create a big string of all characters to pull leftovers from

#leftovers will be used to randomly generate extra characters to create a full password. "filler characters"
#reducing the range of characters by the amount of mandatory characters
leftovers = random.randint((minimumamount - character - numbernum - lowernum - uppernum), (maximumamount - character - numbernum - lowernum - uppernum))

def character_picker(cycles, the_set):
    """cycles = (uppernum, lowernum, etc.) the_set = (lowerset, upperset, etc.)"""
    picker = ""
    while cycles != 0:
        randominrange = random.randint(0, len(the_set)-1)
        picker += the_set[randominrange]
        cycles -= 1
    return picker
    
password = character_picker(lowernum, lowerset)
password += character_picker(uppernum, upperset)
password += character_picker(numbernum, numberset)
password += character_picker(character, characterset)
password += character_picker(leftovers, monty)

def scrambler(password):
    """Takes a random index of the password string and moves it to another random index."""
    scramble_cycles = 0
    while scramble_cycles != 1000:    #Sets the amount of times characters will be moved
        scramble_cycles += 1
        randomstart = random.randint(0, len(password)-1)   #picks which character (index) will be removed
        randomend = random.randint(0, len(password)-1)    #picks index that the character will be inserted at
        letter = password[randomstart]      #saves characted being moved
        password = password[:randomstart] + password[randomstart+1:]    #removes picked letter from password
        password = password[:randomend] + letter + password[randomend:]    #inserts character at new index
    return password

password = scrambler(password)
print(f"Here is your password: {password}")