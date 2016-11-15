f= open('hh001.hcl', 'rb')
f.read(512)
index=0
for i in range(0,16):
    print "%3s" % hex(i) ,
print
for i in range(0,16):
    print "%-3s" % "#" ,
print
for i in range(0,512):
    temp=f.read(1)
    if len(temp) == 0:
        break
    else:
        #print "%3s" % temp.encode('hex'),
        a = temp.encode('hex')
        #a = int(a,16)
        #a = bin(int(a))
        print "%3s" % a,
        index=index+1
    if index == 8:
        index=0
        print
f.close()