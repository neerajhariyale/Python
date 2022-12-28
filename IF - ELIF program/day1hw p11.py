# DAY 1 TASK NO.9 === Write a program to accept the cost price of a bike and diplay the road tax to be paid according to the following criteria:
    
    
#             S.NO                  COST PRICE (in RUPEES)                               TAX 
            
#             1.                    >100000                                               15%
#             2.                    >50000 AND <=100000                                   10%
#             3.                    <=50000                                               5%





i=int(input('ENTER THE COST PRICE OF A BIKE :'))
if i >= 100000:
        print('15%',': IS THE ROAD TAX.')
elif i in range(50000,100000):
        print('10%',': IS THE ROAD TAX.')
elif i <= 50000:
        print('5%',': IS THE ROAD TAX.')
    