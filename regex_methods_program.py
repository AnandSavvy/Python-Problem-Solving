'''
regex is used to extract the target pattern in given string 
match: it is used to check the word at begning of the string only not entire string;
search: is used to search first occurance in the string 
findall: is finds the whole string and return how many times repeat the string

'''


import re
sir=" dexterious is teaching python in adm"
result=re.search('is',sir)
# print(re.match("is",sir))
# print(re.findall("t",sir))#findall() is used to find something(pattern,expression) from sir string
# print(re.search("xt",sir ))
# print(result.group())
print(re.findall(r'[a-z]',sir))
print(re.findall(r'[a-z]+',sir))#using findall fn to find out something(pattern) from sir"string"
print(re.search(r'[a-z].+',sir )) 
print(re.match(r'[a-z].+',sir))
print(re.findall(r't',sir))
print(re.findall(r't.',sir))
print(re.findall(r't*',sir))
print(re.findall(r't.*',sir))
print(re.findall(r't[a-z].',sir))




sample="John age is 22, Anand age is 23, Naidu age is 22"
names=re.findall(r'[A-z][a-z]+',sample)
print(names) 

ages=re.findall(r'\d{1,3}',sample)
print(ages)
s=1
p={}
for each in names:
	p[each]=ages[1]
	s=s+1
print(p)

