//INT to D2

const int geigerInputPin = 2; // Set the input pin of the geiger counter
int count = 0; // Initialize the count variable
float conversionFactor = 0.0082; // Conversion factor to calculate radiation in µSv/h

void setup() {
  Serial.begin(9600); // Start the serial communication
  pinMode(geigerInputPin, INPUT); // Set the input pin as input
}

void loop() {
  count = 0; // Reset the count variable
  delay(300); // Wait for the tube to stabilize
  for (int i = 0; i < 10; i++) { // Take 10 readings and average them
    count += pulseIn(geigerInputPin, HIGH); // Read the pulse duration
    delay(100); // Wait 100ms between readings
  }
  count = count / 10; // Average the counts
  float radiation = count * conversionFactor; // Calculate the radiation in µSv/h
  Serial.print("Radiation: "); // Print the label for the radiation value
  Serial.print(radiation, 3); // Print the radiation value with 3 decimal places
  Serial.println(" µSv/h"); // Print the units for the radiation value
  delay(1000); // Wait for 1 second
