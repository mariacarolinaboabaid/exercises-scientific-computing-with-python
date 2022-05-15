filehandle = open("mbox-short.py")

for line in filehandle:
    line_x = line.rstrip()
    print(line_x.upper())

