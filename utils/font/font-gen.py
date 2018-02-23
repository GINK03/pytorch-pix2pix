import os

import numpy
from PIL import Image, ImageDraw, ImageFont

import six

import numpy as np

from   io import BytesIO

import os

import pickle

import json

import random

from pathlib import Path

class GenFontsImage():
  def __init__(self):
    self.source = set(''.join([p.open().read().replace('\n', '') for p in Path('texts/').glob('*')]))
  
  def generate(self):
    for word in self.source:
      t = np.zeros((300, 300, 3)).astype('uint8')
      t += 255
      to_save_img_a = Image.fromarray(t)
      draw = ImageDraw.Draw(to_save_img_a)
      font = ImageFont.truetype("fonts/TakaoGothic.ttf", 200)
      draw.text((50,50), word, (0, 0, 0),font=font)
    
      t = np.zeros((300, 300, 3)).astype('uint8')
      t += 255
      to_save_img_b = Image.fromarray(t)
      draw = ImageDraw.Draw(to_save_img_b)
      #font = ImageFont.truetype("./PixelMplus12-Regular.ttf", 200)
      font = ImageFont.truetype("fonts/aoyagireisyosimo_ttf_2_01.ttf", 200)
      draw.text((50,50), word, (0, 0, 0),font=font)
      
      if random.random() <= 0.8:
        to_save_img_a.save( f'train/a/{word}.jpg', 'JPEG' ) 
        to_save_img_b.save( f'train/b/{word}.jpg', 'JPEG' ) 
      else:
        to_save_img_a.save( f'test/a/{word}.jpg', 'JPEG' ) 
        to_save_img_b.save( f'test/b/{word}.jpg', 'JPEG' ) 
        

if __name__ == '__main__':
  #vec = VecDataset( None )
  gen_fonts_image = GenFontsImage()
  gen_fonts_image.generate()
