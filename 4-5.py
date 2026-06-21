f = open("Magic.txt", 'w')
f.write("Life is too short")
f.close()

f = open("Magic.txt", 'r')
print(f.read())
f.close()
