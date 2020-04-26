'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
initString = "babad"
answer = initString[0]
answer_length = 1
for i in range(1, len(initString)-1):
    currIndex = i
    j = currIndex-1
    k = currIndex+1
    currString = initString[currIndex]
    leftString = ''
    rightString = ''
    flag = 1
    while(j>=0):
        leftString = initString[j]+leftString
        rightString = rightString + initString[k]
        newString = leftString+currString+rightString
        if(newString == newString[::-1] and len(newString) > answer_length ):
            answer = newString
            answer_length = len(newString)
        else:
            flag = 0
            break
        j-=1
        k+=1
    if(flag == 0):
        newLeftString = leftString+currString
        newRightString = currString+rightString
        if(newLeftString == newLeftString[::-1] and len(newLeftString) > answer_length ):
            answer = newLeftString
            answer_length = len(newLeftString)
        elif(newRightString == newRightString[::-1] and len(newRightString) > answer_length ):
            answer = newRightString
            answer_length = len(newRightString)
print answer
print answer_length
    