#!/usr/bin/python
# -*- coding:utf-8 -*-
# for easy testing on stand-alone


from Driver.ILCDDriver import LCDDriver


class ConsoleTest(LCDDriver):
    def __init__(self):
        super.__init__()
