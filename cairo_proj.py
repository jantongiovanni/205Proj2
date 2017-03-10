#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

from PIL import Image
from random import random
import cairo
import shutil

myList = []
# print("Input complete image filename: ")
# image = raw_input();
# myList.append(Image.open(image))
# width, height  = myList[0].size
PI = 3.14159265359
TWOPI = 2.0*PI
BACK = [0,0,0,1]
FRONT = [0,0,0,1.0]
SIZE = 1000
ONE = 1/SIZE
LINEWIDTH = ONE

STEPS = 1000

NEW_COUNT = 100


# #STEPS = 250
# #NEW_COUNT = 600
# print("Input for steps and new circles. Higher values will take longer but will generate more complex and detailed images")
# print("Input number of steps to execute (recommended values between 100 - 300) : ")
# STEPS = input();
# print("Input number of new circles generated at each step (recommended values between 100 and 500) : ")
# NEW_COUNT = input();


RES = 'out.png'

def getNewFile():
  return RES

def imageSrc(msg):
    myList.append(Image.open(msg))
    global width
    global height
    width, height  = myList[0].size

def is_ok(x1, y1, r1, x2, y2, r2):
  return ((x1-x2)**2 + (y1-y2)**2) > (r1 + r2 + ONE)**2

def add_new_circles(n, circles):

  for i in xrange(n):
    xn = random()
    yn = random()
    rn = ONE

    ok = True
    for c in circles:

      if not is_ok(xn, yn, rn, c['x'], c['y'], c['r']):
        ok = False
        break

    if ok:
      circles.append({
        'x': xn, 
        'y': yn, 
        'r': rn, 
        'active': True
      })

def increase_radius(circles):

  for c in circles:
    if c['active']:
      c['r'] += ONE

def test(circles):

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

  ctx.set_source_rgba(*FRONT)

  for c in circles:
    r, g, b = myList[0].getpixel((c['x'] * width, c['y'] * height))
    rgba = [r/256, g/256, b/256, 1.0]
    ctx.set_source_rgba(*rgba)
    ctx.arc(c['x'], c['y'], c['r'], 0, TWOPI)
    ctx.fill()

def main():

  # make the canvas
  sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, SIZE, SIZE)
  #sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
  ctx = cairo.Context(sur)

  # scale canvas so that x and y ranges from 0 to 1.
  ctx.scale(SIZE, SIZE)
  #ctx.scale(width, heigth)
  # set the background color of the canvas
  ctx.set_source_rgba(*BACK)
  ctx.rectangle(0, 0, 1.0, 1.0)
  ctx.fill()

  ctx.set_line_width(LINEWIDTH)


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
  shutil.move(RES, "static/circlePacked/"+RES)
  

if __name__ == '__main__':
  main()
  
print("Image generated! Thank you for using the program!")
#400, 400 1:50