# DAY 1 TASK NO.14 === Write a Program to check whether a number entered is three digit number or not.

i = int(input('ENTER THREE DIGITS NO. :'))
if i in range(100,1000):
        print(i,' : THIS IS THREE DIGIT NUMBER.')
elif i <=1000:
        print(i,' : THIS IS NOT THREE DIGIT NUMBER.')
elif i >=99:
        print(i,' : THIS IS NOT THREE DIGIT NUMBER.')             
