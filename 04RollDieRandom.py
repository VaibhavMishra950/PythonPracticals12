import random
ch = "Y"
while ch.lower()=='y':
	val = random.randint(1,6)
	print("Value Got After Rolling Die: ", val)
	ch = input("Roll Again [Y / N]: ")

