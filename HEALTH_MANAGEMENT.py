''' HEALTH MANAGEMENT SYSTEM '''
# get date time
def getdate():
    '''through this function you will get the date and time'''
    import datetime
    return datetime.datetime.now()

# loading function
def loading():
    import time
    for i in range(0,7):
        print(".", end="")
        time.sleep(1)
    return print("loading over")

# FUNCTION TO REGISTER YOURSELF
def register(a):
    '''This function will register you'''
    for i in range(a):
        name_people = input("Enter your name\n")
        o = open("list of people.txt", 'a')
        o.write(str(i+1) + " " + " " + "=" + " " + " " + name_people + " " + " " + " " + str(getdate()) + '\n')
        o.close()
        file_formation(name_people)

# FUNCTION TO CHECK YOU ARE REGISTER OR NOT IF NOT YOU WILL BE REGISTER
def register_check():
    '''This function will register you if you are not registered '''
    k = int(input("Press 1 if you are registered and Press 2 if you are not registered\n"))
    if k == 2:
        a = int(input("Enter no of people you want to manage health\n"))
        register(a)
    elif k == 1:
        print("you are registered")
        name = input("Enter your name\n")
        c = open('list of people.txt', 'r')
        check = c.read()
        c.close()

        if name in check:
            print('yes you are register')
        else:
            print('you are not register please register yourself')
            a = int(input("Enter no of people you want to manage health\n"))
            register(a)
    else:
        print("Press 1 or 2 ")

# using this you will create file
def file_formation(name):
    '''you can create file through this function'''
    f = open(name + "F.txt", "a")
    f.close()

    f = open(name + "E.txt", "a")
    f.close()

# log file function
def file_log_F(name):
    '''you can log food through this function'''
    p = open(name + "F.txt", "w")
    k = input("write the food you eaten\n")
    k1 = p.write(str(getdate()) + " " + " " + " " + k)
    p.close()

def file_log_E(name):
    '''you can log exercise through this function'''
    p = open(name + "E.txt", "w")
    k = input("write the exercise you done\n")
    k1 = p.write(str(getdate()) + " " + " " + " " + k)
    p.close()

# read file function
def file_read_F(name):
    '''you can read food you have eaten'''
    p = open(name + "F.txt", "r")
    k = p.read()
    p.close()

def file_read_E(name):
    '''you can read exercise you have done'''
    p = open(name + "E.txt", "r")
    k = p.read()
    p.close()
