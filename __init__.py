#!/usr/bin/env python


class DECODER:

	_OUT_DECODER_PINS = [1, 2, 3, 4, 5, 6, 7, 8]
	_IN_DECODER_PINS = []

	''' function: setup
	    description: setups necessary variables for the 
	    DECODER GPIO driver.
	    
	    inputs: RPi pin1, RPi pin2, RPi pin3 
	'''
	def setup(pin1, pin2, pin3):
		_IN_DECODER_PINS[1] = pin1
		_IN_DECODER_PINS[2] = pin2
		_IN_DECODER_PINS[3] = pin3
		

	def on(decoder):
		return 'test'






#DECODER.on(_OUT_DECODER_PIN)
#DECODER.off(_OUT_DECODER_PIN)
#DECODER.setup(_OUT_DECODER_PIN, _OUT_DECODER_PIN, _OUT_DECODER_PIN)



