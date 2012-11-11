import serial
'''
def scan():
   # scan for available ports. return a list of tuples (num, name)
   available = []
   for i in range(256):
       try:
           s = serial.Serial(i)
           available.append( (i, s.portstr))
           s.close()
       except serial.SerialException:
           pass
   return available
 
print ("Found ports:")
for n,s in scan():
	print ("(", n, ") " + s)
'''    
ser = serial.Serial('COM5', 115200, timeout=1)

x = ser.write(b'!')          # read one byte
#s = ser.read(10)        # read up to ten bytes (timeout)
s = ser.readline()
#line = ser.readline()   # read a '\n' terminated line
ser.close()

print(s)