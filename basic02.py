# from sys import argv
# print('The length of command line argument is: ',len(argv))
# print('The list of command line argument is: ',argv)
# print('command line argument one by one: ',argv)
# for x in argv:
# 	print(x)
	
# """use of ternary operator
# write a program to find the biggest from two number"""
# a=int(input('Enter a: '))
# b=int(input('Enter b: '))
# big= a if a>b else b
# # print("{0} is the bigger than {0}".format(big, b))
# print('The biggest number is',big)

"""use of ternary operator
write a program to find the biggest from three number"""
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter b: '))
big= a if(a>b and a>c) else b if b>c else c
print("{0} is the bigger than {1}".format(big, b))
# print('The biggest number is',big)

