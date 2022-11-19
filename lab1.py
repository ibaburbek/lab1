# 1. Gipotenuza
a = int(input())
b = int(input())
c = (a**2 + b**2)**0.5
print('Answer 1: ', c)

#2.
a = int(input())
b = a//10
c = b%10
print('Answer 2: ', c)

#3.
a = int(input())
b = a//2
c = 2*(b+1)
print('Answer 3: ', c)

#4.
a = int(input())
b = a-1
c = b//2
d = b-c
e = 45*a + c*15 + d*5
f = e//60
g = e%60
print('Answer 4: ', f, g)

#5.
a = int(input())
b = int(input())
if a>b:
    print('Answer 5: ', 1)
elif a<b:
    print('Answer 5: ', 2)
else:
    print('Answer 5: ', 0)

#6.
a = int(input())
b = int(input())
c = int(input())
max = a
if max>b:
    if max<c:
        max=c
else:
    if b>c:
        max=b
    elif b<c:
        max=c
print('Answer 6: ', max)

#7.
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if a1==b1 or a2==b2:
    print('Answer 7: ', 'YES')
else:
    print('Answer 7: ', 'NO')

#8.
a = int(input())
b = int(input())
c = int(input())
if a+b>c>a-b and a+c>b>a-c and b+c>a>b-c:
    print('Answer 8: ', 'YES')
else:
    print('Answer 8: ', 'NO')

#9.
a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print('Answer 9: ', 3)
elif a==b or a==c or b==c:
    print('Answer 9: ', 2)
else:
    print('Answer 9: ', 0)

