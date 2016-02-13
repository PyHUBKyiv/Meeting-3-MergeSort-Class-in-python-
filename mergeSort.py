def merge(a,b):
	result = []
	i = 0
	j = 0
	while i<len(a) and j<len(b):
		if a[i]<b[j]:
			result.append(a[i])
			i+=1
		else:
			result.append(b[j])
			j+=1
	if i==len(a):
		result+=b[j:]
	else:
		result+=a[i:]

	print(result)	
	return result

def merge_sort(d):
	len_d = len(d)
	if len_d < 2:
		return d
	mid = len_d // 2	
	print(d[:mid],d[mid:])
	a1 = merge_sort(d[:mid])
	a2 = merge_sort(d[mid:])
	result=merge(a1,a2)
	print result
	return result	

assert merge([1,3],[2,4])==[1,2,3,4]
assert merge([1,3,6],[2,4])==[1,2,3,4,6]

#positive tests
assert merge_sort([1])==[1]
assert merge_sort([5])==[5]
assert merge_sort([5,7])==[5,7]
assert merge_sort([5,3,7])==[3,5,7]
assert merge_sort([-4,6, 3,-1,7])==[-4,-1,3,6,7]

#negative tests
assert merge_sort([])==[]
assert merge_sort([0,0,0,0,0])==[0,0,0,0,0]