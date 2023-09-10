#import cv2
from time import sleep
from lobe import ImageModel
import subprocess
import gpiozero
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

model = ImageModel.load('/home/pi/Downloads/model')

# Set the default pin factory to pigpio
gpiozero.Device.pin_factory = PiGPIOFactory()

# Define the GPIO pin
servo_pin = 17  # Change to the GPIO pin connected to your servo

# Create a servo object
# min_pulse_width and max_pulse_width might need adjustments depending on the servo's specifications
servo = Servo(servo_pin, min_pulse_width=0.001, max_pulse_width=0.002)
servo.mid()

def capture_image(device="/dev/video0", resolution="1920x1020", output_file="image.jpg"):
    try:
        subprocess.run(["fswebcam", "-d", device, "-r", resolution, output_file], check=True)
        print(f"Image captured and saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError as e:
        print(f"fswebcam not found: {e}")


# Main Function
while True:
   
    sleep(1)
    capture_image()
    # Run photo through Lobe TF model
    result = model.predict_from_file('/home/pi/Downloads/image.jpg')
    print(result.prediction)
    print(result.labels[0][1]*100, "%")
    if (result.labels[0][1]*100 > 90):
        if (result.labels[0][0] == "paper"):
            servo.max()
        elif (result.labels[0][0] == "biological"):
            servo.min()        
    sleep(1)
    servo.mid() #Will always end at mid/horizontal position.
