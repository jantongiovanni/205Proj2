# from PIL import Image
# from PIL import ImageDraw
from Circle import Circle
import numpy
import cv2
import random

from PIL import Image
from numpy import array

import math

circles = []
# posSpots = []

bWidth = 768
bHeight = 1024

width = 1024
height = 768

def newCircle():
    for i in range (0,3000):
        # slot = random.randint(0, len(posSpots))
        # x, y = posSpots[slot]
        randY = random.randint(0, 767)
        randX = random.randint(0, 1023)
        # print "x " + str(randX) + " y " + str(randY)
        # randX = x
        # randY = y
        
        valid = True
        for c in circles:
            d = math.hypot(c.x - randX, c.y - randY)
            if (d < c.r):
                valid = False
                break
        
        # print "x: " + str(randX) + " y: " + str(randY)
        if valid:
            red, green, blue = img.getpixel((randX,randY))
            # return Circle(randX, randY)
            circles.append(Circle(randX, randY, (red, green, blue)))
        else:
            i -= 1


    
# for i in range (0,5):
#     randX = random.randint(0, width)
#     randY = random.randint(0, height)
    
#     circles.append(Circle(randX, randY))



# if c != None:
#     circles.append(c)

# for p in circles: print p.growing


# c = Circle(200, 200)

# Create a black image
newImg = numpy.zeros((bWidth,bHeight,3), numpy.uint8)

img = Image.fromarray(newImg)
img.save("black.png")

img = Image.open("birdoriginal.jpg")

# get a numpy array from an image
imgBlack = Image.open("black.png")
arr = array(imgBlack)

# for x in range(0, width):
#     for y in range(0, height):
#         red, green, blue = img.getpixel((x,y))
#         if (red == 255) and (green == 255) and (blue == 255):
#             posSpots.append((x,y))
            
# print len(posSpots)

newCircle()

for currC in circles:
    currC.dimensions(width, height)
    currC.numpyArray(arr)
    # print "x: " + str(currC.x) + " y: " + str(currC.y)
    while (currC.growing):
        # print "edge: " + str(currC.edges())
        
        currC.grow()
        if currC.edges():
            currC.growing = False
        else:
            for other in circles:
                if currC != other:
                    d = math.hypot(currC.x - other.x, currC.y - other.y)
                    if (d - 1 < currC.r + other.r):
                        currC.growing = False
                        break
                
    currC.draw(arr)

# c.numpyArray(arr)
# c.draw(arr)

# get an image from a numpy array

img = Image.fromarray(arr)
img.save("fifth.png")



# -----------------------------------works-------------------------------------------
# # get a numpy array from an image
# img = Image.open("output.png")
# arr = array(img)



# # for ()

# # cv2.circle(arr,(450,187), 63, (0,0,255), -1)
# # cv2.circle(arr,(100,187), 63, (0,0,255), -1)
# cv2.circle(arr,(200,187), 63, (0,0,255), -1)

# # get an image from a numpy array
# img = Image.fromarray(arr)
# img.save("output.png")

# # img = Image.open("output.png")
# # arr = array(img)

# # # for ()

# # cv2.circle(arr,(100,187), 63, (0,0,255), -1)
# # # cv2.circle(arr,(100,187), 63, (0,0,255), -1)
# # # cv2.circle(arr,(200,187), 63, (0,0,255), -1)

# # # get an image from a numpy array
# # img = Image.fromarray(arr)
# # img.save("output.png")

# ----------------------------------------------------------------------------







# Create a black image
# newImg = np.zeros((512,512,3), np.uint8)
# newImg = cv2.imread("test2.jpeg")

# creates the new image
# newImg = Image.new("RGB", (640, 360))
# newImg = Image.open("cute.jpg")
# im = cv2.imread("cute.jpg")
# cv2.circle(newImg,(100,187), 63, (0,0,255), -1)

# im = Image.fromarray(newImg)
# im.save("test3.jpeg")

# image = Image.new('RGBA', (640, 360))
# image = Image.open("cute.jpg")
# draw = ImageDraw.Draw(image)
# draw.ellipse((50, 50, 180, 180), fill = 'blue', outline ='blue')
# # draw.point((100, 100), 'red')
# image.save('test1.png')

# image = Image.open("cute.jpg")
# draw = ImageDraw.Draw(image)
# draw.ellipse(((200-50, 200-50), (200+50, 200+50)), fill=(255,0,0,0))        

# c = Circle(200, 200)

# c.show();

# saves the image in the current directory   
# newImg.save("test.png", "PNG") 

print "done"