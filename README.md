[![noswpatv3](http://zoobab.wdfiles.com/local--files/start/noupcv3.jpg)](https://ffii.org/donate-now-to-save-europe-from-software-patents-says-ffii/)
[![noswpatv3](http://zoobab.wdfiles.com/local--files/start/noupcv3.jpg)](https://ffii.org/donate-now-to-save-europe-from-software-patents-says-ffii/)
CH340G bitbanging
=================

I just wanted to set a pin low or high on a USB-serial adaptor.

This could be used to:

* blink a LED
* power on/off a relay
* bitbanging a protocol over several pins (avrdude)

Picture
=======

![WinChipHead CH340G usb-serial adaptor](https://raw.githubusercontent.com/zoobab/ch340g-bitbanging/master/ch340g-usb-serial.jpg)

Pinout
======

The RTS pin14, the pin1 is marked with the little round on the top head corner.

The usable pins are:

* RTS = pin14
* DTR = pin13

We note that the Avrdude flasher mentioned below uses the following four pins:

* RTS (RESET)
* DTR (SCK)
* TXD (MOSI)
* CTS (MISO)

![WinChipHead CH340G pinout](https://raw.githubusercontent.com/zoobab/ch340g-bitbanging/master/ch340g-pinout.jpg)

Price
=====

You can get those adaptors by a pack of 10 for 10EUR via Aliexpress.com. Standalone you can find them at 0.88EUR, or just the chip in SOP16 format at around 0.44EUR.

Usage
=====

You can set the RTS pin of the CH340G low (0V) or high (3.7V) with this simple script.

In the future, those CTS/RTS/DCD/CI pins could be used as GPIOs in sysfs or via
libusb, which pyserial probably uses.

Speed
=====

When I set 100K permutations, the execution time is around 35secs:

```
root@sabayon /home/zoobab/soft/ch340g-bitbanging [9]# time ./ch340g-rts.py
real    0m35.066s
user    0m4.004s
sys     0m2.354s

root@sabayon /home/zoobab/soft/ch340g-bitbanging [10]# python
Python 2.7.9 (default, Dec 29 2014, 06:44:46) 
[GCC 4.8.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 100000.0/35.0
2857.1428571428573
```

Which makes a speed of about 2.8KHz, which is very similar to the RaspberryPi sysfs shell speed.

CP2102 dongle
=============

I also have a CP2102 dongle, and the nice feature with this one is that the DTR pin is available on the header:

![Silabs CP2102 usb-serial adaptor breakout](https://raw.githubusercontent.com/zoobab/ch340g-bitbanging/master/cp2102-usb-serial.jpg)

The DTR voltage is different from the CH340G, as it has precise 3.3V or 0V values.

I tried the same on the RTS pin (you need to solder a pin on the nicely exposed hole), and it also has 0V or 3.3V.

![Silabs CP2102 blinking a LED with the DTR pin](https://raw.githubusercontent.com/zoobab/ch340g-bitbanging/master/cp2102-blinkled.jpg)

FTDI UMFT230XB dongle
=====================

This dongle has a nice 10 pins female header:

![FTDI UMFT230XB dongle](https://raw.githubusercontent.com/zoobab/ch340g-bitbanging/master/ftdi-umft230xb.jpg)
![FTDI UMFT230XB blinking a LED with the RTS pin](https://raw.githubusercontent.com/zoobab/ch340g-bitbanging/master/ftdi-umft230xb-blinkled.jpg)

TODO
====

* Rewrite the whole thing in C with libusb in order to remove python dependencies.

Links
=====

* Datasheet and basic circuit: http://fobit.blogspot.be/2014/11/ch340g-in-eagle.html
* RaspberryPi gpio bitbanging speed: http://codeandlife.com/2012/07/03/benchmarking-raspberry-pi-gpio-speed/
* Avrdude ch340g avr flasher: http://web.archive.org/web/20141229024211/http://arduino.densikit.com/jikken-shitsu/ch340g
* USBIO with a PIC18f14k50: http://jap.hu/electronic/usbio.html
* Using the DTR & RTS signal lines as outputs from Liberty BASIC http://www.diga.me.uk/dtrts.html
* PySerial DTR and RTS Manipulation http://projectproto.blogspot.be/2009/11/pyserial-dtr-and-rts-manipulation.html
