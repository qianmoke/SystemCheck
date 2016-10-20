from win32com.client import Dispatch
import os
from config import imagePath
from re import search
from os import remove

def exceltoimage(reportPath, fileName, imagePath):
    try:
        excel = Dispatch('Excel.Application')
    
        excel.Visible = True
        excel.DisplayAlerts = True
    
        workbook = excel.Workbooks.Open(reportPath+ '\\' + fileName)
        imageName=os.path.abspath(imagePath+'\\'+fileName+".html")
        excel.ActiveWorkbook.SaveAs(imageName, 44)  
        excel.ActiveWorkbook.Close()
    finally:
        excel.Application.Quit()
        del excel

def imagechoose(Path, fileName):
    count = int(fileName.split(".")[0][5:])
    if (("png" not in fileName) or (count % 2 == 0)):
        remove(Path +"\\"+ fileName)
    
        
        
    