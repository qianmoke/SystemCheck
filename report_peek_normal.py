'''
Created on Dec 21, 2015

@author: joy
'''
import xlsxwriter
import os


def readpeek(file):
    peekFile = open(file,"r")
    #print peekFile
    timetaglist=[]
    TClassINFO01list=[]
    TClassINFO02list=[]
    TClassINFO03list=[]
    TClassINFO04list=[]
    TClassINFO05list=[]
    TClassINFO06list=[]
    TClassINFO07list=[]
    TClassINFO08list=[]
    TClassINFO09list=[]
    TClassINFO10list=[]
    peektablelist=[]
    for line in peekFile:
        linetmp=line[:-1]
        timetaglist.append(linetmp.split(",")[0])
        TClassINFO01list.append(long(linetmp.split(",")[1])) 
        TClassINFO02list.append(long(linetmp.split(",")[2])) 
        TClassINFO03list.append(long(linetmp.split(",")[3])) 
        TClassINFO04list.append(long(linetmp.split(",")[4])) 
        TClassINFO05list.append(long(linetmp.split(",")[5])) 
        TClassINFO06list.append(long(linetmp.split(",")[6])) 
        TClassINFO07list.append(long(linetmp.split(",")[7])) 
        TClassINFO08list.append(long(linetmp.split(",")[8])) 
        TClassINFO09list.append(long(linetmp.split(",")[9])) 
        TClassINFO10list.append(long(linetmp.split(",")[10]))
    peektablelist.append(timetaglist)
    peektablelist.append(TClassINFO01list)
    peektablelist.append(TClassINFO02list)
    peektablelist.append(TClassINFO03list)
    peektablelist.append(TClassINFO04list)
    peektablelist.append(TClassINFO05list)
    peektablelist.append(TClassINFO06list)
    peektablelist.append(TClassINFO07list)
    peektablelist.append(TClassINFO08list)
    peektablelist.append(TClassINFO09list)
    peektablelist.append(TClassINFO10list)
    #print peektablelist
    return peektablelist
    
def TClassPeek_area_stacked(peektablelist,file):
    workbook = xlsxwriter.Workbook(file + '.chart_column.xlsx')
    worksheet = workbook.add_worksheet('TclassPeekStacked')  
    bold = workbook.add_format({'bold': 1})    
    
    # Add the worksheet data that the charts will refer to.
    headings = ['timetag', 'TClassINFO01', 'TClassINFO02', 'TClassINFO03', 'TClassINFO04', 'TClassINFO05', 'TClassINFO06','TClassINFO07', 'TClassINFO08', 'TClassINFO09', 'TClassINFO10']
    data = peektablelist
    worksheet.write_row('A1', headings, bold)
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3]) 
    worksheet.write_column('E2', data[4]) 
    worksheet.write_column('F2', data[5]) 
    worksheet.write_column('G2', data[6])
    worksheet.write_column('H2', data[7]) 
    worksheet.write_column('I2', data[8]) 
    worksheet.write_column('J2', data[9]) 
    worksheet.write_column('K2', data[10])
    chart2 = workbook.add_chart({'type': 'area', 'subtype': 'stacked'})
    # Configure the TClassINFO01 series.
    lineNumber = len(data[0])
    chart2.add_series({
        'name':       '=TclassPeekStacked!$B$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$B$2:$B$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'red'}
    })    
    # Configure TClassINFO02 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$C$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$C$2:$C$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'blue'}
    })
    # Configure TClassINFO03 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$D$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$D$2:$D$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'yellow'}
    })    
    # Configure TClassINFO04 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$E$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$E$2:$E$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'green'}
    })
    # Configure TClassINFO05 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$F$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$F$2:$F$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'brown'}
    })    
    # Configure TClassINFO06 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$G$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$G$2:$G$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'orange'}
    })
    # Configure the TClassINFO07 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$H$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$H$2:$H$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'pink'}
    })    
    # Configure TClassINFO08 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$I$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$I$2:$I$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'lime'}
    })
    # Configure TClassINFO09 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$J$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$J$2:$J$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'purple'}
    })    
    # Configure TClassINFO10 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$K$1',
        'categories': '=TclassPeekStacked!$A$2:$A$' + str(lineNumber),
        'values':     '=TclassPeekStacked!$K$2:$K$' + str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'cyan'}
    })
    # Add a chart title and some axis labels.
    #chart2.set_title ({'name': 'Peek Stacked Chart'})
    chart2.set_title({'none': True})
    chart2.set_x_axis({'name': 'Time Tag'})
    chart2.set_y_axis({'name': 'Peek number'})
    
    # Set an Excel chart style.
    chart2.set_style(12)
    chart2.set_legend({'position': 'top'})
    chart2.set_size({'width': 600, 'height': 450})
    # Insert the chart into the worksheet (with an offset).
    worksheet.insert_chart('D3', chart2, {'x_offset': 25, 'y_offset': 10}) 
    
    test11(1, workbook, str(lineNumber), peektablelist ) 
    test11(2,workbook, str(lineNumber), peektablelist)
    test11(3,workbook, str(lineNumber), peektablelist) 
    test11(4,workbook, str(lineNumber), peektablelist)
    test11(5,workbook, str(lineNumber), peektablelist) 
    test11(6,workbook, str(lineNumber), peektablelist)
    test11(7,workbook, str(lineNumber), peektablelist) 
    test11(8,workbook, str(lineNumber), peektablelist)
    test11(9,workbook, str(lineNumber), peektablelist) 
    test11(10,workbook, str(lineNumber), peektablelist)    

    workbook.close() 
def test11(tclassnum, workbook, lineNumber, data):
    tclass = "TClassINFO" + str(0) + str(tclassnum)
    if(tclassnum==10):
        tclass = "TClassINFO"  + str(tclassnum)
    print str(tclassnum) + "___" + tclass + "-->" + str(workbook)
    worksheet21 = workbook.add_worksheet(tclass)
    bold = workbook.add_format({'bold': 1})
    # Add the worksheet1 data that the charts will refer to.
    headings = ['timetag', tclass]
    worksheet21.write_row('A1', headings, bold)
    worksheet21.write_column('A2', data[0])
    worksheet21.write_column('B2', data[tclassnum])
    
    chart21 = workbook.add_chart({'type': 'area'})    
    # Configure the TClassINFO01 series.
    if(tclassnum==1):
        chart21.add_series({
                            'name':       '=TClassINFO01!$B$1',
                            'categories': '=TClassINFO01!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO01!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'red'}
                            })
    elif(tclassnum==2):
        chart21.add_series({
                            'name':       '=TClassINFO02!$B$1',
                            'categories': '=TClassINFO02!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO02!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'blue'}
                            })
    elif(tclassnum==3):
        chart21.add_series({
                            'name':       '=TClassINFO03!$B$1',
                            'categories': '=TClassINFO03!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO03!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'yellow'}
                            })
    elif(tclassnum==4):
        chart21.add_series({
                            'name':       '=TClassINFO04!$B$1',
                            'categories': '=TClassINFO04!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO04!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'green'}
                            })
    elif(tclassnum==5):
        chart21.add_series({
                            'name':       '=TClassINFO05!$B$1',
                            'categories': '=TClassINFO05!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO05!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'brown'}
                            })
    elif(tclassnum==6):
        chart21.add_series({
                            'name':       '=TClassINFO06!$B$1',
                            'categories': '=TClassINFO06!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO06!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'orange'}
                            })
    elif(tclassnum==7):
        chart21.add_series({
                            'name':       '=TClassINFO07!$B$1',
                            'categories': '=TClassINFO07!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO07!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'pink'}
                            })
    elif(tclassnum==8):
        chart21.add_series({
                            'name':       '=TClassINFO08!$B$1',
                            'categories': '=TClassINFO08!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO08!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'lime'}
                            })
    elif(tclassnum==9):
        chart21.add_series({
                            'name':       '=TClassINFO09!$B$1',
                            'categories': '=TClassINFO09!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO09!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'purple'}
                            })
    elif(tclassnum==10):
        chart21.add_series({
                            'name':       '=TClassINFO10!$B$1',
                            'categories': '=TClassINFO10!$A$2:$A$' + str(lineNumber),
                            'values':     '=TClassINFO10!$B$2:$B$' + str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': 'cyan'}
                            })
    # Add a chart title and some axis labels.
    #chart21.set_title ({'name': 'Peek Stacked Chart'})
    chart21.set_title({'none': True})
    chart21.set_x_axis({'name': 'Time Tag'})
    chart21.set_y_axis({'name': 'Peek number'})
    
    # Set an Excel chart style.
    chart21.set_style(12)
    chart21.set_size({'width': 600, 'height': 450})
    chart21.set_legend({'position': 'top'})
    # Insert the chart into the worksheet1 (with an offset).
    worksheet21.insert_chart('D3', chart21, {'x_offset': 25, 'y_offset': 10})

if __name__ == "__main__":
    fpath = "D:\\report"
    for root, dirs, files in os.walk(fpath):
        for file in files:
            print file
            peektablelist = readpeek(fpath + "\\" + file)
            TClassPeek_area_stacked(peektablelist, fpath + "\\" + file)   