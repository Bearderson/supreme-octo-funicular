message = ''
topping_list = []
active = True
while message.lower() != 'quit':
    message = input("Tell me something, and I will repeat it back to you: \nEnter 'quit' to exit the program.")
    if message.lower() == 'quit':
            active = False
            print("Thank you for using Parrot.")
            
    else:
        topping_list.append(message)
        print(message)
for topping in topping_list:
    print(topping)