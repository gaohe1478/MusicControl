import csv
import  serial

ser  = serial.Serial('COM4',57600)
while True:
    a=ser.read(36)
    if a[0] == a[1] == 170 and a[2] == 32:
        #print(a[32])
        lowalpha = (a[13] << 16) | (a[14] << 8) | (a[15])
        highalpha = (a[16] << 16) | (a[17] << 8) | (a[18])
        theta = (a[9] << 16) | (a[10] << 8) | (a[11])
        delta = (a[7] << 16) | (a[8] << 8) | (a[9])
        lowbeta =((a[19] << 16) | (a[20] << 8) | (a[21]))
        highbeta = ((a[22] << 16) | (a[23] << 8) | (a[24]))
        #theta  = (a[10] << 16) | (a[11] << 8) | (a[12])
        lowgamma = ((a[25] << 16) | (a[26] << 8) | (a[27]))
        highgamma = ((a[28] << 16) | (a[29] << 8) | (a[30]))
        att = 0
        print (a[32])
        # if a[32]<35:
        #     att = 0
        # if a[32]>=35 and a[32]<65:
        #     att = 1
        # if  a[32]>=65:
        #     att = 2
        # with open("2020.5.01.csv",'a+',newline='') as t:#numline是来控制空的行数的
        #     writer=csv.writer(t)#这一步是创建一个csv的写入器
        #     n = [delta,theta,lowalpha,highalpha,lowbeta,highbeta,lowgamma,highgamma,att]
        #     writer.writerows(n)#写入样本数据