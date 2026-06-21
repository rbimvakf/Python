f = open("Magic.txt", 'r')
body = f.read()
f.close()

body = body.replace("java", "python")
f = open("Magic.txt", 'w')
f.write(body)
f.close()
