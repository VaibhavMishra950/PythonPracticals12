import bisect
L1=eval(input('Enter any sorted List: '))
print("Now List is Sorted : ",L1)
item=int(input('Enter new element to be inserted : '))
pos=bisect.bisect(L1,item)
bisect.insort(L1,item)
print(item,"inserted at index",pos)
print('The list after inserting element: ')
print(L1)