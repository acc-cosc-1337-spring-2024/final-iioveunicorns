#add import
import question_a

menu = 1
while menu > 0:
    print('Enter 5 numbers.')
    print('')
    userNumber1 = input('First Number: ')
    print('')
    userNumber2 = input('Second Number: ')
    print('')
    userNumber3 = input('Third Number: ')
    print('')
    userNumber4 = input('Fourth Number: ')
    print('')
    userNumber5 = input('Fifth Number: ')
    menu = 2
    while menu == 2:
        userList = question_a.listMaker(userNumber1, userNumber2, userNumber3, userNumber4, userNumber5)
        question_a.displayList(userList)
        print('Enter to Exit.')
        quitCheck = input(' ')
        menu = 0
        