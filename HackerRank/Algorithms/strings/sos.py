s = list(input().strip())
count = 0
for i in range(0,len(s),3):
	count += int(s[i] != 'S') + int(s[i+1] != 'O') + int(s[i+2] != 'S')
print(count)