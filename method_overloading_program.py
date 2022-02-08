class Anand:
 	def __init__(self,x1,x2):
 		self.x1=x1;
 		self.x2=x2;
 		print("constructor is working perfectly")
 	def naidu(self):#method over ridding
 		return "hello hii"
 		super().__init__();
class my_Anand(Anand):
 	def __init__(self,x3,x4):
 		self.x3=x3;
 		self.x4=x4;
 		print("my_anand is running by Anand class")
 		super().__init__(45,67);
 	def naidu(self): #method over ridding
 		return "nice to meet you"

M=my_Anand(3,4)
print(M.x1,M.x2)
print(M.naidu())

