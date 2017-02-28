# from PIL import Image
# from PIL import ImageDraw
from Circle import Circle
import numpy
import cv2

from PIL import Image
from numpy import array

circles = []

circles.append(Circle(200, 200))



# c = Circle(200, 200)

# Create a black image
newImg = numpy.zeros((360,640,3), numpy.uint8)

img = Image.fromarray(newImg)
img.save("black.png")

# get a numpy array from an image
img = Image.open("black.png")
arr = array(img)

for currC in circles:
    currC.dimensions(360, 640)
    currC.numpyArray(arr)
    while (currC.growing):
        currC.grow()
        if currC.edges():
            currC.growing = False
    currC.draw(arr)

# c.numpyArray(arr)
# c.draw(arr)

# get an image from a numpy array

img = Image.fromarray(arr)
img.save("third.png")


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
