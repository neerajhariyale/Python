# DAY 1 TASK NO.5 === Write a program to calculated the electricity bill(accept number of unit from user)according to the following criteria :



                #  S.NO         UNIT                     PRICE
                #  1.           first 100 units          no charge
                #  2.           next 100 units           RS 5 per unit
                #  3.           after 200 units          RS 10 per units
                
                
                # for example === if input unit is 350 than total bill amount is RS2000.
                  
                  

n=int(input('ENTER THE UNIT AND GET THE ELECTRICITY BILL :'))
if n in range(0,101):
     print(n ,' ', ':IS THE ELECTRICITY BILL.')
elif n in range(101,201):
     print(n*5,' ', ':IS THE ELECTRICITY BILL.')
elif n in range(201,5000):
     print(n*10,' ', ':IS THE ELECTRICITY BILL.')

     