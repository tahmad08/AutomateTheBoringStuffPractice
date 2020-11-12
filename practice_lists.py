import random

def commacode(og):
    sentence = ''
    for i in range(len(og)):
        if i != (len(og) - 1):
            sentence += str(og[i]) + ', '
        else:
            sentence += 'and ' + str(og[i])

    print(sentence)
    
def coin_flip():
    numberOfStreaks = 0
    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        listo = []
        for i in range(100):
            hort = random.randint(0,1)
            listo.append(hort)
        # Code that checks if there is a streak of 6 heads or tails in a row.
        numberOfStreaks = 0
        for i in range(len(listo) - 5):
            if ((listo[i] == listo[i+1]) and (listo[i] == listo[i+2])
            and (listo[i] == listo[i+3]) and (listo[i] == listo[i+4])
            and (listo[i] == listo[i+5])):
                numberOfStreaks += 1
                i+=5           
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def char_pic():
    for row in range(len(grid)):
        sent = ''
        for col in range(len(grid[row])):
            sent+=(grid[row][col])
        print(sent)
    print('\n')


def bdays():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break

        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')
bdays()
