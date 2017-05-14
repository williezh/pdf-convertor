#!/usr/bin/env python3
#coding=utf-8
import os
import sys  
import shutil
import PyPDF2  
import PythonMagick 
from os.path import exists, dirname, basename, splitext, isdir, join as joinpath
from tqdm import tqdm

# create a temp file with only ascii code in path
# 创建一个的临时文件和临时文件夹, 使其路径和文件名不含中文
realname =  "sample/xml教程.pdf" 
parentdir = dirname(realname)
tempname = joinpath('~', 'temp.pdf')
shutil.copyfile(realname, tempname)   
tempdir = joinpath('~', '.temp_pdf_jpg')
if not exists(tempdir):
    shutil.delete(tempdir)
os.mkdir(tempdir)

# create a folder as the name of the pdf file
# 创建与pdf文件同名的文件夹， 若存在询问是否覆盖 
fname = basename(real/name)
outdir = splitext(fname)[0]
if not exists(outdir) or not isdir(outdir) or '1.jpg' not in os.listdir(outdir):
    os.mkdir(outdir)
else:
    y = input('dir exists, cover it?[y/(n)] ')
    if y.lower() not in ('y', 'yes'):
        pass # append outputdir name with 1, 2, 3 ...
        

#print('Converting {} ...'.format(fname)) 

pdf_im = PyPDF2.PdfFileReader(file(tempname, "rb"))
npage = pdf_im.getNumPages()
for p in tqdm(range(npage)):  
    im = PythonMagick.Image('{}[{}]'.format(tempname, p))  
    im.write(joinpath(tempdir, '{}.jpg'.format(p+1))) 

shutil.copytree(tempdir, outdir)
os.remove(tempname)
shutil.delete(tempdir)

