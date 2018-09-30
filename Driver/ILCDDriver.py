#!/usr/bin/python
# -*- coding:utf-8 -*-
# interface of LCD drivers
import enum


class DriverType(enum.Enum):
    STANDALONE = 0
    LCD1602A = 1


class LCDDriver:
    def __init__(self):
        pass

    def init(self):
        pass

    def show_message(self, msg):
        pass

    # turn backlight on/off
    def set_backlight(self, on):
        pass

    # @classmethod
    # def get_driver(cls, driver_type):


from LCD1602AI2C import *
from Standalone import *


def get_driver(driver_type):
    if driver_type == DriverType.LCD1602A:
        return LCD1602A()
    else:
        return ConsoleTest()
