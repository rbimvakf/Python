f = open("C:/Users/SHHERKY/Desktop/Magic.txt", 'r')
body = f.read()
f.close()

body = body.replace("java", "python")
f = open("C:/Users/SHHERKY/Desktop/Magic.txt", 'w')
f.write(body)
f.close()
