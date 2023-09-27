"Task 1"
"1.1"
print('4','8','15','16','23','42')
"1.2"
print('4')
print('8')
print('15')
print('16')
print('23')
print('42')
"1.3"
a = int(input())
print(a+1)
print(a+2)
"1.4"
d_ = int(input())
_u = int(input())
p = int(input())
print(d_+_u+p)
"1.5"
'''
Сначала вводим длину ребра через тип данных int 
который принимает только целые числа
'''
a1 = int(input())
'''
Вводим формулу обьема куба и поверхности куба через команду Print
'''
print("Volume is =",a1**3)
print("Total surface area is =",6*(a1**2))
"Task 2"
"2.1"
d_ = int(input())
b_1 = int(input())
print(f"{b_1//d_}\n{b_1%d_}")
"2.2"
c = int(input())
c1 = c//1000
c2 = (c//100)%10
c3 = (c%100)//10
c4 = c%10
print('The number in the thousands position equals', c1)
print('The number in the hundreds position is', c2)
print('The digit in the tens position is equal to', c3)
print('The digit in the units position is equal to', c4)
"2.3"
e = int(input())
print(e//2+e%2)
"2.4"
try:
    e = int(input("Enter the number:"))
    if e==0:
        print("Error,Try again!")
    else:
        print("The result of << is:",2**e)
except ValueError:
    print("Please enter a valid integer!")



"2.5"
print("please enter the first number:")
e = int(input())
print("please enter the second number:")
m = int(input())
print("please choose an operation (+, -, *, /):")
b = str(input())
if b=='+' :
    print(e+m)
elif b=='-':
    print(e-m)
elif b=='*':
    print(e*m)
elif b=='/':
    print(int(e/m))
