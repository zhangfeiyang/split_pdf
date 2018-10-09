#!/usr/bin/python3

from PyPDF2 import PdfFileReader, PdfFileWriter

def get_sub_pdf(name,super_pdf,start_page,end_page):
    pdf_read = PdfFileReader(open(super_pdf,'rb'))
    pdf_output = PdfFileWriter()
    
    #for page in range(start_page,end_page+1):
    for page in range(start_page-1,end_page):
        pdf_output.addPage(pdf_read.getPage(page))

    pdf_output.write(open(name,'wb'))

import sys
import os

super_pdf = sys.argv[1]  # You should input the name of file you would like to split 

index_file = 'index'     # Index file, from start page to end page 

if __name__ == "__main__":
       
    file = open(index_file,'r')

    lines = file.readlines()
    os.system('mkdir '+super_pdf)

    for i in range(len(lines)):
        indexs = lines[i].split()
        file_id = indexs[5]
        if not file_id == super_pdf:
            continue
        start_page = int(indexs[0])
        end_page = int(indexs[1])
        name = '_'.join(indexs[2:5])+".pdf"

        get_sub_pdf(name,super_pdf+'.pdf',start_page,end_page)
        os.system('mv '+name+' '+super_pdf)

