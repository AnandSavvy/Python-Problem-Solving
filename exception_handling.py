
class Test:
	def stuff(self):
		pass
		#self.doStuff();#instance method
	def doStuff(self):

		
		try:
			print("anand")
			print(10/0)
		except ZeroDivisionError as z:
			print(z)
		except NameError as n:
			print(n)
		except Exception as e:
			print(e)
		


	# 	try:
	# 		print(y)
	# 	except:
	# 		print("we can't divisible by zero so..")
	# 		print(10/2)
	# 		print("we get the output")
			
	# 	else:
	# 		pass
	# 	finally:
	# 		print("im always executes the program")
	# def Morestuff(self):
	# 	pass
	
		# print("hello")
		# try:
		
		# 	print("its possile?")
		# 	print(10/0)
		# 	print("annad")
		
		# except:
		# 	print("we can't divisible by zero so..")
		# 	print(10/0)
		# 	print("we get the output")
			
		# else:
		# 	print("error raised in except block")
		# finally:
		# 	print("im always executes the program")







t=Test()
t.stuff() 
t.doStuff()




