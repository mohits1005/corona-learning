num = 123
new_num = 0
neg = 0
if(num<0):
    neg = 1
    num *= -1
while(num > 0):
    rem = num % 10
    num = num / 10
    new_num = new_num * 10 + rem
if(neg):
    print -new_num
else:
    print new_num