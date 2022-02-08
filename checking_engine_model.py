class car():
	def __init__(self,x1,x2):
		self.x1=x1;
		self.x2=x2;
		print("CRDI engine")
		super().__init__();
	def breaks(self):
		print("its working")
		return "breaks are properly working"
class engine(car):
	print("it is used to turn the steering left and rightside")
 	#return "turning"
c=car("model",2022)
print(c.x1,c.x2)
print(c.breaks())
#s=steering()
#print(s)

eat=engine("anand",34)
print(eat)