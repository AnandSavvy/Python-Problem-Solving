import re 
txt= "my name,is.anand"
pattern='[ , .]'
replace='#'
result= re.sub(pattern,replace,txt)
print(result)