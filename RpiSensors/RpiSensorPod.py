'''
Created on Jul 12, 2014

@author: ak
'''
from automation.Pytoserver import PytoServer
import RPIO
from automation.MotionSensor import MotionSensor
import atexit
from datetime import datetime
class RpiSensorPod(object):
    
    def __init__(self,url,user,password, sensors):
        self.motionSensors = {}
        self.server = PytoServer(url,user,password)
        
        RPIO.setmode(RPIO.BCM)
        for sensor in sensors:
            print("Number of sensors = " + str(len(sensors)))
            print ("adding callback to sensor : %s %s %s" % (sensor.gpioPin, sensor.ID, sensor.debounce))
            self.motionSensors[sensor.gpioPin] = sensor.ID
            self.initGPIO(sensor)
            
    def sensorCallback(self,gpio_id,val):
            #print ("callback %s %s" % (gpio_id,val) );
            print datetime.now().time()
            if val==1:
                self.server.motion(self.motionSensors[gpio_id])
            else:
                self.server.still(self.motionSensors[gpio_id])
                
    def initGPIO(self,sensor):
        print ("adding callback to sensor : %s %s %s" % (sensor.gpioPin, sensor.ID, sensor.debounce))
        RPIO.add_interrupt_callback(sensor.gpioPin, self.sensorCallback, edge="both", pull_up_down=RPIO.PUD_OFF, threaded_callback=True, debounce_timeout_ms=sensor.debounce)
def clean():
    print ("Cleaning interrupts")
    RPIO.cleanup()
    RPIO.cleanup_interrupts()     

if __name__ == '__main__':
    
    atexit.register(clean)
    
    sensor1 = MotionSensor("Motion9",4,debounce=5)
    sensor2 = MotionSensor("Motion10",17)
    
    sensors = [sensor1,sensor2]
    
    myPod = RpiSensorPod("http://192.168.1.71:8085","admin","funk",sensors)
    
    RPIO.wait_for_interrupts(False)
    
    