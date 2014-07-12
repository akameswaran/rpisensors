'''
Created on Jul 12, 2014

@author: ak
'''
import RPIO 

class MotionSensor(object):
    '''
    classdocs
    '''



    def __init__(self,id, gpioPin,debounce=100):
        '''
        Constructor
        '''
        self.ID = id
        self.gpioPin = gpioPin
        self.debounce = debounce

        
        