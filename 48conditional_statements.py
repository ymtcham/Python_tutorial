name = input("Enter name: ")
age = int(input("What's your age, {}? \n".format(name)))

if 18 <= age <= 31:
    print('Welcome aboard, {}'.format(name))

else:
    print('Sorry, try somewhere else')