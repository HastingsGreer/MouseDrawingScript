from PIL import Image
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random

import urllib, cStringIO

m = PyMouse()
k = PyKeyboard()


x_dim, y_dim = m.screen_size()

def getpositiontimer(name):
    print "Capturing "+ name + " in:"
    for i in range(3, 0, -1):
        print i
        time.sleep(1)
    place = m.position()
    print name + " at ", place
    return place

topLeft = getpositiontimer("Top Left")
bottomRight = getpositiontimer("Bottom Right")

width = bottomRight[0] - topLeft[0]
height = bottomRight[1]- topLeft[1]

scale = input("Scale? ")


print width, width / scale
print height, height / scale

print "URL?"
file = cStringIO.StringIO(urllib.urlopen(raw_input()).read())
doge = Image.open(file)
doge = doge.resize((width/scale, height/scale), Image.ANTIALIAS)
doge = doge.convert("1")
print doge.getpixel((1,1))
print doge.size
for x in range(0,doge.size[0]):
    for y in range(0,doge.size[1]):
        if not(doge.getpixel((x, y)) ):
            m.click(x*scale+ topLeft[0] + random.randint(-1, 1), y*scale+ topLeft[1] + random.randint(-1, 1), 1)
            time.sleep(.02)
