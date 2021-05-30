print ("Hello Python world!")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = (f"\tHello, {full_name.title()}!") #\t for tab. \n for new line in a string
print(message)
favorite_language = "python     "
favorite_language.rstrip() #strips extra whitespace on right end of string (single use). save to variable for permanent change. .lstrip(), .strip()
namer = "sara"
sara_is_a_butt = (f"{namer}, you are a butt.") #f-string
print(sara_is_a_butt)
print(namer.lower(), namer.upper(), namer.title())  #name case
#math syntax: =, -, *, /, **, % (_ used to make numbers easy to read without printing the underscores)
x, y, z = 0, 0, 0   #initializing more than one variable at a time
CONSTANT = 0        #use all caps to indicate var should remain unchanged

#lists
list_bikes = ['trek', 'cannondale', 'redline', 'huffy']
print(list_bikes[0]) #[0] indicates index 0
print(list_bikes[0].title()) #[0] indicates index first item on list
print(list_bikes[-1].title()) #[-1] indicates index last item on list
print(f"My first bicycle was a {list_bikes[-1].title()}.")
list_letters = ["a", "b", "c", "d", "e", "f"]
print(f"The first letter is: {list_letters[0].upper()}")
list_letters[0] = "AAAAAAAAAAAA"
print(list_letters[0])
list_letters.append("gold")
list_letters.insert(0, "First")
print(list_letters)
del list_letters[1]
pop_letter = list_letters.pop(-2)
print(pop_letter)
print(list_letters)
list_letters.remove("First")
print(list_letters)
expensive = "gold"
list_letters.remove(expensive)
master_mess = [list_letters, list_bikes, pop_letter, sara_is_a_butt]
print(list_letters)
list_letters.sort(reverse=True)  #sorts list in reverse order
print(list_letters)
print(sorted(list_letters)) #sorts list and prints it without changing the list
list_letters.reverse() #reverses order of list
len(list_letters) #counts the indices in the list
print(len("word")) #prints characters in a string, starts counting at 1
numbers = list(range(1, 101)) #this creates a whole new list (in given range) and assigns it to a variable
#list.sort(reverse=True) print(sorted(list, reverse=True))
print(numbers)

#for loops
magicians = ['alice', 'damascus', 'herecles', 'yo mamma']
for magician in magicians:
    print(magician)
squares = [value**2 for value in range(1,11)] #LIST COMPREHENSION: using the for loop INSIDE of the list creation and assigning it to a variable
print(squares)
for value in range(1, 21):
    print(value)
million_nums = []
for value in range(1, 1000001):
    million_nums.append(value)
print(magicians[0:3]) #prints index 0-2 (non-inclusive stop point 3)
print(magicians[-3:])  #starts at index -3 (third from the end, inclusive) and prints to end of the list
for magician in magicians[-3:]: #loops through the slice
    print(magician.title())
acolytes = magicians[:] #copies all index of list into new list 
dimensions = (200, 50) #TUPLE. Immutable list. The list can be redefined, but not modified.
'alice' in magicians # this line returns TRUE using IN to check for a value inside a list
user = "sara"
if user not in magicians: #NOT and IN checking a list for an object not in the list returning TRUE
    print(f"User {user.title()} is not a magician")
if magicians:        #format checks for empty list, if not empty, executes indented shit ('for statement')
    print("List has magicians!")
else:
    print("List is empty.")
toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
toppings_order = ['mushrooms', 'cat', 'extra cheese']
for topping_order in toppings_order:
    if topping_order in toppings:
        print(f"Adding {topping_order}")
    else:
        print(f"Sorry, we don't have {topping_order}.")

#dictionaries
alien_0 = {'color' : 'green', 'points' : 5}  #creating dictionary
print (alien_0['color']) #calling a value based on the key
print(alien_0['points'])
alien_0['gun'] = "doom cannon"  #adding a key value pair to a dictionary, or redefining a key value pair
del alien_0['gun']  #deleting a key value pair from a dictionary
point_value = alien_0.get('points', "No point value assigned.") #.get attempts to pull 'key', if unavailable, returns "default"
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
favorite_languages = {
    'jen' : 'python',
    'sarah' : "c",
    'edward' : "ruby",
    'phil' : "python"
}
for name, language in favorite_languages.items(): #assigns key to name, and value to language (.items pulls both, .keys pulls just the key, .values pulls just the value)
    print(f"{name.title()}'s favorite language is {language.title()}.")
friends = ['phil',  'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
language_set = {'python', 'c', 'ruby', 'python'} # this set will eliminate repeated items in the set, use set() to do the same in a list or dictionary
