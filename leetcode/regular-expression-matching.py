'''
Given an input string (s) and a pattern (p), 
implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z,
and characters like . or *.
'''
str1 = 'aab'
str2 = 'c*a*b'
maxLength = len(str1)
uniqChar = []
for char in str1 :
    if char not in uniqChar:
        uniqChar.append(char)
# print(uniqChar)
possiblCases = []
for i in range(0, len(str2)):
    if str2[i] == '.':
        # pass
        if len(possiblCases) == 0:
            for char in uniqChar:
                possiblCases.append(char)
        else:
            tempPossibleCases = []
            for char in uniqChar:
                for j in range(0,len(possiblCases)):
                    tempStr = possiblCases[j] + char
                    tempPossibleCases.append(tempStr)
            possiblCases = tempPossibleCases
    elif str2[i] == '*':
        # pass
        if i == 0:
            pass
        else:
            prevChar = str2[i]
            if len(possiblCases) > 0:
                tempPossibleCases = []
                for j in range(0, len(possiblCases)):
                    possiblCasesStr = possiblCases[j]
                    possiblCasesStrLastChar = possiblCasesStr[len(possiblCasesStr)-1]
                    # 0 rep of last char
                    tempPossibleCases.append(possiblCasesStr[:-1])
                    # 0 to maxlen-1 rep of last char
                    for k in range(1, maxLength):
                        if(k == 1):
                            pass
                        else:
                            possiblCasesStr +=  possiblCasesStrLastChar
                        tempPossibleCases.append(possiblCasesStr)
                possiblCases = tempPossibleCases
    else:
        if len(possiblCases) == 0:
            possiblCases.append(str2[i])
        else:
            for j in range(0,len(possiblCases)):
                possiblCases[j] += str2[i]
# print(possiblCases)
flag = "false"
if str1 in possiblCases:
    flag = "true"
print(flag)