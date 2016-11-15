from PIL import Image
from pylab import *
import os

index = 0
temp = '00'


def trancehcl():
    if index == 0 :
        temp = f.read(1)
        temp = temp.encode('hex')
        data = trance1622(temp[0])
        data += trance1622(temp[1])
        temp = data
        return(temp[index-1])

def trance1622(str):

    map = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
           '4':'0100', '5':'0101', '6':'0110', '7':'0111',
           '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
           'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'}
    return map[str]


if __name__ == '__main__':
    for n in range(0,3):
        filename = "hh%03d" %(n+1)
        f = open("hcl/"+filename+".hcl", 'rb')
        f.read(512)
        #f.read(512)
        index = 0
        while f.tell() < 1923072:
            d = zeros((64, 64))
            index += 1
            for i in range(0, 64):
                for j in range(0, 8):
                    temp = f.read(1)
                    temp = temp.encode('hex')
                    # print temp
                    data = trance1622(temp[0])
                    # print data
                    data += trance1622(temp[1])
                    for k in range(0, 8):
                        d[i][j*8+k] = (1-int(data[k]))*255
            gray()
            if not os.path.exists('data/%d/' % index):
                os.mkdir('data/%d/' % index)
            imsave('data/%d/%s.jpg' % (index, filename), d)
            print "saving data/%d/%s.jpg" % (index, filename)

