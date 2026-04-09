#hex()
a=15
b=hex(a)
print(b,type(b))
#output: 0xf <class 'str'>

a='oxF'
print(a,type(a))
#output: oxF <class 'str'>

a='oxF'
print(a,type(a))
#output: 0xF<class'str'>

a=0xF
print(a,type(a))
#output: 15 <class 'int'>

#float datatype
a=0.9
print(a,type(a),id(a))
#output: 0.9 <class 'float'> 2429165444432

#float datatype can also be used for storing scientific notation of data
a=3e2
print(a,type(a))
#output: 300.0 <class'float'>

print(10e-3)
#output: 0.01

a=0.0000000000000000000000000000000000000000000000000000005
print(a,type(a))
#output: 5e-55 <class 'float'>

#the advantage of scientific notation is that it represents big floating point values on short forms and takes less space

#bool datatype
a=True
b=False
print(a,type(a))
#output: True <class 'bool'>

print(True+True-False)
#output: 2

print(2*True+4-True)
#output: 5

#compleax datatype
a=2+3j
print(a,type(a))
#output: (2+3j) <class'complex'>

a=2.4+5.6j
print (a,type(a))
#output: (2.4+5.6j) <class'complex'>

print(a.real)
#output: 2.4

print(a.imag)
#output: 5.6

