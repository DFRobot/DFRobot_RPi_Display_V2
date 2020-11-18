# -*- coding:utf-8 -*-

import spidev

class SPI:

  MODE_1 = 1
  MODE_2 = 2
  MODE_3 = 3
  MODE_4 = 4

  def __init__(self, bus, dev, speed = 3900000, mode = MODE_4):
    self._bus = spidev.SpiDev()
    self._bus.open(0, 0)
    self._bus.no_cs = True
    self._bus.max_speed_hz = speed
    self._bus.threewire  = True

  def transfer(self, buf):
    if len(buf):
      return self._bus.writebytes(buf)
    return []
  def readData(self, cmd):
    return self._bus.readbytes(cmd)
    #return  0
    