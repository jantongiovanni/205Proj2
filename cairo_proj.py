# CST 205 Section 2
# cairo_proj.py

# This file converts a photo into a circle packed themed.

# Joseph Antongiovanni, there are only 7 functions that Maria Loza worked on. 
# Everything else was from Joseph.

# 15 March 2017

# https://github.com/jantongiovanni/205Proj2/tree/maria



#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

from PIL import Image
from random import random, randrange
import cairo
import shutil
import time

#UPLOADED IMAGE SHOULD BE SQUARE FOR CORRECT SCALING

myList = [] #stores image

PI = 3.14159265359
TWOPI = 2.0*PI
BACK = [0,0,0,1] #background image
FRONT = [0,0,0,1] #default color of circle
SIZE = 1000
ONE = 1/SIZE
LINEWIDTH = ONE

# STEPS = 1000 #steps controls potential max size of circles

# NEW_COUNT = 100 #new_count controls number of new cicles added per instance

# RADIUS = 5; #radius sets the default smallest circle radius, smaller numbers will generate images with tiny circles

# #STEPS = 250
# #NEW_COUNT = 600

  
# Maria worked only in this section ----------------------------------------------------------

def makeNewImg():
  global RES
  RES = str(randrange(0, 1000))+'.png'
  print(RES + " MAKE")

def getNewFile():
  return RES
  
def setSteps(num):
  global STEPS
  STEPS = num

def setCount(num):
  global NEW_COUNT
  NEW_COUNT = num
  
def setRadius(num):
  global RADIUS
  RADIUS = num
  
def setOverlap(num):
  global OVERLAP
  OVERLAP = num

def imageSrc(msg):
    myList.append(Image.open(msg))
    global width
    global height
    width, height  = myList[0].size #size of image
#-------------------------------------------------------------------------------------- 


# # uncomment if you don't want GUI review the README first ------------------------------------
# makeNewImg()
# print("Input complete image filename: ")
# image = raw_input();

# #UPLOADED IMAGE SHOULD BE SQUARE FOR CORRECT SCALING

# myList.append(Image.open(image))
# width, height  = myList[0].size #size of image

# print("try 400 400 .005 2 for overlapping circle image, 400 400 .01 1 for normal")

# print("Input for steps and new circles. Higher values will take longer but will generate more complex and detailed images")
# print("Input number of steps to execute (recommended value: 400) : ")
# STEPS = input();
# print("Input number of new circles generated at each step (recommended value: 400) : ")
# NEW_COUNT = input();
# print("Input starting radius of cirlces (recommended value: .01)")
# RADIUS = float(input());
# print("circle overlap value: 1 for none, 2 for max")
# OVERLAP = float(input());
# # --------------------------------------------------------------------------------------------
    

def is_ok(x1, y1, r1, x2, y2, r2):  #checks if a new cicle to be added will not overlap with any other circles
  return ((x1-x2)**2 + (y1-y2)**2) > (r1 + r2 + ONE)**2
  #returns true if difference between x and y values of cicles (squared to make positive)
  #are greater than the difference between the radius of the cicles(squared to make positive)

def add_new_circles(n, circles):  #method to add new circles, n is new_count to be added

  for i in xrange(n): #picks random x and y
    xn = random()
    yn = random()
    # rn = ONE
    rn = RADIUS

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
      # c['r'] += ONE #adds .001 to radius size
      c['r'] += ONE + ONE #adds .001 to radius size

def test(circles): #no clue --------------------

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

  ctx.set_source_rgba(*FRONT) #default color of circle

  for c in circles:
    r, g, b = myList[0].getpixel((c['x'] * width, c['y'] * height)) #grabs rgb value from image
    rgba = [r/256, g/256, b/256, 1.0]  #formats rgb values
    ctx.set_source_rgba(*rgba) #assigns rgb value
    ctx.arc(c['x'], c['y'], c['r'] * OVERLAP, 0, TWOPI) #creates circle
    ctx.fill() #fills with correct rgb value

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


  circles = [] #main circle arrray to store all circles locations and radius values
  add_new_circles(NEW_COUNT, circles)

  for i in xrange(STEPS):

    increase_radius(circles)

    ok_count = test(circles)

    if ok_count < 1:
      add_new_circles(NEW_COUNT, circles)
      print(i, 'adding new circles, total count: ' + str(len(circles)))
    
    
    

  show(ctx, circles)

  sur.write_to_png(getNewFile())
  shutil.move(getNewFile(), "static/circlePacked/"+getNewFile())
  

if __name__ == '__main__':
  main()
  
# print("Image generated! Thank you for using the program!")
