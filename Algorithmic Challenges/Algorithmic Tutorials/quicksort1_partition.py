def partition(ar):
	#set pivot
	partitioner = ar[0]
	count = 0

	lower = []
	higher = []

	#sort array into higher and lower than pivot
	for i in ar:
		if i < partitioner:
			lower.append(i)
		elif i == partitioner:
			count += 1
		else:
			higher.append(i)
	
	#add duplicates of pivot back in
	while count > 0:
		lower.append(partitioner)
		count -= 1

	#join lists and format printing for tests
	ar = lower + higher
	print ''.join(str(ar)).replace(',','').replace('[','').replace(']','')

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)