import math
print('This is a calculator app. \nIt lets you do basic arithmitic operations.')
menChoice = ''

def mainMenu():
    global menChoice
    menChoice = input('\nEnter the type of operation you want to do by entering the number next to one of the four options below or enter q to quit: \n1.Add \n2.Subtract \n3.Multiply \n4.Divide \n')
    print('')    
    if menChoice == '1':
        Add()
    elif menChoice == '2':
        Sub()
    elif menChoice == '3':
        Mult()
    elif menChoice == '4':
        Div()
    elif menChoice == 'q':
        quit()
    
def Add():
    num1=()
    num2=()
    print('You have selected 1.Addition')
    
    if menChoice == '1':
        num1 = input('\n1.Enter the first number:')
        num2 = input('2.Enter the second number:')
        addResult = int(num1) + int(num2)
        print('\nThe result is', addResult)
 
def Sub():
    num1=()
    num2=()
    print('You have selected 2.Subtraction')
    
    if menChoice == '2':
        num1 = input('\n1.Enter the first number:')
        num2 = input('2.Enter the second number:')
        addResult = int(num1) - int(num2)
        print('\nThe result is', addResult)

def Mult():
    num1=()
    num2=()
    print('You have selecred 3.Multiplication.')

    if menChoice == '3':
        num1 = input('\n1.Enter the fist number:')
        num2 = input('2.Enter the second number:')
        addResult = int(num1) * int(num2)
        print('\nThe result is:', addResult)

def Div():
    num1=()
    num2=()
    print('You have selecred 4.Division.')

    if menChoice == '4':
        num1 = input('\n1.Enter the first number:')
        num2 = input('2.Enter the second number:')
        addResult = float(num1) / float(num2)
        print('\nThe result is:', addResult)

while menChoice != 'q':
    menChoice = mainMenu()
