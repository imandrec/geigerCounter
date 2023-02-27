import time
import board
import analogio

analog_in = analogio.AnalogIn(board.A1)

reference_voltage = 5 # voltage supplied must be 5V
conversion_factor = 0.0082 # the conversion factor is given as 0.0082 µSv/hr/V.

while True:
    analog_input_value = analog_in.value
    voltage = (analog_input_value / 65535) * reference_voltage
    radiation_level = voltage * conversion_factor

    print("Radiation level:", radiation_level, "µSv/hr")
    time.sleep(1)