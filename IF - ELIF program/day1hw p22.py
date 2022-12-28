# DAY 1 TASK NO.20 === Write a program to find the largest number out of three number ecepted from the user.



i=int(input('ENTER THE NUMBER A :'))
j=int(input('ENTER THE NUMBER B :'))
k=int(input('ENTER THE NUMBER C :'))

if i<=j<=k:
        print(k)
elif i>=j>=k:
        print(i)
elif i<=j>=k:
        print(j)