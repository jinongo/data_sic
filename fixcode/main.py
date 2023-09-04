import pulse
import lmmcp
import time
from ubidots import build_payload, post_request
import ubidots

def setup():
    while True:
        reading_value = lmmcp.read_suhu()
        pulse_sensor_value = pulse.kalibrasi()
        print("Reading:", reading_value)
        print("Pulse Sensor:", pulse_sensor_value)

        payload = build_payload(reading_value, pulse_sensor_value)
        print("[INFO] Attemping to send data")
        post_request(payload)
        print("[INFO] finished")
        time.sleep(2)
        
if __name__ == "__main__":
    setup()
        
