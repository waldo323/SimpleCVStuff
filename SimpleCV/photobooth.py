from SimpleCV import Camera, Display, Color
import datetime, time


def time_stamped(fname, fmt='%Y_%m_%d_%H%M%S.{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

def timeFmt( fmt='%Y-%m-%d-%H:%M:%S'):
    return datetime.datetime.now().strftime(fmt)
#with open(time_stamped('myfile.txt'),'w') as outf:
#    outf.write('data!')

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
		img.save("./photos/" + time_stamped("photo.jpg"))
		img.drawText("photo saved.", color=Color().getRandom())
		img.save(display)
		time.sleep(5)
		counter = counter + 1
