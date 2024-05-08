#add import
import question_b

menu = 1
while menu >=1:
    print('1 - Display Stock Purchase History')
    print('2 = Quit')
    print('')
    select = input('')
    print('')
    if select:
        menu = 2
    while menu == 2:
        try:
            choice = int(select)
        except:
            print('Error: Please select option from menu.')
            print('')
            break
        if choice == 2:
            quit()
        elif choice == 1:
            question_b.stock_purchase_history()
        else:
            print('Error: Please select option from menu.')
            print('')
        menu = 1
        