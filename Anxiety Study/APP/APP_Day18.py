print("Hello World!")

from Phidget22.Devices.DigitalOutput import *

#Declare any event handlers here. These will be called every time the associated event occurs.

def main():
	#Create your Phidget channels
	digitalOutput0 = DigitalOutput()
	digitalOutput1 = DigitalOutput()
	digitalOutput4 = DigitalOutput()
	digitalOutput5 = DigitalOutput()
	digitalOutput6 = DigitalOutput()
	digitalOutput7 = DigitalOutput()

	#Set addressing parameters to specify which channel to open (if any)
	digitalOutput0.setChannel(0)
	digitalOutput1.setChannel(1)
	digitalOutput4.setChannel(4)
	digitalOutput5.setChannel(5)
	digitalOutput6.setChannel(6)
	digitalOutput7.setChannel(7)

	#Assign any event handlers you need before calling open so that no events are missed.

	#Open your Phidgets and wait for attachment
	digitalOutput0.openWaitForAttachment(5000)
	digitalOutput1.openWaitForAttachment(5000)
	digitalOutput4.openWaitForAttachment(5000)
	digitalOutput5.openWaitForAttachment(5000)
	digitalOutput6.openWaitForAttachment(5000)
	digitalOutput7.openWaitForAttachment(5000)

	#Do stuff with your Phidgets here or in your event handlers.
	digitalOutput0.setDutyCycle(0)
	digitalOutput1.setDutyCycle(0)
	digitalOutput4.setDutyCycle(0)
	digitalOutput5.setDutyCycle(1)
	digitalOutput6.setDutyCycle(0)
	digitalOutput7.setDutyCycle(0)

	# import date and time information
	import time
	from datetime import datetime

	now = datetime.now()

	current_date = now.strftime("%m/%d/%Y")
	current_time = now.strftime("%H:%M:%S")

	# project description and date/time info

	print("""
	Anxiety Study: Classical Conditioning Paradigm

	Condition: APP 
	Day 18: Training (WN u Food x 6)

	Today's date is""", current_date)
	print("Time at beginning of the trial is", current_time)

	time.sleep(360)

	# Event 1

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Event 1: no event; wait interval
	Time at beginning of event:""", current_time)

	time.sleep(30)

	time.sleep(.5)

	# Inter-event interval

	time.sleep(180)

	# Event 2

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Event 2: White noise - food pairing
	Time at beginning of event:""", current_time)

	digitalOutput4.setDutyCycle(1)

	time.sleep(30)

	digitalOutput4.setDutyCycle(0)
	digitalOutput0.setDutyCycle(1)

	time.sleep(.5)

	digitalOutput0.setDutyCycle(0)

	# Inter-event interval

	time.sleep(240)

	# Event 3

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Event 3: white noise - food pairing
	Time at beginning of event:""", current_time)

	digitalOutput4.setDutyCycle(1)

	time.sleep(30)

	digitalOutput4.setDutyCycle(0)
	digitalOutput0.setDutyCycle(1)

	time.sleep(.5)

	digitalOutput0.setDutyCycle(0)

	# Inter-event interval

	time.sleep(240)

	# Event 4

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Event 4: no event; wait interval
	Time at beginning of event:""", current_time)

	time.sleep(30)

	time.sleep(.5)

	# Inter-event interval

	time.sleep(300)

	# Event 5

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Event 5: white noise - food pairing
	Time at beginning of event:""", current_time)

	digitalOutput4.setDutyCycle(1)

	time.sleep(30)

	digitalOutput4.setDutyCycle(0)
	digitalOutput0.setDutyCycle(1)

	time.sleep(.5)

	digitalOutput0.setDutyCycle(0)

	# Inter-event interval

	time.sleep(180)

	# Event 6

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Event 6: White noise - food pairing
	Time at beginning of event:""", current_time)

	digitalOutput4.setDutyCycle(1)

	time.sleep(30)

	digitalOutput4.setDutyCycle(0)
	digitalOutput0.setDutyCycle(1)

	time.sleep(.5)

	digitalOutput0.setDutyCycle(0)

	# Inter-event interval

	time.sleep(180)

	# Event 7

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Event 7: no event; wait interval
	Time at beginning of event:""", current_time)

	digitalOutput4.setDutyCycle(1)

	time.sleep(30)

	digitalOutput4.setDutyCycle(0)
	digitalOutput0.setDutyCycle(1)

	time.sleep(.5)

	digitalOutput0.setDutyCycle(0)

	# Inter-event interval

	time.sleep(240)

	# Event 8

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Event 8: white noise - food pairing
	Time at beginning of event:""", current_time)

	digitalOutput4.setDutyCycle(1)

	time.sleep(30)

	digitalOutput4.setDutyCycle(0)
	digitalOutput0.setDutyCycle(1)

	time.sleep(.5)

	digitalOutput0.setDutyCycle(0)

	# Wait for end of trial

	time.sleep(240)

	# End trial timestamp

	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	print("""
	Time at end of trial:""", current_time)

	# Close your Phidgets once the program is done.
	digitalOutput0.close()
	digitalOutput1.close()
	digitalOutput4.close()
	digitalOutput5.close()
	digitalOutput6.close()
	digitalOutput7.close()


main()