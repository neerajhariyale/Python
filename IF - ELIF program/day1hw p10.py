# DAY 1 TASK NO.8 === Write a Program to accept percentage from the user and display the grade acccording to the following criteria:
    
#               S.NO.           MARKS                          GRADE
              
#               1.              >90                             A
#               2.              >80 and <=90                    B
#               3.              >=60 and <=80                   C
#               4.              below 60                        D         

i=int(input('WRITE THE PECENTAGE AND GET GRADE :'))

if i in range(90,100):
        print('A' ,' ',': IS THE GRADE OF YOUR PERCENTAGE.')
elif i in range(80,90):
        print('B',' ',': IS THE GRADE OF YOUR PERCENTAGE.')
elif i in range(60,80):
        print('B',' ',': IS THE GRADE OF YOUR PERCENTAGE.')
elif i in range(0,60):
        print('D',' ',': IS THE GRADE OF YOUR PERCENTAGE.')