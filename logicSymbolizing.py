
#GOAL: determine the validity of any logical propositional arguments

#invalid if premises are true and conclusion is false

#
#& = and
#| = or
#>> = conditional
#=== = biconditional

#cool API function:
#sympy.logic.boolalg.POSform(variables, minterms, dontcares=None) -- truth values into symbolization

from sympy import *
from sympy.logic.boolalg import truth_table

finishedVars = False

variables = []
masterList = []
rowList = []

currentSelected = 0
testingSelected = 0

valid = False

#GET VARIABLESSS
numberVars = input('How many variables are there: ')

for i in range(int(numberVars)):
    symbolizedIn = input("enter variables (one at a time): ")
    if symbolizedIn == 'end':
        break
    variables.append(symbolizedIn)
    print(variables)
    
numberOfVars = len(variables)


#GET PREMISESSS

premStr = input('How many premises: ')
premiseNumber = int(premStr)

#SYMBOLIZE PREMISES
varsAuto = [Symbol(name) for name in variables]

premList = []
finishedPrems = False

print('KEY: & - and, | - or, >> - conditional, === - biconditional')

for i in range(premiseNumber):
    prem = input("Premise: ")
    if "===" in prem:
        x, y = prem.split("===")
        x = x.strip()  # remove leading and trailing whitespaces
        y = y.strip()  # remove leading and trailing whitespaces
        new_statement = f"Equivalent({x}, {y})"
        prem = prem.replace(prem, new_statement)
        print(prem)

   # if prem == 'end':
   #     break
    premLength = len(prem)
    if premLength == 1:
        prem = '~~' + prem
    sympyTrans = sympify(prem)

    premList.append(sympyTrans)


#SYMBOLIZE CONCLUSION

conclusion = input('conclusion: ')
if "===" in conclusion:
    x, y = conclusion.split("===")
    x = x.strip()  # remove leading and trailing whitespaces
    y = y.strip()  # remove leading and trailing whitespaces
    new_statement = f"Equivalent({x}, {y})"
    conclusion = conclusion.replace(conclusion, new_statement)
    print(conclusion)

concTrans = sympify(conclusion)
premList.append(concTrans)


#get the max number a LIST can interpret of all the premises
maxList = premiseNumber - 1


#CREATE A TRUTH TABLE

for i in range(premiseNumber):
    for word in premList:
        try:
            table = truth_table(premList[currentSelected], variables, False)
        except IndexError as e:
            break
        #TURN TABLE INTO LIST
        rowList = list(table)
        #GET LIST LENGTH TO GET NUMBER OF ROWS IN ONE PREMISE
        num_rows = len(rowList)
        #ADD LIST TO MASTER
        masterList.append(rowList)
        currentSelected = currentSelected + 1
        if currentSelected == maxList:
            break
        

#get the max number a LIST can interpret of all the rows IN a premise
listNumRows = num_rows - 1

#masterList.append(concTrans)
#print('added ' + str(concTrans) + ' to masterlist')


#DEBUG PRINT STATEMENTS
print('FULL LIST: ' + str(masterList))
print('NUMBER OF ROWS: ' + str(listNumRows))


#Find the conclusion by going to the final item in the master list?
masterNum= len(masterList)
masterConcNum = masterNum - 1

#this is one item behind the conclusion so it is therefore the max number of premises to search
premiseNumberForList = masterNum - 2

#GET THE CONCLUSION: masterList[masterConcNum]


#have to figure out a way to get the number of premises
#premiseNumber = # of premises

#CHECK FOR VALIDITY

for i in range(num_rows):

    if bool(masterList[0][testingSelected]) == True:

        for i in range(1, premiseNumberForList):

            if bool(masterList[i][testingSelected]) == True:
                print('BEING TESTED: ' + str(masterList[i][testingSelected]))
                print('its true')
            elif bool(masterList[i][testingSelected]) != True:
                print('BEING TESTED: ' + str(masterList[i][testingSelected]))
                print('its not')
    
    elif bool(masterList[0][testingSelected]) != True:
        print('first prem row being checked not true moving on')



#for every row there is in the truth table
for i in range(num_rows):

    #print the row number being checked at the moment
    print('ROW CHECK: ' + str(testingSelected))    

    #if the first PREMSE's row of the row being checked is true
    if bool(masterList[0][testingSelected]) == True:

        #if the first PREMISE's row of being checked is the same as the second PREMISE's row being checked (i.e. if they are both true)
        if bool(masterList[0][testingSelected]) == bool(masterList[1][testingSelected]):
            #check if the conclusion is true or false
            if bool(masterList[2][testingSelected]) != True:
                print('Invalid')
                testingSelected = testingSelected + 1
                valid = False
                #if an argument is T T :. F at any point then it is all invalid, so quit the for loop
                break
            if bool(masterList[2][testingSelected]) == True:
                print('Valid')
                testingSelected = testingSelected + 1
                #an argument could be valid someplace but invalid at another, so unless we are at the last row continue the for loop
                if testingSelected > listNumRows:
                    valid = True
                    break
        #elif the first PREMISE'S row being checked (which we know is true because of the previous if statement) != the second premise's row being checked's value, just move to the next row (T F)
        elif bool(masterList[0][testingSelected]) != bool(masterList[1][testingSelected]):
            print('Check')
            testingSelected = testingSelected + 1
            if testingSelected > listNumRows:
                break
            continue
    #if the first premise's row being checked is not true then we cannot determine validity so just check the next row
    elif bool(masterList[0][testingSelected]) != True:
        print('Check')
        testingSelected = testingSelected + 1
        if testingSelected > listNumRows:
            break
        continue

        

#PRINT VALIDITY
if valid == True:
    print("~ARGUMENT VALID~")
else:
    print("~ARGUMENT INVALID~")


