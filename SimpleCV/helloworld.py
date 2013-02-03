from SimpleCV import Camera, Display, Image
import time

cam = Camera()
display = Display()
img = cam.getImage()
img.drawText("Hello world")
img.save(display)
time.sleep(10)
