#!/usr/bin/python
"""
 * dial.py
 * 
 * Created on: 1 Nov 2010
 * Author:     Duncan Law
 *
 * Modified by: Ted Carancho
 * For compatibility with Python 3.3, PyQt and integration into AeroQuad
 * 
 *      Copyright (C) 2010 Duncan Law
 *      This program is free software; you can redistribute it and/or modify
 *      it under the terms of the GNU General Public License as published by
 *      the Free Software Foundation; either version 2 of the License, or
 *      (at your option) any later version.
 *
 *      This program is distributed in the hope that it will be useful,
 *      but WITHOUT ANY WARRANTY; without even the implied warranty of
 *      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *      GNU General Public License for more details.
 *
 *      You should have received a copy of the GNU General Public License
 *      along with this program; if not, write to the Free Software
 *      Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 *      Thanks to Chootair at http://www.codeproject.com/Members/Chootair 
 *      for the inspiration and the artwork that i based this code on.
 *      His full work is intended for C# and can be found here:
 *      http://www.codeproject.com/KB/miscctrl/Avionic_Instruments.aspx

 * Requires pySerial and pyGame to run.
 * http://pyserial.sourceforge.net
 * http://www.pygame.org

"""

import math
import serial
import pygame
from pygame.locals import *
pygame.init()
import sys

class Dial:
   """
   Generic dial type.
   """
   def __init__(self, image, frameImage, x=0, y=0, w=0, h=0):
       """
       x,y = coordinates of top left of dial.
       w,h = Width and Height of dial.
       """
       self.x = x 
       self.y = y
       self.image = image
       self.frameImage = frameImage
       # Not compatibile with Python 3.3
       #self.dial = pygame.Surface(self.frameImage.get_rect()[2:4])
       self.width = self.frameImage.get_rect()[2]
       self.height = self.frameImage.get_rect()[3]
       self.dial = pygame.Surface((int(self.width), int(self.height)))
       self.dial.fill(0xFFFF00)
       if(w==0):
          w = self.frameImage.get_rect()[2]
       if(h==0):
          h = self.frameImage.get_rect()[3]
       self.w = w
       self.h = h
       self.pos = self.dial.get_rect()
       self.pos = self.pos.move(x, y)

   def position(self, x, y):
       """
       Reposition top,left of dial at x,y.
       """
       self.x = x 
       self.y = y
       self.pos[0] = x 
       self.pos[1] = y 

   def position_center(self, x, y):
       """
       Reposition centre of dial at x,y.
       """
       self.x = x
       self.y = y
       self.pos[0] = x - self.pos[2]/2
       self.pos[1] = y - self.pos[3]/2

   def rotate(self, image, angle):
       """
       Rotate supplied image by "angle" degrees.
       This rotates round the centre of the image. 
       If you need to offset the centre, resize the image using self.clip.
       This is used to rotate dial needles and probably doesn't need to be used externally.
       """
       tmpImage = pygame.transform.rotate(image ,angle)
       imageCentreX = tmpImage.get_rect()[0] + tmpImage.get_rect()[2]/2
       imageCentreY = tmpImage.get_rect()[1] + tmpImage.get_rect()[3]/2

       targetWidth = tmpImage.get_rect()[2]
       targetHeight = tmpImage.get_rect()[3]

       imageOut = pygame.Surface((targetWidth, targetHeight))
       imageOut.fill(0xFFFF00)
       imageOut.set_colorkey(0xFFFF00)
       imageOut.blit(tmpImage,(0,0), pygame.Rect( imageCentreX-targetWidth/2,imageCentreY-targetHeight/2, targetWidth, targetHeight ) )
       return imageOut

   def clip(self, image, x=0, y=0, w=0, h=0, oX=0, oY=0):
       """
       Cuts out a part of the needle image at x,y position to the correct size (w,h).
       This is put on to "imageOut" at an offset of oX,oY if required.
       This is used to centre dial needles and probably doesn't need to be used externally.       
       """
       if(w==0):
           w = image.get_rect()[2]
       if(h==0):
           h = image.get_rect()[3]
       needleW = w + 2*math.sqrt(oX*oX)
       needleH = h + 2*math.sqrt(oY*oY)
       imageOut = pygame.Surface((needleW, needleH))
       imageOut.fill(0xFFFF00)
       imageOut.set_colorkey(0xFFFF00)
       imageOut.blit(image, (needleW/2-w/2+oX, needleH/2-h/2+oY), pygame.Rect(x,y,w,h))
       return imageOut

   def overlay(self, image, x, y, r=0):
       """
       Overlays one image on top of another using 0xFFFF00 (Yellow) as the overlay colour.
       """
       x -= (image.get_rect()[2] - self.dial.get_rect()[2])/2
       y -= (image.get_rect()[3] - self.dial.get_rect()[3])/2
       image.set_colorkey(0xFFFF00)
       self.dial.blit(image, (x,y))

class Horizon(Dial):
   """
   Artificial horizon dial.
   """
   def __init__(self, x=0, y=0, w=0, h=0):
       """
       Initialise dial at x,y.
       Default size of 300px can be overidden using w,h.
       """
       self.image = pygame.image.load('resources/Horizon_GroundSkyAQ.png').convert()
       #self.image = pygame.image.load('resources/AH.jpg').convert()
       self.frameImage = pygame.image.load('resources/Horizon_Background.png').convert()
       self.maquetteImage = pygame.image.load('resources/Maquette_Avion.png').convert()
       Dial.__init__(self, self.image, self.frameImage, x, y, w, h)
   def update(self, screen, angleX, angleY):
       """
       Called to update an Artificial horizon dial.
       "angleX" and "angleY" are the inputs.
       "screen" is the surface to draw the dial on.
       """
       angleX %= 360
       angleY %= 360
       if (angleX > 180):
           angleX -= 360 
       if (angleY > 90)and(angleY < 270):
           angleY = 180 - angleY 
       elif (angleY > 270):
           angleY -= 360
       tmpImage = self.clip(self.image, 0, (59-angleY)*720/180, 250, 250)
       tmpImage = self.rotate(tmpImage, angleX)
       self.overlay(tmpImage, 0, 0)
       self.overlay(self.frameImage, 0,0)
       self.overlay(self.maquetteImage, 0,0)
       self.dial.set_colorkey(0xFFFF00)
       screen.blit( pygame.transform.scale(self.dial,(self.w,self.h)), self.pos )

class TurnCoord(Dial):
   """
   Turn Coordinator dial.
   """
   def __init__(self, x=0, y=0, w=0, h=0):
       """
       Initialise dial at x,y.
       Default size of 300px can be overidden using w,h.
       """
       self.image = pygame.image.load('resources/TurnCoordinatorAircraft.png').convert()
       self.frameImage = pygame.image.load('resources/TurnCoordinator_Background.png').convert()
       self.marks = pygame.image.load('resources/TurnCoordinatorMarks.png').convert()
       self.ball = pygame.image.load('resources/TurnCoordinatorBall.png').convert()
       Dial.__init__(self, self.image, self.frameImage, x, y, w, h)
   def update(self, screen, angleX, angleY):
       """
       Called to update a Turn Coordinator dial.
       "angleX" and "angleY" are the inputs.
       "screen" is the surface to draw the dial on.       
       """
       angleX %= 360 
       angleY %= 360
       if (angleX > 180):
           angleX -= 360 
       if (angleY > 180):
           angleY -= 360
       if(angleY > 14): 
           angleY = 14
       if(angleY < -14): 
           angleY = -14
       tmpImage = self.clip(self.image, 0, 0, 0, 0, 0, -12)
       tmpImage = self.rotate(tmpImage, angleX)
       self.overlay(self.frameImage, 0,0)
       self.overlay(tmpImage, 0, 0)
       tmpImage = self.clip(self.marks, 0, 0, 0, 0, 0, 0)
       self.overlay(tmpImage, 0, 80)
       tmpImage = self.clip(self.ball, 0, 0, 0, 0, 0, 300)
       tmpImage = self.rotate(tmpImage, angleY)
       self.overlay(tmpImage, 0, -220)
       self.dial.set_colorkey(0xFFFF00)
       screen.blit( pygame.transform.scale(self.dial,(self.w,self.h)), self.pos )

class Generic(Dial):
   """
   Generic Dial. This is built on by other dials.
   """
   def __init__(self, x=0, y=0, w=0, h=0):
       """
       Initialise dial at x,y.
       Default size of 300px can be overidden using w,h.       
       """
       self.image = pygame.image.load('resources/AirSpeedNeedle.png').convert()
       self.frameImage = pygame.image.load('resources/Indicator_Background.png').convert()
       Dial.__init__(self, self.image, self.frameImage, x, y, w, h)
   def update(self, screen, angleX, iconLayer=0):
       """
       Called to update a Generic dial.
       "angleX" and "angleY" are the inputs.
       "screen" is the surface to draw the dial on.       
       """
       angleX %= 360
       angleX = 360 - angleX
       tmpImage = self.clip(self.image, 0, 0, 0, 0, 0, -35)
       tmpImage = self.rotate(tmpImage, angleX)
       self.overlay(self.frameImage, 0,0)
       if iconLayer:
          self.overlay(iconLayer[0],iconLayer[1],iconLayer[2])
       self.overlay(tmpImage, 0, 0)
       self.dial.set_colorkey(0xFFFF00)
       screen.blit( pygame.transform.scale(self.dial,(self.w,self.h)), self.pos )

class Battery(Generic):
   """
   Battery dial.
   """
   def __init__(self, x=0, y=0, w=0, h=0):
       """
       Initialise dial at x,y.
       Default size of 300px can be overidden using w,h.
       """
       self.icon = pygame.image.load('resources/battery2.png').convert()
       Generic.__init__(self, x, y, w, h)
       self.frameImage = pygame.image.load('resources/ledgend.png').convert()
   def update(self, screen, angleX):
       """
       Called to update a Battery dial.
       "angleX" is the input.
       "screen" is the surface to draw the dial on.       
       """
       if angleX > 100:
          angleX = 100
       elif angleX < 0:
          angleX = 0
       angleX *= 2.7
       angleX -= 135
       Generic.update(self, screen, angleX, (self.icon, 0, 100))

class RfSignal(Generic):
   """
   RF Signal dial.
   """
   def __init__(self, x=0, y=0, w=0, h=0):
       """
       Initialise dial at x,y.
       Default size of 300px can be overidden using w,h.
       """
       self.image = pygame.Surface((0,0))
       self.frameImage = pygame.image.load('resources/RF_Dial_Background.png').convert()
       Dial.__init__(self, self.image, self.frameImage, x, y, w, h)
   def update(self, screen, inputA, inputB, scanPos):
       """
       "screen" is the surface to draw the dial on.       
       """

       top = self.dial.get_rect()[0] +60
       left = self.dial.get_rect()[1] +30
       bottom = self.dial.get_rect()[0] + self.dial.get_rect()[2] -60
       right = self.dial.get_rect()[1] + self.dial.get_rect()[3] -30
       height = bottom - top
       middle = height/2 + top

       scanPos %= right -30
       scanPos += 30
       inputA %= 100
       inputB %= 100
       inputA = height * inputA / 200
       inputB = height * inputB / 200

       pygame.draw.line(self.dial, 0xFFFFFF, (scanPos,top), (scanPos,bottom), 1)
       pygame.draw.line(self.dial, 0x222222, (scanPos-1,top), (scanPos-1,bottom), 1)

       pygame.draw.line(self.dial, 0x00FFFF, (scanPos-1,middle-inputA), (scanPos-1,middle),4)
       pygame.draw.line(self.dial, 0xFF00FF, (scanPos-1,bottom-inputB), (scanPos-1,bottom),4)
       pygame.draw.line(self.dial, 0xFFFF00, (scanPos-1,middle), (scanPos-1,middle))

       self.overlay(self.frameImage, 0,0)

       self.dial.set_colorkey(0xFFFF00)
       screen.blit( pygame.transform.scale(self.dial,(self.w,self.h)), self.pos )

class TxSerial:
   """
   Wrapper round pyserial.
   """
   def __init__(self, port, baud, testing=0):
      """
      Open serial port if possible.
      Exit program if not.
      "testing" = 1 prevents the program teminating if valid serial port is not found.
      """
      self.testing = testing
      try:
         self.serial = serial.Serial(port, baud, timeout=1)
      except serial.SerialException:
         print (serialPort + " not found.")
         print
         print ("Usage: " + sys.argv[0] + " [SERIAL_DEVICE]")
         print (" Opens SERIAL_DEVICE and lisens for telemitery data.")
         print (" If SERIAL_DEVICE not specified, /dev/ttyUSB0 will be tried.")
         print ("Usage: " + sys.argv[0] + " test")
         print (" Uses dummy data for testing purposes.")
         print
         if (not testing):
            sys.exit()

   def readline(self):
      """
      Returns data from serial port 
      or dummy data if "testing"=1.
      """
      if (not self.testing):
          line = self.serial.readline()
      else:
          line = ''
      rf_data = 0
      if (len(line)==35):
         rf_data = {'RX_RSSI':int(line[1:3],16), 'RX_fr_sucsess':int(line[4:6],16), \
                    'RX_fr_con_err':int(line[7:9],16), 'RX_batt_volt':int(line[10:12],16), \
                    'RX_batt_cur':int(line[13:15],16), 'TX_batt_volt':int(line[16:18],16), \
                    'TX_fr_sucsess':int(line[19:21],16), 'RX_accel_x':int(line[22:24],16), \
                    'RX_accel_y':int(line[25:27],16), 'RX_est_x':int(line[28:30],16), \
                    'RX_est_y':int(line[31:33],16)}
      elif (self.testing):
         # dummy testing data
         rf_data = {'RX_RSSI':0, 'RX_fr_sucsess':0, 'RX_fr_con_err':0, 'RX_batt_volt':0, \
                    'RX_batt_cur':0, 'TX_batt_volt':0, 'TX_fr_sucsess':0, 'RX_accel_x':0, \
                    'RX_accel_y':0, 'RX_est_x':0, 'RX_est_y':0}
      return rf_data
   def close(self):
      """
      Close serial port.
      """
      if((not self.testing) and self.serial.isOpen()):
         self.serial.close()      # close serial port.

serialPort = '/dev/ttyUSB0'
baud = 115200

if (len(sys.argv) == 1):
    # No options used at run time. Presume serial port is "dev/ttyUSB0"
    test = 0
    serialPort = '/dev/ttyUSB0'
elif (sys.argv[1] == 'test'):
    # Option "test" was selected. Run in test mode. (Dummy data used.)
    test = 1
else:
    # An option other that "test" was enterd. Maybe it's the Serial port.
    test = 0
    serialPort = sys.argv[1]

# Initialise Serial port.
ser = TxSerial(serialPort, baud, test)

# Initialise screen.
screen = pygame.display.set_mode((640, 480))
screen.fill(0x222222)
   
# Initialise Dials.
horizon = Horizon(0,0)
#turn = TurnCoord(20,180,150,150)
#throttle = Generic(470,255,75,75)
#RXbattery = Battery(470,180,75,75)
#TXbattery = Battery(545,180,75,75)
TXbattery = Battery(300,0, 150, 150)
rfSignal = RfSignal(300,150,150,150)


a=0
pygame.display.set_mode((600,300))
while 1:
   # Main program loop.
   for event in pygame.event.get():
       if event.type == QUIT:
           print ("Exiting....")
           ser.close()	# close serial port.
           sys.exit()   # end program.

   if(test):
      # Use dummy test data
      curPos = pygame.mouse.get_pos()
      rf_data = {'RX_RSSI':0, 'RX_fr_sucsess':0, 'RX_fr_con_err':0, 'RX_batt_volt':0, \
                 'RX_batt_cur':0, 'TX_batt_volt':0, 'TX_fr_sucsess':0, 'RX_accel_x':a, \
                 'RX_accel_y':0, 'RX_est_x':curPos[0]/2, 'RX_est_y':curPos[1]/2}
      pygame.time.delay(100)
   else: 
      # Get real data from USB port.
      rf_data = ser.readline()
      rf_data = ser.readline()

   if(rf_data):
      # We have data.
      #print (rf_data)
      a+=1

      # Update dials.
      horizon.update(screen, 127 - rf_data['RX_est_x'], 127 - rf_data['RX_est_y'] )
      #turn.update(screen, (rf_data['RX_est_x'] - 127)/2, (127 - rf_data['RX_accel_x'])/4)
      #throttle.update(screen, rf_data['RX_batt_cur'])
      #RXbattery.update(screen, (rf_data['RX_batt_volt'] - 115))
      TXbattery.update(screen, 12.5*(rf_data['TX_batt_volt'] - 105))
      rfSignal.update(screen, rf_data['RX_fr_sucsess'], rf_data['TX_fr_sucsess'],a)

      pygame.display.update()
   elif not ser.testing:
      # We do not have any data to display.
      print (" * No data received. Is the transmitter powered on?")
      print (" * Restartinging " + serialPort + ".\n")
      ser = TxSerial(serialPort, baud)



