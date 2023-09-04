# -*- coding: utf-8 -*-
from gpiozero import MCP3008
from time import sleep
# from ubilm import build_payload, post_request
# Set up channel number and SPI chip select device
reading = MCP3008(channel=1)

while True:
    # Converts ACD voltage to temperature in Celsius
    temp_c = round((reading.value * 3.3) * 100, 2)

    # Convert Celsius degrees to Farenheit
    temp_f = round(temp_c * 1.8 + 32, 2)

    # Print both temperatures
    print('Temp: {}ºC    {}ºF'.format(temp_c, temp_f))
    sleep(1.5)  # Wait 1.5 seconds for the next read

    