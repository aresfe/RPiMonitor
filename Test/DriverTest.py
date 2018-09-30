#!/usr/bin/python
# -*- coding:utf-8 -*-


from Driver.ILCDDriver import *
import time

if __name__ == '__main__':
    dr = get_driver(DriverType.LCD1602A)
    dr.init()
    dr.set_backlight(True)
    dr.set_message("Hello World!")
    time.sleep(5)
    dr.msg_blink(True)
    dr.msg_move_left(3)
    time.sleep(5)
    dr.set_backlight(False)
    dr.set_led_off()
