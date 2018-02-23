
from pathlib import Path
import os
import shutil
import random
HOME = os.environ["HOME"]

for kizunaai in Path('{HOME}/dance/キズナアイ/jpegs'.format(HOME=HOME)).glob('*'):
  no = str(kizunaai).split('/').pop()
  print(kizunaai)
  print(no)
  shiro = Path('{HOME}/dance/シロ/jpegs/{no}'.format(HOME=HOME, no=no))
  
  if random.random() <= 0.8:
    shutil.copy(str(kizunaai), 'train/a/{no}'.format(no=no) )
    shutil.copy(str(shiro), 'train/b/{no}'.format(no=no) )
  #else:
  shutil.copy(str(kizunaai), 'test/a/{no}'.format(no=no) )
  shutil.copy(str(shiro), 'test/b/{no}'.format(no=no) )
