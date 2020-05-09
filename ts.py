import math
import binascii
def str2hex(s):
    odata = 0;
    su =s.upper()
    for c in su:
        tmp=ord(c)
        if tmp <= ord('9') :
            odata = odata << 4
            odata += tmp - ord('0')
        elif ord('A') <= tmp <= ord('F'):
            odata = odata << 4
            odata += tmp - ord('A') + 10
    return odata
file = open("data1.txt","r")

list = file.readlines()

for i in range(512):
    b=int(list[i])
    a=str2hex(b)
    lowalpha = (a[13] << 16) | (a[14] << 8) | (a[15])
    highalpha = (a[16] << 16) | (a[17] << 8) | (a[18])
    print(a[34])
    print(math.log(lowalpha,10))
    print(math.log(highalpha))
    print("--------------")