import time
import board
import pulseio

geigerInputPin = board.D2 # Set the input pin of the geiger counter
count = 0 # Initialize the count variable
conversionFactor = 0.0082 # Conversion factor to calculate radiation in µSv/h

# Set up the pulse input pin
pulse_in = pulseio.PulseIn(geigerInputPin, maxlen=100, idle_state=True)

while True:
    count = 0 # Reset the count variable
    time.sleep(0.3) # Wait for the tube to stabilize
    for i in range(10): # Take 10 readings and average them
        pulse_in.clear() # Clear the pulse buffer
        pulse_in.resume() # Start listening for pulses
        time.sleep(0.1) # Wait 100ms between readings
        pulse_in.pause() # Stop listening for pulses
        count += len(pulse_in) # Count the number of pulses

    count = count / 10 # Average the counts
    radiation = count * conversionFactor # Calculate the radiation in µSv/h
    print("Radiation: {:.3f} µSv/h".format(radiation)) # Print the radiation value with 3 decimal places
    time.sleep(1) # Wait for 1 second
