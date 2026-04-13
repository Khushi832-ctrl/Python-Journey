#slicing operation: purpose is to get substring or range of values from main str obj
#The process of obtaining range of values or substring from main str obj is called slicing.
#syntax(1) str obj [BEGIN:END]
# case(1): positive BEGIN: positive END provided BEGIN<END index
s="python"
print(s,type(s)) 
#output:python <class 'str'>

print(s[0:5])
#output: pytho

print(s[1:4])
#output: yth

#case(2): -ve BEGIN: -ve END provided BEGIN<END index
s="python"
print(s[-5:-1])
#output: ytho

print(s[-6:-3])
#output: pyt

print(s[-2:-1])
#output: o

#case(3):+ve BEGIN: -ve END ignore BEGIN<END index
print(s[2:-1])
#output: tho

print(s[2:-4])
#output:' '

#case(4): -ve BEGIN: +ve END ignore BEGIN<END index
print(s[-6:6]) 
#output: 'python'

print(s[-3:6])
#output: hon

print(s[0]+s[-3:-1])
#output: pho

print(s[0:1]+s[-3:1])
#output: p