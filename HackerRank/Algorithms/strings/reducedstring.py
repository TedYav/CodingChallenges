def equal(s1, s2):
	if(len(s1) != len(s2)):
		return False
	for i in range(len(s1)):
		if(s1[i]!=s2[i]):
			return False
	return True

s = list(input().strip())
out, prev, i = s, [], 0
while(not equal(out, prev)):
	prev, out, i = out, [], 0
	prev.append('_')
	while(i < len(prev)-1):
		if(prev[i] != prev[i+1]):
			out.append(prev[i])
		else:
			i += 1
		i += 1
	prev.pop()
print("".join(out) if len(out) > 0 else "Empty String")