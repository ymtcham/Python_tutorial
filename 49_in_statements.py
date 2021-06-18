q1 = input("Hi there, what's your name? \n")
print('-' * 100)
q2 = input("How are you today, {}?\n".format(q1))
print('-' * 100)
if ('well' or 'good' or 'ok' or 'fine' or 'alright' or 'cool' or 'great') and not 'not'  in q2:
    print('Glad to hear that, {}'.format(q1))
else:
    print("Sorry, to hear that. I wish there's something I can do to make you feel better")
print('-' * 100)
q3 = input('How can I be of help to you, {}? \n'.format(q1))
print('-' * 100)
print("Your wish is my command")