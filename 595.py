#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time


DS = 36
ST_CP = 38
SH_CP = 40

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(DS,GPIO.OUT)
	GPIO.setup(ST_CP,GPIO.OUT)
	GPIO.setup(SH_CP,GPIO.OUT)
	GPIO.output(DS,GPIO.LOW)
	GPIO.output(ST_CP,GPIO.LOW)
	GPIO.output(SH_CP,GPIO.LOW)

def shift(x):
	GPIO.output(SH_CP,GPIO.LOW)
	GPIO.output(DS,x)               #当X为1时，输出高电平
	GPIO.output(SH_CP,GPIO.HIGH)

	
def shiftout(num):
	s = 1				#掩码初始为1
	for i in range(1,9):            #循环8次，因有8位
		if (a & s) == 0:	#做 与 操作
			shift(0)
		else:
			shift(1)
		s <<= 1			#相当于s = s<<1
	
	
setup()

try:	
	while True:
		#1010 1001
		GPIO.output(ST_CP,GPIO.LOW)
		
		shiftout(221)#它的二进制码将倒着输出，但74HC595也是“倒着”输出，此时第一位二进制数就对应着Q0口

		GPIO.output(ST_CP,GPIO.HIGH)  #做一次输出操作

		
except KeyboardInterrupt:
    GPIO.cleanup()
