""" string in python """
# ALL are valid string
str="Ranjan"
str1='Ranjan' 
str2='\'Ranjan\'' #use of '
str3='"Ranjan"' #inside ""
str4="'Ranjan'" #inside ''
str5='RanjanKumar' 
print(str,str1)

""" Acessing """
# forward and backward direction are allowed in python
# slicing concept 
# syntax
# str[startIndex:endIndex:step]
print(str5[0])
print(str5[-1])
print(str5[-3])
print(str5[0:5])
print(str5[-1:])
print(str5[:-1])
print(str5[::1]) #ranjankumar
print(str5[::-1]) # reverse i.e. ramuknajnar
#print(str5[9:0:0]) # valueError: slice step cannot be zero
# in some case like step or endIndex is 1 or -1 then it may return
# empty string
# slice operator never raises IndexError

""" membership operator """
s="ranjan"
print("ran" in s) #return true
print("x" in s) #return false