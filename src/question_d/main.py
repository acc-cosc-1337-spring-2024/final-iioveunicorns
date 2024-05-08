#add import
import question_d

menu = 1
table = question_d.create_multiplication_table()
while menu>0:
    question_d.display_multiplication_table(table)
    print('')
    select = input('Enter E or Exit to quit: ')
    print('')
    try:
        if select.upper()=='E' or select.upper()=='Exit':
            menu = 0
            quit()
    except ValueError:
        print('Invalid Selection')
