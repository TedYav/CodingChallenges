n = int(input().strip())
gems = set(list(input().strip()))
for i in range(n-1):
	gems = gems.intersection(set(list(input().strip())))
print(len(gems))