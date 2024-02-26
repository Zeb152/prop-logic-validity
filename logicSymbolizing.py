
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

valid = True

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


#CHECK FOR VALIDITY

#if the validityInt/the number of premises is, for example, 3/3, the row is valid
validityInt = 0

#whether to break the validity check for loop
breakValidityCheck = False

#loop for every row there is
for i in range(num_rows):
    print('\n')
    print('ROW ' + str(testingSelected))

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



#for every row there is in the truth table
#for i in range(num_rows):

    #print the row number being checked at the moment
 #   print('ROW CHECK: ' + str(testingSelected))    

    #if the first PREMSE's row of the row being checked is true
#    if bool(masterList[0][testingSelected]) == True:

        #if the first PREMISE's row of being checked is the same as the second PREMISE's row being checked (i.e. if they are both true)
 #       if bool(masterList[0][testingSelected]) == bool(masterList[1][testingSelected]):
            #check if the conclusion is true or false
 #           if bool(masterList[2][testingSelected]) != True:
 #               print('Invalid')
 #               testingSelected = testingSelected + 1
 #               valid = False
                #if an argument is T T :. F at any point then it is all invalid, so quit the for loop
 #               break
 #           if bool(masterList[2][testingSelected]) == True:
 #               print('Valid')
 #               testingSelected = testingSelected + 1
                #an argument could be valid someplace but invalid at another, so unless we are at the last row continue the for loop
 #               if testingSelected > listNumRows:
 #                   valid = True
 #                   break
        #elif the first PREMISE'S row being checked (which we know is true because of the previous if statement) != the second premise's row being checked's value, just move to the next row (T F)
 #       elif bool(masterList[0][testingSelected]) != bool(masterList[1][testingSelected]):
 #           print('Check')
 #           testingSelected = testingSelected + 1
 #           if testingSelected > listNumRows:
 #               break
 #           continue
    #if the first premise's row being checked is not true then we cannot determine validity so just check the next row
 #   elif bool(masterList[0][testingSelected]) != True:
 #       print('Check')
 #       testingSelected = testingSelected + 1
 #       if testingSelected > listNumRows:
 #           break
 #       continue


#PRINT VALIDITY
if valid == True:
    print("~ARGUMENT VALID~")
else:
    print("~ARGUMENT INVALID~")
