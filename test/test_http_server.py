#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import requests

def test1():
    bai = 0
    shi = 0
    ge = 0
    for x in range(1,5):
        bai = x
        for y in range(1,5):
            if y != bai:
                shi = y
                for z in range(1,5):
                    if bai != z and shi != z:
                        ge = z
                        print(bai*100+shi*10+ge)

def test2():
    shouyi = int(input())
    lirun = 0
    lirun_list=[0.1,0.075,0.05,0.03,0.015,0.01]
    shouyi_list=[10,10,20,20,40]
    for x in range(0,5):
        if shouyi <= shouyi_list[x]:
            lirun += shouyi*lirun_list[x]
            break
        else:
            lirun += shouyi_list[x] * lirun_list[x]
            shouyi -= shouyi_list[x]

    return  lirun

def test3():
    for x in range(1,65535):
        for y in range(1,65535):
            if x+100 == y*y:
                for z in range(1,65535):
                    if x+100+168 == z*z:
                        print("x:"+str(x)+" x+100: "+str(y)+" x+268: "+str(z))
                        break

def test4():

    response = requests.get('https://www.baidu.com')
    print(response.text)


if __name__ == '__main__':
    test4()