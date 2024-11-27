
#calculator
def calculation(operation,a,b):
    if (operation == "*"):
        result = a*b
    elif(operation  == "/"):
        result = a / b
    elif(operation  == "+"):
        result = a + b
    elif(operation  == "-"):
        result = a - b
    else:
        return "Error! Wrong operation"                     
    return result

def calculationResult(result):
    print(result)

def main():
    operator,a,b = user_input()
    result = calculation(operator,a,b)
    calculationResult(result)

if __name__ == '__main__':
    main()
