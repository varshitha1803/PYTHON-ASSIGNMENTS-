#Write a program to print leap years upto given range?
def leap(y):
    if n1%4==0 or n1%100!=0 and n1%400==0:
        return 1
    else:
        return 0
n1=int(input())
n2=int(input())
while(n1<n2):
    if leap(n1)==1:
        print(n1,end=' ')
    n1=n1+1   