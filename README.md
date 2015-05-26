CH340G bitbanging
=================

I just wanted to set a pin low or high on a USB-serial adaptor.

This could be used to:

* blink a LED
* power on/off a relay

Picture
=======

![WinChipHead CH340G usb-serial adaptor](https://raw.githubusercontent.com/zoobab/ch340g-bitbanging/master/ch340g-usb-serial.jpg)

Pinout
======

The RTS pin14, the pin1 is marked with the little round on the top head corner.

![WinChipHead CH340G pinout](https://raw.githubusercontent.com/zoobab/ch340g-bitbanging/master/ch340g-pinout.jpg)

Price
=====

You can get those adaptors by a pack of 10 for 10EUR via Aliexpress.com.

Usage
=====

You can set the RTS pin of the CH340G low (0V) or high (3.7V) with this simple script.

In the future, those CTS/RTS/DCD/CI pins could be used as GPIOs in sysfs or via
libusb, which pyserial probably uses.

Speed
=====

When I set 100K permutations, the execution time is around 35secs:

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

Which makes a speed of about 2.8KHz, which is very similar to the RaspberryPi sysfs shell speed.

Links
=====

* Datasheet and basic circuit: http://fobit.blogspot.be/2014/11/ch340g-in-eagle.html
* RaspberryPi gpio bitbanging speed: http://codeandlife.com/2012/07/03/benchmarking-raspberry-pi-gpio-speed/
* Avrdude ch340g avr flasher: http://arduino.densikit.com/jikken-shitsu/ch340g
