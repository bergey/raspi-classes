import spidev
import time

adc = spidev.SpiDev()
adc.open(0,0)

def readadc(channel):
  r = adc.xfer2([1, (8+channel)<<4, 0])
  adcout = ((r[1]&3) << 8) + r[2]
  return adcout

while True:
  print(readadc(0))
  time.sleep(1)
