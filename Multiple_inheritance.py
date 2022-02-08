'''
class car:
	def __init__(self):
		self.x=10;
		print(" na car ")
class bmw(car):
	def __init__(self):
		self.x=20; 
		print("black bmw")
class bmw_3_series(bmw):
	pass;
class bmw_7_series(bmw):
	def __init__(self):
		self.x=30;
		print("7 series car")
		super().__init__();
class benz(car):
	def __init__(self):
		self.x=40;
		print("benzzz is royal")
		super().__init__();
class test(benz,bmw_7_series,bmw_3_series):
	def __init__(self):
		self.x=50;
		print("testing all cars")
		super().__init__();
tr=test();
print(tr.x)




1..output;
testing all cars
benzzz is royal
7 series car
black bmw
20


'''

'''
class car:
	def __init__(self):
		self.x=10;
		print(" na car ")
class bmw(car):
	def __init__(self):
		self.x=20; 
		print("black bmw")
		super().__init__()
class bmw_3_series(bmw):
	pass;
class bmw_7_series(bmw):
	def __init__(self):
		self.x=30;
		print("7 series car")
		super().__init__();
class benz(car):
	def __init__(self):
		self.x=40;
		print("benzzz is royal")
		super().__init__();
class test(bmw_3_series,bmw_7_series,benz):
	def __init__(self):
		self.x=50;
		print("testing all cars")
		super().__init__();
tr=test();
print(tr.x)
   

output:
testing all cars
7 series car
black bmw
benzzz is royal
 na car 
10


'''




class car:
	def __init__(self):
		self.x=10;
		print(" na car ")
class bmw(car):
	def __init__(self):
		self.x=20; 
		print("black bmw")
		super().__init__()
class bmw_3_series(bmw):
	pass;
class bmw_7_series(bmw):
	def __init__(self):
		
		self.x=30;
		print("7 series car")
		super().__init__();
class benz(car):
	def __init__(self):
		self.x=40;
		print("benzzz is royal")
		super().__init__();


class test(bmw_7_series,bmw_3_series,benz):
	def __init__(self):
		self.x=50;
		print("testing all cars")
		super().__init__();
		print("last statement")
tr=test();
print(tr.x)




#testing all caers
#black bmw   na car 7 series car  benz is royall 
