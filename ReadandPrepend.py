#!/usr/bin/env python
import os
import sys
import glob

from PIL import Image
import PIL.Image

import tesserocr

jpgs = glob.glob('./*jpg')

prep = ''
if len(sys.argv) == 2:
    prep = sys.argv[1]
elif len(sys.argv) != 2:
   print 'python ReadandPrepend.py [prependage]'
   exit(1)
api = tesserocr.PyTessBaseAPI(lang='chi_sim+eng+chi_tra')

for file in jpgs:
    src = file
    api.SetImageFile(file)
    text = api.GetUTF8Text().strip()
    text = text.replace("/",'').replace(".","").replace(":","").replace("$","").replace(";","").replace("\n","")
    print text.encode('utf8')
    dst = prep+text+'.jpg'
#    print u"src:  " + src.decode('utf-8') + " dst:  " + dst.decode('utf-8')
    os.rename(src,dst.encode('utf-8'))

#print text



