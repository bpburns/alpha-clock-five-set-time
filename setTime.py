import calendar
from datetime import datetime
import serial

with serial.Serial('COM8', 19200, timeout=1) as ser:
    ser.write('\xffST' + str(calendar.timegm(datetime.now().utctimetuple())))
