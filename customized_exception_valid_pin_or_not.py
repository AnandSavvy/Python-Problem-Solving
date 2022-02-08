# class InvalidPINError(Exception):
# 	def __init__(self):
# 		print("Invalid PIN. please enter a valid pin")
# class ATM:
# 	def __init__(self,card,pin):
# 		self.pin_check(pin)
# 	def pin_check(self,pin):
# 		if pin == 1447:
# 			print("transaction is running, wait for money")
# 		else:
# 			raise InvalidPINError()
# a=ATM("Visa",1447)
# a.pin_check(1447)


class InvalidPINError(Exception):
	def __init__(self):
		print("Invalid PIN. please enter a valid pin")
class ATM:
	def __init__(self,card,pin):
		self.pin_check(pin)
	def pin_check(self,pin):
		if pin == 1447:
			return "transaction is running, wait for money"
		else:
			raise InvalidPINError()
a=ATM("Visa",1447)
print(a.pin_check(1447))
