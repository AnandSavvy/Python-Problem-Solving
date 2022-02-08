class amma:
 	def __init__(self,name,age):
 		self.x1=name;
 		self.x2=age;
 		print("my lovely amma")
 		super().__init__();

class Thamudu(amma):
	def __init__(self,name,age):
 		self.x7=name;
 		self.x8=age
 		print("strong person in my family")
 		super().__init__("sathya",45)
p=Thamudu("vishal",20)
print(p.x1,p.x2)
print(p.x7,p.x8)
#rint(p.x5,p.x6)                         
#print(p.x7,p.x8)

#a=Anna(name,age)
#print(a.x2,a.x1)
