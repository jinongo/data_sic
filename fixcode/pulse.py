import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from ubidots import build_payload, post_request

# Konfigurasi MCP3008
CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# def kalibrasi():
    # Kalibrasi awal
calibration_samples = 10
calibration_sum = 0

for _ in range(calibration_samples):
    raw_value = mcp.read_adc(0)  # Ubah saluran sesuai koneksi
    calibration_sum += raw_value

calibration_value = calibration_sum / calibration_samples

    # Faktor skala (sesuaikan berdasarkan pengalaman atau referensi spesifik sensor)
scaling_factor = 0.3

# def read_tes():
# Baca data sensor dan hitung detak jantung
while True:
    raw_value = mcp.read_adc(0)  # Ubah saluran sesuai koneksi
    heart_rate = int((raw_value - calibration_value) * scaling_factor)
    print("Detak jantung:", heart_rate)
    time.sleep(1)

    payload = build_payload(heart_rate)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
        # return heart_rate

