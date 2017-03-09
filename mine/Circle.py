from PIL import ImageDraw
from PIL import Image
import cv2

class Circle:
    def __init__(self, x, y, c): #constructor
        self.x = x
        self.y = y
        self.r = 1
        self.growing = True
        self.c = c
        
    def numpyArray(self, array):
        self.array = array
        return self.array
        
    def draw(self, array):
        cv2.circle(array,(self.x,self.y), self.r, self.c, -1)
        
    def modNumArray(self):
        return self.array
        
    def grow(self):
        if self.growing:
            self.r += 1
    
    def edges(self):
        return (self.x + self.r > self.w or self.x - self.r < 0 or self.y + self.r > self.h or self.y - self.r < 0)
        
    def dimensions(self, w, h):
        self.w = w
        self.h = h
        