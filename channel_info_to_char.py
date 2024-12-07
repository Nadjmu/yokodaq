f = open('channel_info_python.csv','r')
g = open('channel_in_char','w')
lines = f.readlines()

i = 0

for line in lines[1:-210]:
    x = line.split(",")
    in_char = chr(int(x[1]))
    line2 = str(i)+","+in_char
    g.write(line2)
    g.write('\n')
    i=i+1