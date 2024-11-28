
#Print Characters at Even Indices in a String

def getCharAtIndicesInString(inputStr):

    result = ''
    counter = 0
    for i in inputStr:
        if counter % 2 == 1:
            result += i
        counter += 1
    return result

    
print(getCharAtIndicesInString("abcdef"))


    