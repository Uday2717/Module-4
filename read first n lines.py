n=int(input("Enter Lines To Read : "))
f=open("text.txt","r")
for i in range(n):
	print(f.readline())
