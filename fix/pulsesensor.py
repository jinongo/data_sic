from gpiozero import MCP3008
import time

# Connect the Pulse Sensor's signal pin to the MCP3008 channel
pulse_sensor = MCP3008(channel=0)  # Use the appropriate channel number

def calculate_bpm(pulse_values, interval):
    # Count the number of times the sensor value crosses a certain threshold
    threshold = 0.5  # Adjust this threshold based on your sensor's characteristi>
    crossings = sum(1 for prev, curr in zip(pulse_values, pulse_values[1:]) if pr>
    
    # Calculate beats per minute
    bpm = (crossings / interval) * 60
    return bpm

def read_pulse():
    pulse_values = []
    start_time = time.time()
    
    while True:
        sensor_value = pulse_sensor.value
        pulse_values.append(sensor_value)

        # Keep only the last few values for calculation
        max_values_to_keep = 10
        pulse_values = pulse_values[-max_values_to_keep:]

        elapsed_time = time.time() - start_time
        if elapsed_time >= 1:  # Calculate BPM every 5 seconds
            bpm = calculate_bpm(pulse_values, elapsed_time)
            print("Heart Rate (BPM):", bpm)
            start_time = time.time()

        time.sleep(1)  # Adjust the delay as needed

try:
    read_pulse()
except KeyboardInterrupt:
    pass

