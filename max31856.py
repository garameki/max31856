# _*_ coding:utf-8 _*_

import sys
import codecs
from time import sleep
import spidev


#関数
filename = "max31856.txt"	#権限は -rw-rw---- www-data www-data
def fwrite(valueFlt,valueHJ,valueCJ):
	global filename
	file = codecs.open(filename,"w","utf-8")
	jsonResult = "{{FAULT:{0}\nHJ:{1}\nCJ:{2}\n}}".format(valueFlt,valueHJ,valueCJ)
	file.write(jsonResult)
	file.close()
	print(5)

dummy = 0

spi = spidev.SpiDev()
spi.open(0,0)			#/sys/bus/spi/devices/dev0.0を使う
spi.mode = 0x03			#モード3 CPOL:1 CPHA:1 ,Especially CPHA must be 1
spi.max_speed_hz = 1000000	#最大クロック周波数

args = sys.argv
if len(args)==2:
	if args[1] == "reset":
		#FAULTピンのリセット
		resp = spi.xfer2([0x80,0x17])
		sleep(1)

try:
	while True:
		#通常計測
		#xfer2はcsを下げたまま
		#xferは1バイトごとにcsを下げ上げする
		resp = spi.xfer2([0x80,0x55,0x35,0x00,0x3C,0xF6,0x57,0x80,0xFE,0xC0,0x00])	#設定と同時に計測するのでCR0の第6ビットを立てる
		sleep(1)			#計測を待つ


		#Faultの検知
		resp = spi.xfer([0x0f,dummy])
		if (resp[1] & 0xFF) != 0:
			valueFlt = resp[1]
			valueHJ = ""
			valueCJ = ""
			fwrite(valueFlt,valueHJ,valueCJ)
			print(resp)
			break
		else:

			valueFlt = resp[1]

			#熱電対の温度を読み込み
			resp = spi.xfer2([0x0C,0x0D,0x0E,dummy])
			valueHJ = resp[1] * 256 + resp[2]
			if (resp[1] & 0x80) != 0:
				valueHJ = -1 * (~(valueHJ - 1) & 0x7FFF)	#2の補数の10進数化

			#冷接点の温度を読み込み
			resp = spi.xfer2([0x0A,0x0B,dummy])
			valueCJ = (resp[1] << 6)  + (resp[2] >> 2)
			if (resp[1] & 0x80) != 0:
				valueCJ = -1 * (~(valueCJ - 1) & 0x7FFF)	#2の補数の10進数化

			fwrite(valueFlt,valueHJ,valueCJ)
			print(6)
except KeyboardInterrupt:
	pass
finally:
	spi.close()
