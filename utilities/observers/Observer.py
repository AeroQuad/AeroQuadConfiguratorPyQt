'''
Created on Apr 22, 2013

@author: Kenny
'''

class Obeserver(object):
            
    def __init__(self,name=None):
        self.name = name
     
    def method(self,sender,event,msg=None):
        print "[{0}] got event {1} with message {2}".format(self.name,event,msg)
    


        