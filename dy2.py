#ocatlnumbersytem
a=0o10 
print(a,type(a)) 
#output: 8 <class'int'>

a=0o123
print(a,type(a))
#output: 83 <class'int'>

#ocatlnumbersytem
a=0xAC 
print(a,type(a))
#output: 172 <class'int'>

a=0x12
print(a,type(a))
#output: 18 <class 'int'>

#Base conversion functions
#bin()
a=10
b=bin(a)
print(b,type(b))
#output: 0b1010 <class'str'>

b=bin(0xA)
print(b,type(b))

a=0xF
b=oct(a)
print(b,type(b))
#output: 0o17 <class 'str'>