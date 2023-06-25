import time
import datetime
import picamera
import socket

def schedule_drone_monitoring():
    # Get the current time and date.
    now = datetime.datetime.now()

    # Set the time and date for the drone to start monitoring.
    start_time = datetime.datetime(now.year, now.month, now.day, 8, 0, 0)

    # Set the time and date for the drone to stop monitoring.
    end_time = datetime.datetime(now.year, now.month, now.day, 17, 0, 0)

    # Start the drone monitoring.
    while start_time <= now <= end_time:
        # Capture an image.
        with picamera.PiCamera() as camera:
            camera.capture('image.jpg')

        # Send the image to the host laptop.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(('localhost', 8080))
            sock.sendall(open('image.jpg', 'rb').read())

        time.sleep(60)

if __name__ == "__main__":
    schedule_drone_monitoring()