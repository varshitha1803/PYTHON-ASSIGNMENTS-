#Write a program to find maximum and minimum from the given digit?
n=int(input('enter the number:'))
num=int(input())
max=num
min=max
for i in range(1,n+1):
    num=int(input())
    if num>max:
        max=num
    elif num<min:
        min=num
print(max)
print(min)