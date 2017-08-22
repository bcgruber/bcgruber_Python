'''
OBJECTTIVES:

Must:
X 01. Include a function that takes at least two user arguments from the command line
X 02. Contain at least one if/else statement
X 03. Perform a caclulation on a list
X 04. Use at least one dictionary
X 05. Have one try/except clause for every function
X 06. Output something (write) to a file, using string formatting
X 07. Must include docstrings telling us how to run your script.

Options:
X 08. Either create a class to contain the related functions OR output a simple graph

To Turn in:
Upload your final python script or jupyter notebook to Github, turn in the link on Canvas


OPERATION:
This script is designed to represent tracking transactions to a bank account.  The script requires a user to log in,
select which of their accounts they would like to access, and enter the transactions to be tracked.  Once this is done,
the transactions are aggregated with the initial balance of the account and a summary receipt is generated.  A graph is
then launched which displays a line graph of the which reads the receipts and plots the values of the specified account.

'''
import sys
import datetime
import os.path
import matplotlib.pyplot as plt




#Setting up the test case
checkingBeginningBalance = float(10.35)
savingsBeginningBalance = float(100.60)
inputMoneyVals = []
exitCode = ""

#04. Use at least one dictionary
bankAccountDict = {'checking': checkingBeginningBalance , 'savings': savingsBeginningBalance}
userAccountDict = {'brian123':'mybadpassword','tmpuser1':'temppass1','tmpuser2':'tmppass2'}





#01. Include a function that takes at least two user arguments from the command line
#############################
# LOGIN TO USER ACCOUNT FUNCTION
#############################
def login(username,password):
    for key, value in userAccountDict.items():
        # 02. Contain at least one if / else statement
        if username == key:
            if password == value:
                loginOutput = 1
                return loginOutput
        else:
            return print ("incorrect username and or password")




#############################
# RETRIEVE BANK ACCOUNT FUNCTION
#############################

def getAccount(accountName):
    if whichAccount in bankAccountDict.keys():
        getAccountOutput = 1
        return getAccountOutput





#############################
# LOGIN TO USER ACCOUNT
#############################
loginCounter = 0
while loginCounter <= 3:

    un = input("Enter your username: ").lower()
    passw = input("Enter your password: ").lower()
    results = login(un,passw)

    if results == 1:
        print("Hello,",un," You are now logged in.\n")
        break

    if loginCounter >= 3:
        print("Too many login attempts")
        sys.exit()

    loginCounter += 1





#############################
# RETRIEVE BANK ACCOUNT
#############################

accountCounter = 0
while accountCounter <=3:
    whichAccount = input("Which account are you tracking: ").lower()
    getAccountResults = getAccount(whichAccount)

    # 02. Contain at least one if / else statement
    if getAccountResults == 1:
        print("We are tracking your",whichAccount,"account\n")
        break
    else:
        accountCounter += 1
        print("That account does not exist")
        if accountCounter >=3:
            print("You need help. Exiting")
            sys.exit()



#Loopception
#Capture all the transaction to aggregate with the initial balance.
while exitCode != "no":
    try:
        #reset the exit code
        exitCode = ""
        moneyValue = float(input("Enter Amount: "))
        inputMoneyVals.append(moneyValue)
        while exitCode != "yes":
            #Accept only lowercase yes/no from user
            exitCode = input("Are there are other transactions? (yes or no)").lower().replace(" ","")
            if exitCode == "no":
                break
    except ValueError:
        # Display error message when input is not numeric
        print("Numbers pls.")




##################
# SUMMARY STYLE RECEIPT
###################

#03. Perform a caclulation on a list
for z in inputMoneyVals:
    bankAccountDict[whichAccount] += z

#Builds the paths necessary to read and write receipts
path = 'C:/temp/Receipts'
fileName = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
filePath = "C:/temp/receipts/"+fileName+".txt"

#print(filePath)
#06. Output something (write) to a file, using string formatting
with open(filePath, "w+") as outfile:
    outfile.write("YOUR RECEIPT:\n" )
    outfile.write("______________\n\n")


#06. Output something (write) to a file, using string formatting
for key,val in bankAccountDict.items():
    numOutput = "{0:.2f}".format(round(float(val),2))
    fullOutput = str(key) + " " + str(numOutput) + "\n\n"
    with open(filePath, "a") as outfile:
        outfile.write(fullOutput)
        outfile.close()


counter = 0
receiptCounter = []
receiptValue = []


for dirpath, dnames, fnames in os.walk(path):
    for f in fnames:
        fullPath = path + "/" + f
        counter += 1
        receiptCounter.append(counter)
        with open(fullPath,"r") as rd:
            content = rd.readlines()
            for intVal in content:
                if intVal.startswith(whichAccount):
                    intVal = intVal.replace(whichAccount + " ","")
                    intVal = intVal.replace(" ","")
                    intVal = intVal.replace('\n',"")
                    receiptValue.append(float(intVal))
                    rd.close()


plt.plot(receiptValue,"b-")
plt.ylabel(receiptCounter)
plt.show()

print("Tracking Complete")