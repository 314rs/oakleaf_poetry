import os
import random
random.seed()

# get a list of all available files
files_set = set()
for path in os.listdir("poems"):
    files_set.add(path[:4]),
files_list = list(files_set)

#choose a random file
file = "poems/" + str(files_list[random.randint(0, len(files_list)-1)]) + ".pdf"
#print("Printing " + file )

#print the pdf-file using the standart-printer (via PDFtoPrinter.exe)
os.system("PDFtoPrinter.exe " + file + " /s")

#use this to specify a printer
#os.system("PDFtoPrinter.exe " + file - " nameofprinter /s")

# "/s"flag is used to run silent. more info: http://www.columbia.edu/~em36/pdftoprinter.html