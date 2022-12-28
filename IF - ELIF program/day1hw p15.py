# DAY 1 TASK NO.13 === Accept any city from the user and display monument of that city.

#           S.NO.                  CITY                               MONUMENT
          
#           1.                     BHOPAL                             BOAT CLUB,LAKEVIEW ,DB MALL
#           2.                     DELHI                              REDFORT
#           3.                     AGRA                               TAJMAHAL
#           4.                     JAIPUR                             JALMAHAL
#           5.                     UJJAIN                             MAHAKAAL MANDIR 




i=input('ENTER THE NAME OF THE CITY :')
if i=='bhopal':
        print('BOAT CLUB',' LAKEVIEW',' DB MALL')
elif i == 'delhi':
        print('REDFORT')
elif i == 'agra':
        print('TAJMAHAL')
elif i == 'jaipur':
        print('JALMAHL')
elif i == 'ujjain':
        print('MAHAKAAL MANDIR')
elif i:
    print("ENTER THE VALID CITY.") 