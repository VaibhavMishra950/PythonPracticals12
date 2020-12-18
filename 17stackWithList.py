
def push_stack(lst, elm):
	lst.append(elm)

def pop_stack(arr):
	if arr == []:
		print("Underflow")
	else:
		return arr.pop()

def display_stack(arr):
	if arr == []:
		print("Stack Is Empty")
	else:
		top = len(arr)-1
		print(arr[top], " <--Top--")
		for x in range(top-1, -1, -1):
			print(arr[x])


arr = [20, 40, 26, 57] 

menu = """
             Stack Opertaions
1. Push
2. Pop
3. Display
4. Exit

"""
while True:
	print(menu)
	ch = int(input("Enter Your Choice [1-4]: "))
	if ch == 1:
		el = int(input("Enter Element To Insert: "))
		push_stack(arr, el)
		print("Element Pushed")
	
	elif ch == 2:
		item = pop_stack(arr)
		print("Popped ", item)
	
	elif ch == 3:
		display_stack(arr)
	
	elif ch == 4:
		exit()
	
	else:
		print('Invalid Choice')
