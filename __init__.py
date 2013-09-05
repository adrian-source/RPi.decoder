#!/usr/bin/env python


class DECODER:

	_PINS_OUT = 0
	_PINS_IN = 0

	''' function: setup
	    description: setups necessary variables for the 
	    DECODER GPIO driver.
	    
	    inputs: RPi pin1, RPi pin2, RPi pin3 
	'''
	def setup(pins_in, num_out):
		_PINS_IN = pins_in
		_PINS_OUT = range(1, num_out+1)
		

	def on(decoder):
		return 'test'






#DECODER.on(_OUT_DECODER_PIN)
#DECODER.off(_OUT_DECODER_PIN)
#DECODER.setup(_OUT_DECODER_PIN, _OUT_DECODER_PIN, _OUT_DECODER_PIN)



