#tic-tac-toe game
import pprint

boardo = {'top-L':' ','top-M':' ','top-R':' ',
         'mid-L':' ','mid-M':' ','mid-R':' ',
         'low-L':' ','low-M':' ','low-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def play():
    turn='X'
    #there are 9 turns, so in range 9 for a full game
    for i in range(9):
        printBoard(boardo)
        print("it is the turn for " + turn + ".")
        pprint.pprint(boardo.keys())
        print("enter one of the positions to mark:")
        move = input()
        if(boardo[move] == ' '):
            boardo[move] = turn
        else:
            print('Position taken. Enter a different position')
            move = input()
            boardo[move] = turn
        if(turn == 'X'):
            turn = 'O'
        else:
            turn = 'X'
    printBoard(boardo)



# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    print(inventory.items())
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total+=v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    # your code goes here
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
