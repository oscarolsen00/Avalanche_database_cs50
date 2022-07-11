import pdfquery
import pandas as pd


#potential ideas - 
# 1 - scrape do we scrape straight form website or from pdf of images and using database of images compare which one like and output data
# 2 - just scrape text from pdf more difficult to get rose


###################  extracts relevant text ###################

# importing required modules 
import PyPDF2 
 
# creating a pdf file object 
pdfFileObj = open('swiss_ab.pdf', 'rb') 
 
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# creating a page object 
pageObj = pdfReader.getPage(0) 
 
# extracting text from page 
print(pageObj.extractText()) 
 
# closing the pdf file object 
pdfFileObj.close()



##################### extracts relevant images ############################

#this code shows that there is only one image on the pdf which
# is not what we want need to figure out how to find the other images as this is not working...

# import os
# import fitz  
# from tqdm import tqdm 

# workdir = "/Users/oscarolsen/Documents/FATMAP/Round_2/Avalanche_database_cs50/scrap_work"

# for each_path in os.listdir(workdir):
#     if ".pdf" in each_path:
#         doc = fitz.Document((os.path.join(workdir, each_path)))

#         for i in tqdm(range(len(doc)), desc="pages"):
#             for img in tqdm(doc.get_page_images(i), desc="page_images"):
#                 xref = img[0]
#                 image = doc.extract_image(xref)
#                 pix = fitz.Pixmap(doc, xref)
#                 pix.save(os.path.join(workdir, "%s_p%s-%s.png" % (each_path[:-4], i, xref)))
               