'''

'''
from __future__ import print_function
import time
from grovepi import *

#LED = 4
SampleCount = 20
Sample = []

for i in range(SampleCount):
	Sample.append(analogRead(0))
	time.sleep(0.001)
#	digitalWrite(LED, 1)
#	digitalWrite(LED, 0)

#print(Sample)
print(sum(Sample), end="")
#print(sum(Sample)/SampleCount)
