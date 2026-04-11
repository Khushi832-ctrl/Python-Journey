#Sequence category datatype: purpose is to store sequence of values. there 4 datatypes in sequence category.
#str datatype,byte datatype,bytearray datatype, range datatype
s1="python"
print(s1,type(s1))
#output: python <class 'str'>

s2='python'
print(s2,type(s2))
#output: python <class 'str'>

#memory management of str data
#iterable obj:contains one or more value,eg:str,byte,bytearray,range,list,dict
#non-iterable object: contains single value, does not contain length/size
s="python"
print(s,type(s))
#output: python <class 'str'>

s="python"
print(s,type(s))
print(len(s))
#output=6

print(len(s)-1)
#output=5

print(s[len(s)-1])
#output=n

print(-len(s))
#output:-6


