from SimpleCV import Camera, Display, Color
import time

cam = Camera()

display = Display()
img = cam.getImage()

img.drawText("Left click to save a photo", color=Color().getRandom())
img.save(display)
time.sleep(5)

counter = 0
while not display.isDone():
	img = cam.getImage()
	img.save(display)
	
	if display.mouseLeft:
		img.save("photobooth" + str(counter) + ".jpg")
		img.drawText("photo saved.", color=Color().getRandom())
		img.save(display)
		time.sleep(5)
		counter = counter + 1
