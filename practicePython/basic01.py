# 1. print hello world
print("hello world")
# 2. add two numbers
a=5
b=5
c=a+b
print('The addition of two number is',c)
# 3. import a keyword
import keyword
print(keyword.kwlist)
# print the type of variable a.
x=type(a)
print(x)
# same value stored in different variable locates same memory location
print(id(a),id(b))
print(a is b)
#decimal, binary, octal, hex
hexa=0XFACE
decimal=int(hexa)
print(decimal)
print(bin(hexa))
print(hex(decimal))
print(oct(hexa))
#imaginary number-> complex data type
img=3+4j
print(img)
img1=12+3.4j
#add
add=img+img1
print(add)
#real part and imginary part ko retrieve kr sakte h using 
#var.real and var.imag;
print(add.real)
print(add.imag)

#division operator
print(10/2)
print(10//2)
# identity operator-> 1st-is, 2nd-is not
# membership operator-> 1st-in, 2nd-not in