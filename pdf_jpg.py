#coding=utf-8
import os
import sys  
import PyPDF2  
import PythonMagick 
import shutil
from time import sleep
from tkFileDialog import askopenfilename
from os.path import abspath, exists, dirname, basename, splitext, isdir, join as joinpath
from tqdm import tqdm
from chardet import detect
reload(sys)
sys.setdefaultencoding('utf-8')

absname = askopenfilename(filetypes=[(u'pdf格式', '*.pdf')])
coding = 'gbk'  #detect(absname)
tempname = joinpath('D:', 'images.pdf')
tempdir = joinpath('D:', '.temp')
if exists(tempdir):
    shutil.rmtree(tempdir)
os.mkdir(tempdir)
shutil.copyfile(absname, tempname)
fname = basename(absname)
outputdir = joinpath(dirname(absname), splitext(fname)[0])
if not exists(outputdir) or not isdir(outputdir):
    os.mkdir(outputdir)

#print('Converting {} ...'.format(fname)) 

pdf_im = PyPDF2.PdfFileReader(file(tempname, "rb"))
npage = pdf_im.getNumPages()
for p in tqdm(range(npage)):  
    im = PythonMagick.Image('{}[{}]'.format(tempname, p))  
    #im.density('300')  
    #im.read(pdffilename + '[' + str(p) +']')  
    im.write(joinpath(tempdir, '{}.jpg'.format(p+1)).encode(coding)) 

for i in os.listdir(tempdir):
    shutil.move(joinpath(tempdir, i), outputdir)
shutil.move(tempname, 'donefile')
print(u'\n转换完毕。文件位于 {}\n\n'.format(outputdir))
print(u'3秒后窗口自动关闭')
sleep(3)
