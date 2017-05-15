#coding=utf-8
import os
import sys  
import PyPDF2  
import PythonMagick 
import shutil
from time import sleep
from tkinter.filedialog import askopenfilename
from os.path import abspath, exists, dirname, basename, splitext, isdir, join as joinpath
from tqdm import tqdm

fname = askopenfilename(filetypes=[('pdf格式', 'pdf')])
outputdir = joinpath(dirname(fname), splitext(fname)[0])
if not exists(outputdir) or not isdir(outputdir):
    os.mkdir(outputdir)

#print('Converting {} ...'.format(fname)) 

pdf_im = PyPDF2.PdfFileReader(open(fname, "rb"))
npage = pdf_im.getNumPages()
for p in tqdm(range(npage)):  
    im = PythonMagick.Image('{}[{}]'.format(tempname, p))  
    #im.density('300')  
    #im.read(pdffilename + '[' + str(p) +']')  
    im.write(joinpath(outputdir, '{}.jpg'.format(p+1))) 

print(u'\n转换完毕。文件位于 {}\n\n'.format(outputdir))
print(u'3秒后窗口自动关闭')
sleep(3)
