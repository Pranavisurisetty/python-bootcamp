# 4.find peak elem in an array

arr = [10, 20, 15, 2, 23, 90, 67]
n = len(arr)	
def Peak_elem(arr, low, end, n):
    # Find the middle index
	mid = low + (end - low)/2
	mid = int(mid)
	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
		(mid == n - 1 or arr[mid + 1] <= arr[mid])):
		return mid
	elif (mid > 0 and arr[mid + 1] > arr[mid]):
		return Peak_elem(arr, (mid + 1), end, n)
	else:
		return Peak_elem(arr, low, (mid - 1), n)
print("The peak point is", arr[Peak_elem(arr, 0, n - 1, n)])

