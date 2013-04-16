'''
Created on 25 mrt. 2013

@author: Lithium
'''
import time
import logging
from PyQt4 import QtCore, QtGui
from subpanel.subPanel import SubPanel
from subpanel.RCchannelsetup.RCchannelsetupWindow import Ui_Form

class RCchannelsetup(QtGui.QWidget, SubPanel):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.start.setEnabled(True)
        self.ui.cancel.setEnabled(False)
        self.ui.cancel.clicked.connect(self.cancel_RC)
        self.ui.start.clicked.connect(self.start_RCsetup)
        self.amount_channels = 5                                                            #The amount of channels
        self.last_RCvalue = [0, 0, 0, 0, 0, 0, 0, 0]                                        #We store the last RC value in this array
        self.first_loop = 80                                                                #We use this to have a stable reading, the first 10 readings we do nothing with the RC values
        self.channelOrderMap = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]   #This array has the channel order the user wants, we never have a RC with 100 channels
        self.channel_detecting = 0                                                          #Here we are going to save on what channel number we are searching at the moment
        self.running = False
        self.channel_offset = 200
        self.max_amount_channels = 12
    
    def start(self, xmlSubPanel, boardConfiguration):
        self.xmlSubPanel = xmlSubPanel
        self.boardConfiguration = boardConfiguration
        
        try:
            self.amount_channels = int(self.boardConfiguration["Receiver Nb Channels"])
        except:
            logging.warning("Can't read amount of channels from boardconfiguration!")
        
        #print("Amount of channels: " + str(self.amount_channels))    
        self.enable_gui_attribute()
    
    def cancel_RC(self):
        self.stop_RCsetup()
        print('Operation canceled by user')
        
    def start_RCsetup(self):
        if not self.running:
            if (self.comm.isConnected()):
                self.running = True
                self.ui.start.setEnabled(False)
                self.ui.cancel.setEnabled(True)
                self.comm.write("t")
                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.readContinuousData)
                self.timer.start(50)
                self.startCommThread()
    
    def stop_RCsetup(self): #We are stopping the setup procedure, reset values send stop command to the quad etc.
        self.comm.write("x")
        self.comm.flushResponse()
#        print("Roll, Pitch, Yaw, throttle, Mode, Aux1, Aux2, Aux3")
#        print(self.channelOrderMap)
        self.channel_detecting = 0;
        self.running = False
        self.change_label(self.channel_detecting)
#        self.channelOrderMap = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        self.ui.start.setEnabled(True)
        self.ui.cancel.setEnabled(False)
        self.first_loop = 80
        self.sendMappedChannel()
        #return
    
    def save_channel(self, channel_number):                                 #Save the channel id to the channelOrderMap array need it later to send it to the quad
        exist = False
        for i in range(0,self.amount_channels):
            if int(self.channelOrderMap[i]) == int(channel_number):               #Look if we want to save a channel number that already has been saved
#                print('Already saved')
                exist = True

        if not exist:                                                          
            self.channelOrderMap[self.channel_detecting] = channel_number               #If the channel number has not been saved yet save it
            self.channel_detecting += 1
#            print('Channel saved')
            
        #return
    
    def readContinuousData(self):
        isConnected = self.comm.isConnected()
        if isConnected and not self.commData.empty():
            string = self.commData.get()
            string_out = string.split(',')
            
            if self.running:
                if self.channel_detecting >= self.amount_channels:                      #If we scanned all channels we can stop
                    print('stop scanning, all channels are set')
                    self.stop_RCsetup()
                else:
                    for i in range(0, self.amount_channels):                                           
                        if int(self.first_loop) > 0:                                 #We want to have some readings before we compare the channel value's                                             
                            self.first_loop -= 1
                            print('First_Loop')
                        else:
                            self.change_label(self.channel_detecting)                        #Now we are compareing the last readed channel value agenst the new one
                            if (int(string_out[i]) - int(self.last_RCvalue[i])) > self.channel_offset:       #Perhaps we need to change the 100 to an variable or something
                                print('Channel id higher: ' + str(i))
                                self.save_channel(i)
                            if (int(string_out[i]) - int(self.last_RCvalue[i])) < -self.channel_offset:    
                                print('Channel id lower: ' + str(i))
                                self.save_channel(i)
                            
                        self.last_RCvalue[i] = string_out[i]                                 #Put the last reading into the variable array                  
                         
                self.ui.commLog.append(self.timeStamp() + " <- " + self.commData.get())
                self.ui.commLog.ensureCursorVisible()

    def change_label(self, label_number): #We want to have the labels updated so we use this function for it
        if self.running:                                            
            if label_number == 0:
                self.ui.label.setText('Roll... Detecting')
            elif label_number == 1:
                self.ui.label.setText('Roll... Done')    
                self.ui.label_2.setText('Pitch... Detecting')
            elif label_number == 2:
                self.ui.label_2.setText('Pitch.. Done')
                self.ui.label_3.setText('Yaw... Detecting')
            elif label_number == 3:
                self.ui.label_3.setText('Yaw... Done')
                self.ui.label_4.setText('Throttle... Detecting')
            elif label_number == 4:
                self.ui.label_4.setText('Throttle... Done')
                self.ui.label_5.setText('Mode... Detecting')
            elif label_number == 5:
                self.ui.label_5.setText('Mode.. Done')
                self.ui.label_6.setText('Aux1... Detecting')
            elif label_number == 6:
                self.ui.label_6.setText('Aux1.. Done')
                self.ui.label_7.setText('Aux2... Detecting')
            elif label_number == 7:
                self.ui.label_7.setText('Aux2.. Done')
                self.ui.label_8.setText('Aux3... Detecting')
            elif label_number == 8:
                self.ui.label_8.setText('Aux3.. Done')
                self.ui.label_9.setText('Aux4... Detecting')
            elif label_number == 9:
                self.ui.label_9.setText('Aux4.. Done')
                self.ui.label_10.setText('Aux5... Detecting')
            elif label_number == 10:
                self.ui.label_10.setText('Aux5.. Done')
                self.ui.label_11.setText('Aux6... Detecting')
            elif label_number == 11:
                self.ui.label_11.setText('Aux6.. Done')
                self.ui.label_12.setText('Aux7... Detecting')
            elif label_number == 12:
                self.ui.label_12.setText('Aux7.. Done')

        else:
            self.ui.label.setText('Roll')
            self.ui.label_2.setText('Pitch')
            self.ui.label_3.setText('Yaw')
            self.ui.label_4.setText('Throttle')
            self.ui.label_5.setText('Mode')
            self.ui.label_6.setText('Aux1')
            self.ui.label_7.setText('Aux2')
            self.ui.label_8.setText('Aux3')
            self.ui.label_9.setText('Aux4')
            self.ui.label_10.setText('Aux5')
            self.ui.label_11.setText('Aux6')
            self.ui.label_12.setText('Aux7')
                                      
    def enable_gui_attribute(self):
        for i in range(0, self.max_amount_channels):
            if i > (self.amount_channels - 1) and i == 5:
                self.ui.label_6.setHidden(True)
            elif i > (self.amount_channels - 1) and i == 6:
                self.ui.label_7.setHidden(True)
            elif i > (self.amount_channels - 1) and i == 7:
                self.ui.label_8.setHidden(True)
            elif i > (self.amount_channels - 1) and i == 8:
                self.ui.label_9.setHidden(True)
            elif i > (self.amount_channels - 1) and i == 9:
                self.ui.label_10.setHidden(True)
            elif i > (self.amount_channels - 1) and i == 10:
                self.ui.label_11.setHidden(True)
            elif i > (self.amount_channels - 1) and i == 11:
                self.ui.label_12.setHidden(True)
              
    def sendMappedChannel(self):
        command = "R "
        for i in range(0, self.amount_channels):
            command += str(self.channelOrderMap[i])
            command += ";"

        print(command)
        self.comm.write(command)
                
            
            
            
            
            
            
            
            
            
            
        