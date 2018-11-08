# max31856
Use Adafruit max31856 module with my own setting

STATUS
	R type heat-couple


execute:
$ python3 max31856.py

module:
import max31856.Max31856

to make instance:
ins = Max31856()

Program use the pi device '/sys/bus/spi/devices/dev0.0'.
To use this program you must make spi0.0 opened.

Tutorial(japanese):
http://raspberrypi.garameki.com/articles/max31856.html

Return value is dictionary type
{
	FAULT	: indicates what kind of fault in each bits
	HJ	: Hot-Junction Temperature (must be multiplied by 0.0625) to make itself cercius digree)
	CJ	: Cold-Junction (must be multiplied by 0.015625 to make itself cercius digree)
}
