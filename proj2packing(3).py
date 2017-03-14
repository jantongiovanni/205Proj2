#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

from PIL import Image
from random import random
import cairo

print("Input complete image filename: ")
image = raw_input();

#UPLOADED IMAGE SHOULD BE SQUARE FOR CORRECT SCALING

myList = [] #stores image
myList.append(Image.open(image))
width, height  = myList[0].size #size of image
PI = 3.14159265359
TWOPI = 2.0*PI
BACK = [0,0,0,1] #background image
FRONT = [0,0,0,1] #defualt color of circle
SIZE = 1000
ONE = 1/SIZE
LINEWIDTH = ONE

print("try 400 400 .005 2 for overlapping circle image, 400 400 .01 1 for normal")

print("Input for steps and new circles. Higher values will take longer but will generate more complex and detailed images")
print("Input number of steps to execute (recommended value: 400) : ")
STEPS = input();
print("Input number of new circles generated at each step (recommended value: 400) : ")
NEW_COUNT = input();
print("Input starting radius of cirlces (recommended value: .01)")
radius = float(input());
print("circle overlap value: 1 for none, 2 for max")
overlap = float(input());

#steps controls potential max size of circles
#new_count controls number of new cicles added per instance
#radius sets the default smallest circle radius, smaller numbers will generate images with tiny circles

RES = 'out.png' #name of output image

def is_ok(x1, y1, r1, x2, y2, r2): #checks if a new cicle to be added will not overlap with any other circles
  return ((x1-x2)**2 + (y1-y2)**2) > (r1 + r2 + ONE)**2 
  #returns true if difference between x and y values of cicles (squared to make positive)
  #are greater than the difference between the radius of the cicles(squared to make positive)

def add_new_circles(n, circles): #method to add new circles, n is new_count to be added

  for i in xrange(n): #picks random x and y
    xn = random()
    yn = random()
    #rn = ONE
    rn = radius
    
    ok = True
    for c in circles:

      if not is_ok(xn, yn, rn, c['x'], c['y'], c['r']): #checks for overlap
        ok = False
        break

    if ok: #add new circle to circles array
      circles.append({
        'x': xn, 
        'y': yn, 
        'r': rn, 
        'active': True
      })

def increase_radius(circles): #as program runs, increase the potential size of circles to be added

  for c in circles:
    if c['active']:
      c['r'] += ONE + ONE #adds .001 to radius size

def test(circles): #no clue

  ok_count = 0

  for a, ca in enumerate(circles):

    for b, cb in enumerate(circles):

      if a == b:
        continue

      if not cb['active']:
        continue

      if not is_ok(ca['x'], ca['y'], ca['r'], cb['x'], cb['y'], cb['r']):
        cb['active'] = False

      else:
        ok_count += 1

  return ok_count


def show(ctx, circles):
  #default color of circle
  ctx.set_source_rgba(*FRONT) 

  for c in circles:
    #grabs rgb value from image
    r, g, b = myList[0].getpixel((c['x'] * width, c['y'] * height))
    
    #formats rgb values
    rgba = [r/256, g/256, b/256, 1.0] 
    
    #assigns rgb value
    ctx.set_source_rgba(*rgba)
    
    #creates circle
    ctx.arc(c['x'], c['y'], c['r'] * overlap, 0, TWOPI) 
    #ctx.rectangle(c['x'], c['y'], c['r']*2, c['r']*2)
    
    
    #fills with correct rgb value
    ctx.fill() 

def main():

  # make the canvas
  sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, SIZE, SIZE)
  ctx = cairo.Context(sur)

  # scale canvas so that x and y ranges from 0 to 1.
  ctx.scale(SIZE, SIZE)

  # set the background color of the canvas
  ctx.set_source_rgba(*BACK)
  ctx.rectangle(0, 0, 1.0, 1.0)
  ctx.fill()

  ctx.set_line_width(LINEWIDTH)

  #main circle arrray to store all circles locations and radius values
  circles = []
  
  add_new_circles(NEW_COUNT, circles)

  for i in xrange(STEPS):

    increase_radius(circles)

    ok_count = test(circles)

    if ok_count < 1:
      add_new_circles(NEW_COUNT, circles)
      print(i, 'adding new circles, total count: ' + str(len(circles)))
    

  show(ctx, circles)

  sur.write_to_png(RES)
  

if __name__ == '__main__':
  main()
  
print("Image generated! Thank you for using the program!")
