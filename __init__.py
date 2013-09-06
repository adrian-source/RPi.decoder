#!/usr/bin/env python
import RPi.GPIO as GPIO
            
class InvalidRelayNumberException(Exception):
	"""The relay number provided doesn't exist in the relay input_dict list"""
	pass

class InvalidDecoderSetupParametersException(Exception):
	"""Number of in_pins doesn't match size of input_dict"""
	pass
        
        _IN_PINS = 0
        _INPUT_DICT = 0
                
 ''' function: setup
     description: setups necessary variables for the
     DECODER GPIO driver.
 '''
 def setup(in_pins, input_dict):
 	
 	#validate input
 	if len(in_pins) == 0:
 		raise InvalidDecoderSetupException
 	for relay in range(0, len(input_dict)):
 		if len(in_pins) != len(input_dict[relay]):
 			raise InvalidDecoderSetupException
 	
	_IN_PINS = in_pins
        _INPUT_DICT = input_dict
		
	#configure in pins as outputs
	for pin in _IN_PINS:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)
		
	#turn all relays off
	allOff()

''' function: all_off
    description: use the 'off' configuration to turn
    all relays off
'''
def all_off():
	for pin in range(0, 3):
		GPIO.output(_IN_PINS[pin], _INPUT_DICT[len(_INPUT_DICT)][pin])
		
''' function: on
    description: turns off all relays and then turns 
    on the desired one
'''
def on(relay):
	#validate input
	if (relay > len(_INPUT_DICT) - 1):
		throw InvalidRelayNumberException
		
	all_off()
	for pin in range(0, 3):
		GPIO.output(_IN_PINS[pin], _INPUT_DICT[relay][pin])

