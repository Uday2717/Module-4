items = ['Mango', 'Orange', 'Apple', 'Lemon']
s1=str(items)
file = open('items.txt','w')
file.write(s1)
file.close()
