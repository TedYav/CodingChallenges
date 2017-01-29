"""

	LCS(A,B) is really asking:
		LCS of A and B starting at index 0 in both
	Thus, we can define F(i,j) as LCS(A,B) starting at A_i and B_j
	F(i,j) = {
		if i > n - 1  :: 0
		if j > m - 1  :: 0
		if A_i == B_j :: F(i+1,j+1) + 1
		if A_i != B_j :: max(F(i+1,j), F(i,j+1))
	}

"""


def run():
	n,m = map(int, input().strip().split())
	A = list(map(int, input().strip().split()))
	B = list(map(int, input().strip().split()))
	print(" ".join(map(str,longest_common_subsequence(A,B,n,m))))

# passing n and m in...could compute

def longest_common_subsequence(arr1, arr2, n,m):
	LCS = [[[] for i in range(m)] for j in range(n)]
	for i in range(n-1,-1,-1):
		for j in range(m-1, -1, -1):
			if arr1[i] == arr2[j]:
				LCS[i][j] = [arr1[i]] + (LCS[i+1][j+1] if i+1 < n and j+1 < m else [])
			else:
				LCS[i][j] = longest(LCS[i+1][j] if i+1 < n else [], LCS[i][j+1] if j+1 < m else [])
	return LCS[0][0]


def longest(arr1, arr2):
	return arr1 if len(arr1) > len(arr2) else arr2

run()