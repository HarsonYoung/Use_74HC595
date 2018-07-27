#!/usr/bin/env python
#coding: utf8

import RPi.GPIO as GPIO
import time

Pin1 = 11
Pin2 = 12
Pin3 = 13
Pin4 = 15

DS = 36
ST_CP = 38
SH_CP = 40

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(DS,GPIO.OUT)
	GPIO.setup(ST_CP,GPIO.OUT)
	GPIO.setup(SH_CP,GPIO.OUT)
	GPIO.setup(Pin1,GPIO.OUT)
	GPIO.setup(Pin2,GPIO.OUT)
	GPIO.setup(Pin3,GPIO.OUT)
	GPIO.setup(Pin4,GPIO.OUT)
	GPIO.output(DS,GPIO.LOW)
	GPIO.output(ST_CP,GPIO.LOW)
	GPIO.output(SH_CP,GPIO.LOW)
#初始化GPIO

def shift(x):
	GPIO.output(SH_CP,GPIO.LOW)
	GPIO.output(DS,x)			 	#当X为1时，输出高电平
	GPIO.output(SH_CP,GPIO.HIGH)



def shiftout(num):
	s = 1				#掩码初始为1
	for i in range(1,9):	#循环8次，因有8位
		if (num & s) == 0:	#做 与 操作
			shift(0)				
		else:
			shift(1)
		s <<= 1	  #相当于s = s<<1



		
"""
	ABCDEFGH
1	10011111>>>159
2	00100101>>>37
3	00001101>>>13
4	10011001>>>153
5	01001001>>>73
6	01000001>>>65
7	00011111>>>31
8	00000001>>>1
9	00001001>>>9
0	00000011>>>3
		

"""		

num_key = {'1': 159,'2': 37,'3': 13, '4': 153, '5': 73, '6': 65, '7': 31, '8': 1 ,'9': 9, '0': 3}
#建立字典，便于读取对应的编码数



setup()
num1 = input("Type No.1>>>")
num2 = input("Type No.2>>>")
num3 = input("Type No.3>>>")
num4 = input("Type No.4>>>")#数字输入接口，可通过此接口输入任何想显示的数字如温度时间




try:	
	while True:
		#1010 1001
		GPIO.output(ST_CP,GPIO.LOW)
		shiftout(num_key[num1])
		GPIO.output(ST_CP,GPIO.HIGH)
		GPIO.output(Pin1,GPIO.HIGH)
		time.sleep(.005)
		GPIO.output(Pin1,GPIO.LOW)
		
		GPIO.output(ST_CP,GPIO.LOW)
		shiftout(num_key[num2])
		GPIO.output(ST_CP,GPIO.HIGH)
		GPIO.output(Pin2,GPIO.HIGH)
		time.sleep(.005)
		GPIO.output(Pin2,GPIO.LOW)
		
		GPIO.output(ST_CP,GPIO.LOW)
		shiftout(num_key[num3])
		GPIO.output(ST_CP,GPIO.HIGH)
		GPIO.output(Pin3,GPIO.HIGH)
		time.sleep(.005)
		GPIO.output(Pin3,GPIO.LOW)
		
		GPIO.output(ST_CP,GPIO.LOW)
		shiftout(num_key[num4])
		GPIO.output(ST_CP,GPIO.HIGH)
		GPIO.output(Pin4,GPIO.HIGH)
		time.sleep(.005)
		GPIO.output(Pin4,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
#使用Ctrl+C后，在程序停止之前，先清除GPIO数值以免影响之后的实验
