from __future__ import print_function
from wand.image import Image
 
with Image(filename='xml.pdf') as img:
    print('pages = ', len(img.sequence))
 
    with img.convert('jpg') as converted:
        converted.save(filename='pyout/page.jpg')
