
password = ""  #this will be our end result
uppernum = 1   #initializing variables (number of upper case characters required for the password)
lowernum = 1   #number of lower case characters required for the password
numbernum = 1   #number of numbers required for the password
character = 1   #number of special characters required
minimumamount = 8   #minimum number of characters in the finished password
maximumamount = 14   #maximum number of characters in the finished password
#TRASH leftovers = maximumamount - minimumamount  #extra characters to make up password

lowerset = "abcdefghijklmnopqrstuvwxyz"    #initializing character sets used for each individual requirement
upperset = lowerset.upper()
numberset = "0123456789"
characterset = "!@#$%^&*"

amount = range()