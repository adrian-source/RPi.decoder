This driver is n extenton of the RPi GPIO driver. It is reqired for the DECODER driver to work.

Purpose: In order to conserve GPIOs on your Raspberry Pi, your application may allow you to use a decoder. 

Example:

          Raspberry Pi               3 to 8 decoder            8 Relay Module
      +---------------------+                                +----------------+
      |                     |                                |                |
      |                     |                                |              +---->
      |                     |                                |                |
      |                GPIOs|                                |              +---->
      |                  .. |           +--+                 |                |
      |                  .+------------>|  |+--------------->|              +---->
      |                  .+------------>|  |+--------------->|                |
      |                  .+------------>|  |+--------------->|              +---->
      |                  .. |           |  |+--------------->|                |
      |                  .. |           |  |+--------------->|              +---->
      |                  .. |           |  |+--------------->|                |
      |                  .. |           |  |+--------------->|              +---->
      |                  .. |           |  |+--------------->|                |
      |                     |           +--+                 |              +---->
      |                     |                                |                |
      |                     |                                |              +---->
      |                     |                                |                |
      +---------------------+                                |                |
                                                             +----------------+
                                                             
Example setup routine:

import RPi.DECODER as DECODER
in_pins =       [7, 10, 12]     # these are the pins that you are using on your RPi

                                # this is the map translating pin configuration to each relay
input_dict = [
                [ 0, 0, 0],     # relay 1
                [ 1, 0, 0],     # relay 2
                [ 0, 1, 0],     # relay 3
                [ 1, 1, 0],     # relay 4
                [ 0, 0, 1],     # relay 5
                [ 1, 0, 1],     # relay 6
                [ 0, 1, 1],     # relay 7
                [ 1, 1, 1]]     # all off  #state that turns all relays off (relay 8 is unused for that reason)

DECODER.setup(in_pins, input_dict)

DECODER.on(3)      # turns on relay 3
DECODER.all_off()  # executes the off state
