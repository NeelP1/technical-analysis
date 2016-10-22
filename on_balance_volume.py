import numpy
import talib

close = numpy.random.normal(10,2,10)
volume = numpy.random.normal(10000,2000,10)

print close
print volume

output = talib.OBV(close, volume)
print output
