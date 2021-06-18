in_username = input("Please enter your name...\n")
in_password = int(input("Please enter your PIN code, {} \n".format(in_username)))
password=1234
if in_password == password:
    print('Welcome,{}'.format(in_username))
else:
    print('Sorry, wrong PIN code!')
    print(" Try again; but this time add {} to the value you entered previously".format(1234-in_password))

# x=7
# y=5
# if x > y:
#     print('x is greater tha y')
# elif y > x:
#     print('y is greater than x')
# else:
#     print('x is equal to y')