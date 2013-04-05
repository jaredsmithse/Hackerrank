def quickSort(ar):
	#set pivot as first number in the array
	pivot = ar[0]
	count = 0

	lower = []
	higher = []

	#Split the numbers in to two sets above and below
	#the pivot. If equal increase the counter.
	for i in ar:
		if i < pivot:
			lower.append(i)
		elif i == pivot:
			count += 1
		else:
			higher.append(i)
	
	#If there are multiple values in the lower set,
	#call quickSort again.
	if len(lower) > 1:
		
		lower = quickSort(lower)

	#If there are multiple values in the upper set,
	#call quickSort again.
	if len(higher) > 1:
		
		higher = quickSort(higher)

	#add back the multiple values of the pivot if there were any
	while count > 0:
		lower.append(pivot)
		count -= 1

	#rejoin the list
	ar = lower + higher

	#print list in format required
	print ''.join(str(ar)).replace(',','').replace('[','').replace(']','')
	return ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)