
# finds last element in array less than or equal to target value

def bin_search_lte(arr,target):
	low = 0
	high = len(arr) - 1
	guess = low + (high - low)//2
	
