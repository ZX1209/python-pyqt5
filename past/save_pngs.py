

from PIL import Image
import os

import logging


logging.basicConfig(level=logging.DEBUG)



if not os.path.exists('./changed'):
    os.mkdir('./changed')



files = tuple(os.walk(os.curdir))[0][2]


for filename in files:
    logging.debug('process '+filename)
    if filename.endswith('.png') or  filename.endswith('.jpg'):
        oldFile = Image.open(filename)
        filename = filename[:-4]+'.png'
        oldFile.save('./changed/'+filename)
        logging.debug('save '+filename)



