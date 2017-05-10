#coding=utf-8
import os
import sys  
import PyPDF2  
import PythonMagick 
from tkFileDialog import askopenfilename
from os.path import exists, dirname, basename, splitext, isdir, join as joinpath
from tqdm import tqdm
  
pdffilename = str(askopenfilename(filetypes=[(u'pdf格式', '*.pdf')]))  
#pdffilename = "sample/xml.pdf"   
fname = basename(pdffilename)
outputdir = joinpath(dirname(pdffilename), splitext(fname)[0])
if not exists(outputdir) or not isdir(outputdir):
    os.mkdir(outputdir)

#print('Converting {} ...'.format(fname)) 

pdf_im = PyPDF2.PdfFileReader(file(pdffilename, "rb"))
npage = pdf_im.getNumPages()
for p in tqdm(range(npage)):  
    im = PythonMagick.Image(pdffilename + '[' + str(p) +']')  
    #im.density('300')  
    #im.read(pdffilename + '[' + str(p) +']')  
    im.write(joinpath(outputdir, '{}.jpg'.format(p+1))) 
