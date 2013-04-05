def insertionSort(ar):
	
	#set placeholders and booleans
	hold = ar[-1]
	sorted = False
	s = len(ar)

	#get rid of base cases
	if (s == 1) or (ar[-2] < ar[-1]):
		print ''.join(str(ar)).replace(',','').replace('[','').replace(']','')

	#do the first switch
	ar[-1] = ar[-2]
	
	i = s-1
	while sorted == False:
		#if we are done, switch the current number to the one being inserted
		if i == 0:
			ar[i] = hold
			print ''.join(str(ar)).replace(',','').replace('[','').replace(']','')
			break
		#if the number to the left is larger, continue moving over to the left
		if ar[i-1] > hold:
			ar[i] = ar[i-1]
			print ''.join(str(ar)).replace(',','').replace('[','').replace(']','')
			i -= 1
		#if the number being inserted is in the right place, insert it
		elif ar[i-1] <= hold:
			ar[i] = hold
			print ''.join(str(ar)).replace(',','').replace('[','').replace(']','')
			break
		else:
			i -= 1

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)