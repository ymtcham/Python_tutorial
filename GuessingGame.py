answer = 5
print("Guess a single digit number")
inputValue = int(input())

if inputValue == answer:
    print("Well done, Bucko")
else:
    if inputValue > answer:
        inputValue = int(input('Guess lower \n'))
    #     if inputValue == answer:
    #         print("Well done, Bucko")
    #     else:
    #         print('Sorry, Bucko')
    # else:
    #     inputValue = int(input('Guess higher\n'))
    #     if inputValue == answer:
    #         print('Well done, Bucko')
    #     else:
    #         print('Sorry, Bucko')
    else:
        inputValue = int(input('Guess higher\n'))

    if inputValue == answer:
        print('Well done, Bucko!')
    else:
        print('Sorry,Bucko')