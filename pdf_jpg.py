#coding=utf-8
import os
import sys  
import PyPDF2  
import PythonMagick 
from time import sleep
from shutil import copyfile
from tkFileDialog import askopenfilename
from os.path import exists, dirname, basename, splitext, isdir, join as joinpath
from tqdm import tqdm
from chardet import detect
reload(sys)
sys.setdefaultencoding('utf-8')

absname = askopenfilename(filetypes=[(u'pdf格式', '*.pdf')])
coding = 'gbk'  #detect(absname)
pdffilename = joinpath(dirname(absname), 'images.pdf')  
copyfile(absname, pdffilename)
fname = basename(pdffilename)
outputdir = joinpath(dirname(pdffilename), splitext(fname)[0])
if not exists(outputdir) or not isdir(outputdir):
    os.mkdir(outputdir)

#print('Converting {} ...'.format(fname)) 

pdf_im = PyPDF2.PdfFileReader(file(pdffilename, "rb"))
npage = pdf_im.getNumPages()
for p in tqdm(range(npage)):  
    im = PythonMagick.Image('{}[{}]'.format(pdffilename, p))  
    #im.density('300')  
    #im.read(pdffilename + '[' + str(p) +']')  
    im.write(joinpath(outputdir, '{}.jpg'.format(p+1)).encode(coding)) 

print(u'\n转换完毕。文件位于 {}\n\n'.format(outputdir))
print(u'3秒后窗口自动关闭')
sleep(3)
