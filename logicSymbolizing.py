
#determine the validity

#invalid if premises are true and conclusion is false

#
#& = and
#| = or
#

#sympy.logic.boolalg.POSform(variables, minterms, dontcares=None) -- truth values into symbolization

from sympy import *
from sympy.logic.boolalg import truth_table

finishedVars = False

variables = []

numberVars = input('How many variables are there: ')

for i in range(int(numberVars)):
    symbolizedIn = input("enter variables (one at a time): ")
    if symbolizedIn == 'end':
        break
    variables.append(symbolizedIn)
    print(variables)
    
numberOfVars = len(variables)


premStr = input('How many premises: ')
premiseNumber = int(premStr)

#for i in range(numberOfVars):
#    for word in variables:
#        word = Symbol(word)

varsAuto = [Symbol(name) for name in variables]

premList = []
finishedPrems = False

print('KEY: & - and, | - or, >> - conditional, write Equivalent(a, b) for biconditional')

for i in range(premiseNumber):
    prem = input("Premise: ")
   # if prem == 'end':
   #     break
    premLength = len(prem)
    if premLength == 1:
        prem = '~~' + prem
    sympyTrans = sympify(prem)
    premList.append(sympyTrans)


masterList = []

conclusion = input('conclusion: ')

concTrans = sympify(conclusion)

premList.append(concTrans)

maxList = premiseNumber - 1

currentSelected = 0

rowList = []


for i in range(premiseNumber):
    for word in premList:
        #print('CURRENT SELECTED')
        try:
            table = truth_table(premList[currentSelected], variables, False)
        except IndexError as e:
            #print('QUIT LOOP: ' + str(e))
            break

        rowList = list(table)
        num_rows = len(rowList)

        masterList.append(rowList)
        
        #print(rowList)
        #print('ROW ' + str(currentSelected) + ' VALUE: ' + str(rowList[0]))
        #for t in table:
            #rint(str(premList[currentSelected]) + ':> ' '{0} -> {1}'.format(*t))
        currentSelected = currentSelected + 1
        if currentSelected == maxList:
            break
        

#table = truth_table(premList[0], variables)
        

        
#print(masterList)
#print('CONTECNS: ' + str(masterList[1]))

listNumRows = num_rows - 1

# Creating a list of lists
#list_of_lists = [
#    [1, 2, 3],
#    ['a', 'b', 'c'],
#    [True, False, True]
#]
#print(list_of_lists[0])  # Output: [1, 2, 3]
#print(list_of_lists[1][2])  # Output: c

masterList.append(concTrans)

print('FULL LIST: ' + str(masterList))

testingSelected = 0

print('NUMBER OF ROWS: ' + str(listNumRows))

valid = False

masterNum= len(masterList)
masterConcNum = masterNum - 1



for i in range(num_rows):
    print('ROW CHECK: ' + str(testingSelected))    
    if masterList[0][testingSelected] == True or masterList[0][testingSelected] == 1:
        if bool(masterList[0][testingSelected]) == bool(masterList[1][testingSelected]):
            if masterList[2][testingSelected] != True or masterList[2][testingSelected] == 0:
                print('Invalid')
                testingSelected = testingSelected + 1
                valid = False
                break
            if masterList[2][testingSelected] != True or masterList[2][testingSelected] == 0:
                print('Invalid')
                testingSelected = testingSelected + 1
                valid = False
                break
            if masterList[2][testingSelected] == True:
                print('Valid')
                testingSelected = testingSelected + 1
                if testingSelected > listNumRows:
                    valid = True
                    break
            elif masterList[2][testingSelected] == 1:
                print('Valid')
                testingSelected = testingSelected + 1
                if testingSelected > listNumRows:
                    valid = True
                    break
        if bool(masterList[0][testingSelected]) != bool(masterList[1][testingSelected]):
            print('Check')
            testingSelected = testingSelected + 1
            continue
    if masterList[0][testingSelected] != True:
        print('Check')
        testingSelected = testingSelected + 1
        continue
    elif masterList[0][testingSelected] == 0:
        print('Check')
        testingSelected = testingSelected + 1
        continue
        #if testingSelected > 2:
        #    break
        

print(premList)

if valid == True:
    print("~ARGUMENT VALID~")
else:
    print("~ARGUMENT INVALID~")

#for t in table:
#    print('{0} -> {1}'.format(*t))

