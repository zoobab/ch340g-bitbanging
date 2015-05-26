CH340G bitbanging
=================

I just wanted to set a pin low or high on a USB-serial adaptor.

Usage
=====

You can set the RTS pin of the CH340G low (0V) or high (3.7V) with this simple script.

In the future, those CTS/RTS/DCD/CI pins could be used as GPIOs in sysfs or via
libusb, which pyserial probably uses.

Links
=====

* Datasheet and basic circuit: http://fobit.blogspot.be/2014/11/ch340g-in-eagle.html
