n = int(input())

love = "I love "
hate = "I hate "

print(hate, end="")
for i in range(1,n):
	print("that ", end="")
	print(love if i%2 else hate, end="")
print("it")