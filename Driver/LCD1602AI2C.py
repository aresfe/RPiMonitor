import time
import threading
import enum
import Adafruit_CharLCD as LCD

from ILCDDriver import *


class FlashFreq(enum.Enum):
    FAST = 0.05
    NORM = 0.5
    SLOW = 1


class LED:
    def __init__(self, driver):
        self._driver = driver
        self._color = (0, 0, 0)

    def red(self):
        self._color = (1, 0, 0)
        self._driver.set_led_color(*self._color)

    def blue(self):
        self._color = (0, 0, 1)
        self._driver.set_led_color(*self._color)

    def green(self):
        self._color = (0, 1, 0)
        self._driver.set_led_color(*self._color)

    def yellow(self):
        self._color = (1, 1, 0)
        self._driver.set_led_color(*self._color)

    def purple(self):
        self._color = (0, 1, 1)
        self._driver.set_led_color(*self._color)

    def cyan(self):
        self._color = (1, 0, 1)
        self._driver.set_led_color(*self._color)

    def white(self):
        self._color = (1, 1, 1)
        self._driver.set_led_color(*self._color)

    def on(self):
        self._driver.set_led_color(*self._color)

    def off(self):
        self._driver.set_led_color(0, 0, 0)

    def color(self):
        return self._color

    def switch(self):
        if self._driver.get_led_color() == (0, 0, 0):
            self.on()
        else:
            self.off()

    @staticmethod
    def _doflash(driver, interval, count):
        if count > 0:
            driver.switch()
            time.sleep(interval)
            driver.flash(interval, count - 1)
        else:
            driver.off()

    def flash(self, interval=0.1, count=20):
        t = threading.Thread(target=LED._doflash, args=(self, interval, count))
        t.start()

    def flashEx(self, freq, timelength):
        self.flash(freq.value, timelength / freq.value)


class LCD1602A(LCDDriver):
    def __init__(self):
        self.led = LED(self)
        self._color = (1, 1, 1)

    def init(self):
        self._lcd = LCD.Adafruit_CharLCDPlate()

    def switch_backlight(self, on):
        self._lcd.set_backlight(on if 1 else 0)

    def switch_cursor(self, on):
        self._lcd.show_cursor(on)

    def switch_display(self, on):
        self._lcd.enable_display(on)

    def set_led_off(self):
        self._color = (0, 0, 0)
        self._lcd.set_color(0, 0, 0)

    def set_led_color(self, red, green, blue):
        self._color = (red, green, blue)
        self._lcd.set_color(red, green, blue)

    def get_led_color(self):
        return self._color

    def set_cfg_autoscroll(self, on):
        self._lcd.autoscroll(on)

    def set_cfg_blink(self, on):
        self._lcd.blink(on)

    def set_cursor_pos(self, row, col):
        self._lcd.set_cursor(col, row)

    def set_message(self, message):
        self._lcd.message(message)

    def msg_move_left(self, count=1):
        while count:
            self._lcd.move_left()
            count -= 1

    def msg_move_right(self, count=1):
        while count:
            self._lcd.move_right()
            count -= 1

    def clear(self):
        self._lcd.clear()


if __name__ == '__main__':
    print("start test")
    dr = LCD1602A()
    dr.init()
    dr.switch_display(True)
    dr.switch_backlight(True)
    dr.set_led_off()

    dr.led.white()
    """
    dr.led.flashEx(FLASHFREQ.FLASH_NORM, 5)
    dr.set_cfg_autoscroll(True)
    dr.set_message("Hello World! Here is Raspberry Pi~~~~")
    time.sleep(5)
    dr.set_cfg_autoscroll(True)
    dr.set_message("Hello World! Here is Raspberry Pi~~~~")
    dr.switch_cursor(True)
    time.sleep(5)
    dr.set_cfg_blink(True)
    dr.msg_move_left(3)
    """
    time.sleep(5)
    dr.switch_backlight(False)
    dr.set_led_off()
    dr.switch_display(False)
