#shoe size trick
from datetime import datetime

def shoe_trick():
    print("we'll use your shoe size to tell your age\n" 
          + "what is your shoe size?")
    sz = input()
    while not(sz):
        print("enter a value for your shoe size: ")
        sz = input()
    rsz = sz
    if (str(rsz))[-2:] == ".5":
        rsz = float(rsz) + 0.5
        print("we round up your shoe size to " + str(rsz))
        
    print("first we multiply by five: " + str(rsz) + " * 5 = " + str((float(rsz)*5)) + ". ok?")
    sz = float(rsz) * 5
    ok = input()
    print(" add 50: 50 + "+ str(sz) + " = " + str(((sz)+50)))
    sz = sz + 50
    ok = input()
    print("  multiply by 20: 20 * " + str(sz) + " = " + str(sz*20))
    sz = sz * 20
    ok = input()
    year = datetime.now().year
    print("    then take the current year and subtract 1000, add")
    print("     "+str(year) + " - 1000 = " + str(year-1000) + " + " + str(sz) + " = " + str((sz + (year-1000))))

    birth = ''
    while birth == '':
        print("      almost done. next we subtract your birth year.")
        print("        Please enter your birthdate in mm-dd-yyyy format: ")
        birth = input()
        
    curr_month = datetime.now().month
    bmonth = birth[:2]
    bday = birth[3:5]
    byear = birth[-4:]
    bdate = datetime(datetime.now().year,int(bmonth),int(bday))
    rsz = (sz + (year-1000)) - int(byear)
    print("         "+str(sz) + " - " + str(byear) + " = " + str(rsz))
    sz = str(int(rsz))
    shoe = sz[:-2]
    if(bdate > datetime.now()):
        age = int(sz[-2:]) - 1
    else:
        age = int(sz[-2:])
    print(" SHOE SIZE = " + str(shoe)+ " AND AGE: " + str(age))

#shoe_trick()

def hello(name):
    #return "hello " + name
    return name


