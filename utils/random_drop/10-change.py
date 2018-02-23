from PIL import Image

from pathlib import Path

import json

from PIL import ImageOps
from PIL import ImageDraw

import random
for name in Path('../../pixabay-scraper/metas').glob('*'):
  obj = json.load(name.open())
  if '風景' in obj['tags'].split(', '):
    print(obj)
    h = str(name).split('/').pop().replace('.json','')
    print(h)

    p = Path(f'../../pixabay-scraper/imgs/{h}.jpg').exists()
    if p is not True:
      continue
    print(p)

    img = Image.open(f'../../pixabay-scraper/imgs/{h}.jpg')
    print(img.size)
    x, y = (list(img.size))
    if x > y:
      rate = y/224
      xr   = int(x/rate)
      yr   = 224
      img = img.resize((xr, 224))

      # crop mid
      # xrのほうが大きい
      start = xr//2 - 112
      end   = 112 + xr//2
      img  = img.crop( (start, 0, end, 224)  )
      print(img.size)
      
      drop = img.copy()
      draw = ImageDraw.Draw(drop)
      # drop size 20x20
      for y in range(0, 224, 5):
        for x in range(0, 224, 5):
          xs = x
          xe = x + 5
          ys = y
          ye = y + 5
          if random.random() < 0.3:
            draw.rectangle([(xs,ys),(xe,ye)],fill="white")
      if random.random() <= 0.8:
        img.save(f'train/b/{h}.jpg')
        drop.save(f'train/a/{h}.jpg')
      else:
        img.save(f'test/b/{h}.jpg')
        drop.save(f'test/a/{h}.jpg')
    if x <= y:
      rate = x/224
      xr   = 224
      yr   = int(y/rate)
      img  =img.resize((224, yr))

      # crop mid
      # xrのほうが大きい
      start = yr//2 - 112
      end   = 112 + yr//2
      img  = img.crop( (0, start, 224, end)  )
      print(img.size)
      
      drop = img.copy()
      draw = ImageDraw.Draw(drop)
      # drop size 20x20
      for y in range(0, 224, 5):
        for x in range(0, 224, 5):
          xs = x
          xe = x + 5
          ys = y
          ye = y + 5
          if random.random() < 0.3:
            draw.rectangle([(xs,ys),(xe,ye)],fill="white")
      
      if random.random() <= 0.8:
        img.save(f'train/b/{h}.jpg')
        drop.save(f'train/a/{h}.jpg')
      else:
        img.save(f'test/b/{h}.jpg')
        drop.save(f'test/a/{h}.jpg')
