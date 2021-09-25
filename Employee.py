def repeat():

    userInput = int(input("Press 1 to continue press 0 to exit"))

    return userInput

def monDay():

    global month, day

    month = int(input("Enter in which month you worked: "))

    day = int(input("Enter how many days you worked: "))

def roll(rollSalary):

    print("Salary of employee without overtime is: ", rollSalary*day)

    overTime = int(input("Enter Over time days: "))

    ovTimeSalary = ((rollSalary*50)/100)*overTime

    totalSalary = ovTimeSalary+(rollSalary*day)

    print("Overtime salary of employee is: ", ovTimeSalary)

    print("Total salary of employee with overtime is: ", totalSalary)



manager = 2000

tLeader = 1800

tManager = 1500

loop = True



name= input("Enter your name: ")

print("We have 3 designation 1)Manager 2)Team Leader 3)Team Manager choose any one")

desig = input("Enter your designation: ")

designation = desig.upper()





monDay()



if month==2 and day<=29:

    if designation=="MANAGER":

        roll(manager)

    

    elif designation == "TEAM lEADER":

        roll(tLeader)

    elif designation == "TEAM MANAGER":

        roll(tManager)

    else:

        print("You entered wrong designation please try again!")

elif month%2==0 and day<=30 and month<=6 and month!=2:

    if designation=="MANAGER":

        roll(manager)

    

    elif designation == "TEAM lEADER":

        roll(tLeader)

    elif designation == "TEAM MANAGER":

        roll(tManager)

    else:

        print("You entered wrong designation please try again!")



elif month%2==0 and day<=31 and month>=8 and month<=12 and month!=2:

    if designation=="MANAGER":

        roll(manager)

    

    elif designation == "TEAM lEADER":

        roll(tLeader)

    elif designation == "TEAM MANAGER":

        roll(tManager)

    else:

        print("You entered wrong designation please try again!")

elif month%2==1 and day<=31 and month<=7 and month!=2:

    if designation=="MANAGER":

        roll(manager)

    

    elif designation == "TEAM lEADER":

        roll(tLeader)

    elif designation == "TEAM MANAGER":

        roll(tManager)

    else:

        print("You entered wrong designation please try again!")



elif month%2==1 and day<=30 and month>=9 and month<=12 and month!=2:

    if designation=="MANAGER":

        roll(manager)

    

    elif designation == "TEAM lEADER":

        roll(tLeader)

    elif designation == "TEAM MANAGER":

        roll(tManager)

    else:

        print("You entered wrong designation please try again!")

else:

    print("You entered wrong days Or month please try again!")

    monDay()
