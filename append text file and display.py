f = open("text.txt","a")
str = input("Enter Data TO Append  In Text File : ")
f.write(str)
f = open("text.txt","r")
print(f.read())
f.close()
