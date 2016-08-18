import string

ltrs = [c for c in string.ascii_lowercase]
s = list(input().strip())
pangram = False
for c in s:
	try:
		ltrs.remove(c.lower())
	except:
		pass
	if(len(ltrs)==0):
		pangram = True
		break
print("pangram" if pangram else "not pangram")