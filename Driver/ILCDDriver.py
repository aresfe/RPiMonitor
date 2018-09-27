#!/usr/bin/python
# -*- coding:utf-8 -*-
# interface of LCD drivers


class ILCDDriver:
    def __init__(self):
        pass

    def show_message(self, msg):
        pass

    # turn backlight on/off
    def set_backlight(self, on):
        pass
