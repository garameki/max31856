# max31856  
Using Adafruit max31856 module  
  
  
for	R type heat-couple  only
  
execute : $ python3 max31856.py  
  
Return value is dictionary type  
{  
	FAULT	: indicates what kind of fault in each bits  
	HJ	: Hot-Junction Temperature : This value must be multiplied by 0.0625 to make itself cercius digree  
	CJ	: Cold-Junction Temperature : This value must be multiplied by 0.015625 to make itself cercius digree   
}  

おいておくフォルダ  
==================  
	~/src/spi/max31856/の中
  
使われている場所  
================
	~/src/websocket/client-max31856/の中  
  
