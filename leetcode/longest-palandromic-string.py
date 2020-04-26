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
initString = "aaaabaaa"
if len(initString) == 0:
    print ""
elif len(initString) == 1:
    print initString
elif len(initString) == 2 and initString == initString[::-1]:
    print initString
elif initString == initString[::-1]:
    print initString
else:
    answer = initString[0]
    answer_length = 1
    for i in range(1, len(initString)-1):
        currIndex = i
        j = currIndex-1
        k = currIndex+1
        currString = initString[currIndex]
        leftString = ''
        rightString = ''
        while(j>=0 and k<len(initString)):
            leftString = initString[j]+leftString
            rightString = rightString + initString[k]
            newString = leftString+currString+rightString
            print 'left: '+leftString+' right: '+rightString+' new: '+newString+' answer:'+answer+' ans length:'+str(answer_length)
            if(newString == newString[::-1]):
                if(len(newString) >= answer_length):
                    answer = newString
                    answer_length = len(answer)
                    print 'yay:'+' answer:'+answer+' ans length:'+str(answer_length)
            else:
                break
            j-=1
            k+=1
        if currIndex<len(initString) and currString == initString[currIndex+1]:
            #new case
            #print 'new case: '+currString+currString
            j = currIndex - 1
            k = currIndex + 2
            leftString = ''
            rightString = ''
            while(j>=0 and k<len(initString)):
                leftString = initString[j]+leftString
                rightString = rightString + initString[k]
                newString = leftString+currString+currString+rightString
                #print 'left: '+leftString+' right: '+rightString+' new: '+newString
                if(newString == newString[::-1]):
                    if(len(newString) >= answer_length):
                        answer = newString
                        answer_length = len(newString)
                else:
                    break
                j-=1
                k+=1
        j = currIndex-1
        k = currIndex+1
        leftString = initString[j]
        rightString = initString[k]
        if j>= 0:
            newLeftString = leftString+currString
            if(newLeftString == newLeftString[::-1] and len(newLeftString) > answer_length ):
                answer = newLeftString
                answer_length = len(newLeftString)
        if k<len(initString):
            newRightString = currString+rightString
            if(newRightString == newRightString[::-1] and len(newRightString) > answer_length ):
                answer = newRightString
                answer_length = len(newRightString)    
    print answer
        