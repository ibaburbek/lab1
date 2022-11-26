print('#1.')
x = []
a, b = int(input()), int(input())
for i in range(a, b+1):
    if i%2==0:
        x.append(i)

s = ' '.join(x)

print('#2.')
x = int(input())
for i in range(2,x+1):
    if x%i==0:
        print(i)
        break

print('#3.')
s = []
x = int(input())
for i in rang(1,x+1):
    if x%i==0:
        s.append(i)
n = ' '.join(s)
print(n)

print('#4.')
n = int(input())
s = 0
for i in range(n):
    s += int(input())
print(s)

print('#5.')
s = input()
n = len(s)
x = 0
for i in range(n):
    if s[i]=='1':
        x += 2**(i)
print(x)

print('#6.')
s = [int(x) for x in input().split()]
x = s[0]**s[1]
print(x)

print('#7.')
s = [int(x) for x in input().split()]
x0 = s.count(0)
x1 = s.count(1)
x=0
if x0<x1:
    x=1
print(x)

print('#8.')
amount=0
def addToBankAccount(x):
    amount=amount+x
    return amount

def substractFromBankAccount(x):
    amount-=x
    return amount

def moneyConversion(x,convertFrom,convertTo):
    if convertFrom=='USD' and convertTo=='KZT':
        return x*470
    if convertFrom=='KZT' and convertTo=='USD':
        return x/470