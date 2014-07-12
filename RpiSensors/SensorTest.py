import RPIO

def gpio_Callback(gpio_ID,val):
    print ("callback %s %s" % (gpio_ID,val) );


RPIO.setmode(RPIO.BCM)
#RPIO.setup(4,RPIO.IN,pull_up_down=RPIO.PUD_DOWN)

RPIO.add_interrupt_callback(4, gpio_Callback, edge="both", pull_up_down=RPIO.PUD_UP, threaded_callback=True,debounce_timeout_ms=200)
RPIO.wait_for_interrupts()

