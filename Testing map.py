import serial
import matplotlib.pyplot as plt

# Open the serial port
ser = serial.Serial('COM3', 9600)  # replace 'COM3' with your port

# Set up the figure
plt.ion()  # enable interactive drawing
fig = plt.figure()
ax = fig.add_subplot(111)

distances = []

while True:
    try:
        # Read a line from the serial port
        line = ser.readline().decode().strip()

        # Convert the line to a float
        distance = float(line)

        # Ignore readings that exceed 400 cm
        if distance > 400:
            continue

        # Add the distance to the list
        distances.append(distance)

        # Clear the plot
        ax.clear()

        # Plot the distances
        ax.plot(distances)

        # Display the distance as text
        ax.text(1, 1, f'Distance: {distance} cm', horizontalalignment='right', verticalalignment='top', transform=ax.transAxes, fontsize=15)

        # Set the limits
        ax.set_ylim(2, 400)  # set range from 2 cm to 400 cm

        # Redraw the plot
        plt.draw()
        plt.pause(0.001)

    except ValueError:
        # Ignore lines that don't parse to a float
        pass

    except KeyboardInterrupt:
        # Exit the loop when Ctrl+C is pressed
        break

# Close the serial port
ser.close()