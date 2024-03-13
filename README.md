# Distance-Tracking
🚀 This project 🛠️ involves an Arduino equipped with an ultrasonic sensor and a Python script 🐍 for real-time data visualization 📊. The Arduino is programmed 💻 to read distance measurements 📏 from the ultrasonic sensor and send the data over a serial connection 🔌.

The Arduino sketch sets up the trigger and echo pins for the ultrasonic sensor and initializes the serial communication at 9600 baud rate. In the main loop, it triggers the ultrasonic sensor, measures the echo pulse duration, calculates the distance based on the speed of sound 🔊, and sends the distance over the serial connection every second ⏱️.

The Python script on the other hand, opens a serial connection to the Arduino on a specified port and begins reading the distance data. It continuously reads lines from the serial port, converts them to floats, and adds them to a list of distances. Any readings that exceed 400 cm are ignored to ensure data quality 📉.

The list of distances is then visualized using matplotlib 📈. The distances are plotted on a graph 📉, with the most recent distance displayed as text in the top right corner of the plot. The plot is updated in real-time as new data is read from the Arduino. The y-axis of the plot is set to range from 2 cm to 400 cm to match the expected range of the ultrasonic sensor.

This project serves as a basic example of how to interface an Arduino with Python for real-time data visualization, and could be a starting point for more complex projects involving Arduino and ultrasonic sensors. 🌟
