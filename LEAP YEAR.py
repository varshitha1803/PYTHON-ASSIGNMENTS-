#Write a program to print given year is leap year or not?
n=int(input('enter the number:'))
if n%4==0 and  n%100!=0:
    print('Leaoyear!')
if n%400==0:
    print('leap year!')
else:
     print('not a leap year:')
     