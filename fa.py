def isAlphabet(s):
    alphabet = True
    i = 0
    while (alphabet == True) and (i < len(s)) :
        if (65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122 or ord(s[i]) == 95 or ord(s[i]) == 36) :
            alphabet = True
        else :
            alphabet = False
        i += 1
    return alphabet

def isNumber(s):
    number = True
    i = 0
    while (number == True) and (i < len(s)) :
        if (48 <= ord(s[i] <= 57)) :
            number = True
        else :
            number = False
        i += 1

    return number

def isVariable(s):
    variable = True
    i = 0
    while (variable == True) and (i < len(s)) :
        if (i == 0):
            if (not isAlphabet(s[i])) :
                variable = False
        elif (isAlphabet(s[i]) or isNumber(s[i])) :
            continue
        else :
            variable = False
        i += 1

    return variable

# def isOperator(c):
#     listOperator = ['+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^', '~']
#     operator = False
#     i = 0
#     while (i<len(listOperator) and (operator == False)) :
#         if (c == listOperator[i]) :
#             operator = True
#         i+=1
#     return operator

# def isTernaryOperator(c):
#     listTernary = [':', '?']
#     ternary = False
#     i = 0
#     while (i<len(listTernary) and (ternary == False)) :
#         if (c == listTernary[i]) :
#             ternary = True
#         i+=1
#     return ternary

# def isOperand(state, c):
#     if (isNumber(c) or isAlphabet(c)) :
#         return True
#     else :
#         return False

# def isSpace(state, c):
#     if (isSpace(c)) :
#         return True
#     else :
#         return False

# def processOperator(string, i) :
#     operator = string[i] 

#     while (isOperator(string[i+1])) :
#         i += 1
#         operator = operator + string[i]

#     arithmetic = ['+', '-', '*', '/', '%', '**']
#     decremental = ['++', '--']
#     assignment = ['=', '+=', '-=', '*=', '/=', '%=']
#     comparison = ['>', '<', '==', '!=', '>=', '<=', '===', '!===']
#     logical = ['!', '&&', '||']
#     bitwise = ['&', '|', '~', '^', '<<', '>>', '>>>']

#     operatorType = "undefined"
#     j = 0
#     while (operatorType == "undefined" and j < len(arithmetic)) :
#         if (operator == arithmetic[j]) :
#             operatorType = "arithmetic"
#         j+=1
#     j = 0
#     while (operatorType == "undefined" and j < len(decremental)) :
#         if (operator == decremental[j]) :
#             operatorType = "decremental"
#         j+=1
#     j = 0
#     while (operatorType == "undefined" and j < len(assignment)) :
#         if (operator == assignment[j]) :
#             operatorType = "assignment"
#         j+=1
#     j = 0
#     while (operatorType == "undefined" and j < len(comparison)) :
#         if (operator == comparison[j]) :
#             operatorType = "comparison"
#         j+=1
#     j = 0
#     while (operatorType == "undefined" and j < len(logical)) :
#         if (operator == logical[j]) :
#             operatorType = "logical"
#         j+=1
#     j = 0
#     while (operatorType == "undefined" and j < len(bitwise)) :
#         if (operator == bitwise[j]) :
#             operatorType = "bitwise"
#         j+=1

#     return operatorType, i

# # STATE PROCESSOR
# def processZero(string, i):
#     if (isSpace(string[i])) :
#         return 0, i
#     elif (string[i] == '-') :
#         return 1, i
#     elif (isNumber(string[i])) :
#         return 2, i
#     elif (isAlphabet(string[i])) :
#         return 3, i
#     else :
#         return -1, i

# def processOne(string, i) :
#     if (isNumber(string[i])) :
#         return 2, i
#     else :
#         return -1, i

# def processTwo(string, i) :
#     if (isNumber(string[i])) :
#         return 2, i
#     elif (isSpace(string[i])) :
#         return 4, i
#     elif (isOperator(string[i])) :
#         operatorType,i = processOperator(string, i)

#         if (operatorType == "arithmetic" or operatorType == "comparison" or operatorType == "logical" or operatorType == "bitwise") :
#             state = 
#         elif (operatorType)
#         return state, i
#     else :
#         return -1, i

# def processThree(string, i) :
#     if (isAlphabet(string[i])) :
#         return 3, i
#     elif (isNumber(string[i])) :
#         return 3, i
#     elif (isSpace(string[i])) :
#         return 4
#     elif (isOperator(string[i])) :
#         return 5, i
#     else :
#         return -1, i

# def processFour(string, i) :
#     if (isSpace(string[i])) :
#         return 4, i
#     elif (isOperator(string[i])) :
#         return 5, i
#     else :
#         return -1, i





# # 0 = start state
# # 1 = dimulai dengan '-', state berikutnya harus diikuti angka
# # 2 = angka
# # 3 = variable
# # 4 = space setelah operand
# # 5 = operator setelah operand

# def stringEvaluator(string):    
#     state = 0

#     for[]

        