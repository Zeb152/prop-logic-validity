#Started halfway through class on February 21, 2024.
#GOAL: determine the validity of any logical propositional arguments

#invalid if premises are true and conclusion is false

#
#& = and
#| = or
#>> = conditional
#=== = biconditional
#~ = negation

#cool API function:
#sympy.logic.boolalg.POSform(variables, minterms, dontcares=None) -- truth values into symbolization

from sympy import *
from sympy.logic.boolalg import truth_table

import numpy as np
import pandas as pd


finishedVars = False

variables = []
masterList = []
rowList = []
alphabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

currentSelected = 0
testingSelected = 0

valid = True

print("\n ==== LOGICAL PROPOSITION VALIDITY CHECKER ==== \n")


#GET VARIABLESSS
numberVars = input('(Number) Amount of variables in the argument: ')

for i in range(int(numberVars)):
    symbolizedIn = input("(letter) Enter your variables - ONE AT A TIME: ").lower()
    if symbolizedIn == 'end':
        break
    variables.append(symbolizedIn)
    print(variables)
    
numberOfVars = len(variables)


#GET PREMISESSS

premStr = input('(Number) Amount of premises in argument (not including conclusion): ')
premiseNumber = int(premStr)

#SYMBOLIZE PREMISES
varsAuto = [Symbol(name) for name in variables]

premList = []
finishedPrems = False

print('\n KEY: \n & - and \n | - or \n >> - conditional \n === - biconditional \n ~ - negation \n')

for i in range(premiseNumber):
    prem = input("Premise " + str(i + 1) + ": ")
    if "===" in prem:
        x, y = prem.split("===")
        x = x.strip()  # remove leading and trailing whitespaces
        y = y.strip()  # remove leading and trailing whitespaces
        splitX = x.split()
        splitY = y.split()
        print(splitX)
        print(splitY)
        for i in splitX:
            if i in alphabetList:
                lowercase_letters = i
        print(lowercase_letters)
        for i in lowercase_letters:
            if i in x:
                newVarX = x.split(i)
        print(newVarX)
        new_statement = f"Equivalent({x}, {y})"
        print(new_statement)
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

conclusion = input('Conclusion: ')
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
        
        #change any values that came out as 0 or 1 to a bool true or false
        boolRowList = []
        for item in rowList:
            booledItem = bool(item)
            boolRowList.append(booledItem)
        
        #ADD LIST TO MASTER
        masterList.append(boolRowList)
        currentSelected = currentSelected + 1
        if currentSelected == maxList:
            break
        

#get the max number a LIST can interpret of all the rows IN a premise
listNumRows = num_rows - 1

#DEBUG PRINT STATEMENTS
print('\n FULL LIST: ' + str(masterList) + '\n')
print('- TABLE ----------------')
#lets convert masterList to numpy array as np.array
df = pd.DataFrame(masterList, index=[premList])
transLst = df.transpose()
print(transLst)

#Find the conclusion by going to the final item in the master list
masterNum= len(masterList)
masterConcNum = masterNum - 1

#this is one item behind the conclusion so it is therefore the max number of premises to search
premiseNumberForList = masterNum - 2


#CHECK FOR VALIDITY

#if the validityInt/the number of premises is, for example, 3/3, the row is valid
validityInt = 0

#whether to break the validity check for loop
breakValidityCheck = False

#loop for every row there is
for i in range(num_rows):
    print('\n')
    print('ROW ' + str(testingSelected + 1))

    #if the first premise is true then we can determine validity with the other premises - there will always be ONE premise or more
    if bool(masterList[0][testingSelected]) == True:
        validityInt = validityInt + 1

        #skip right to the conclusion if there is just one premise
        if premiseNumber == 1:
            #test to see if the conclusion is true because first premise is true
            if bool(masterList[masterConcNum][testingSelected]) == True:
                    print('this whole row is TRUE and VALID')
                    print('TESTING SELECTED: ' + str(testingSelected) + '\n LIST NUMBER ROWS: ' + str(listNumRows))

                    #because this is just one premise the whole argmuent is true
                    if testingSelected >= listNumRows:
                        valid = True
                        breakValidityCheck = True
            #test to see if the conclusion is false because first premise is true
            elif bool(masterList[masterConcNum][testingSelected]) != True:
                print('these PREMISES are TRUE but the conclusion is FALSE')
                valid = False
                breakValidityCheck = True
        #break the check before it checks for more because it is just 1 premise and 1 conclusion

        #for MORE THAN 1 PREMISE
        #note: the range() function for 'for' loops is as follows for the integers inside: (inclusive, exclusive) - hence the reason +1 is added to the premiseNumberForList var
        for i in range(1, premiseNumberForList + 1):

            #check to see if the first premise is true
            if bool(masterList[i][testingSelected]) == True:
                print('BEING TESTED: premise ' + str(i + 1) + ' row ' + str(testingSelected))
                print(str(i + 1) + ' premise IS true')
                #the validity int is added in order to have a control and make sure that ALL values in one row of premises have been tested. 
                #cont. it makes sure it doesn't "jump to conclusions" (pun intended) before testing all premises' values.
                validityInt = validityInt + 1
                print('VALIDITY INT: ' + str(validityInt) + '/' + str(premiseNumber))

                #if all the premises are valid
                if validityInt >= premiseNumber:
                    #reset validity number (in order to test another row)
                    validityInt = 0
                    print('validity reset')
                    print('all premises are VALID here!')

                    #check to see if conclusion is true because we know the premises are all true
                    #premises true, conclusion false = valid
                    if bool(masterList[masterConcNum][testingSelected]) == True:
                        print('this whole row is TRUE and VALID')
                        if testingSelected >= listNumRows:
                            valid = True
                            breakValidityCheck = True
                    #premises true, conclusion false = invalid
                    elif bool(masterList[masterConcNum][testingSelected]) != True:
                        print('CAUTION: these PREMISES are TRUE but the conclusion is FALSE')
                        valid = False
                        breakValidityCheck = True

            #if one of the premises are not true, just continue because there is no way to prove validity through that row
            elif bool(masterList[i][testingSelected]) != True:
                print('BEING TESTED: premise ' + str(i + 1) + ' row ' + str(testingSelected))
                print(str(i + 1) + ' premise is not true, moving on')
                validityInt = 0
                print('RESET VALIDITY')
                continue

            #if we had gotten an invalid conclusion earlier, this would end the 'for' loop
            if breakValidityCheck == True:
                break

        #reset validity if not already done so
        validityInt = 0
        #move to the next row
        testingSelected = testingSelected + 1

    #if the first premise is not true just move on because we cant check for validity
    elif bool(masterList[0][testingSelected]) != True:
        print('[First premise is not True so can\'t check for validity in row ' + str(testingSelected) + ']')
        testingSelected = testingSelected + 1

    #if we had gotten an invalid conclusion earlier, this would end the 'for' loop
    if breakValidityCheck == True:
        break



#PRINT VALIDITY
if valid == True:
    print('\n')
    print("~ARGUMENT VALID~")
else:
    print('\n')
    print("~ARGUMENT INVALID~")
