'''
Created on Dec 21, 2015

@author: joy
'''
import xlsxwriter
import os

def readtps(file):
    tpsFile = open(file,"r")
    #print tpsFile
    timetaglist=[]
    trancountlist=[]
    tpslist=[]
    tpstablelist=[]
    for line in tpsFile:
        linetmp=line[:-1]
        timetaglist.append(linetmp.split(",")[0])
        trancountlist.append(float(linetmp.split(",")[1])) 
        tpslist.append(float(linetmp.split(",")[2]))
    tpstablelist.append(timetaglist)
    tpstablelist.append(trancountlist)
    tpstablelist.append(tpslist)
    return tpstablelist
    
def tps_line(tpstablelist,file):
    print file
    workbook = xlsxwriter.Workbook(file + ".chart_tps_line.xlsx")
    worksheet = workbook.add_worksheet('TPS')  
    bold = workbook.add_format({'bold': 1})    
    
    # Add the worksheet data that the charts will refer to.
    headings = ['Timetag', 'Trancount', 'Tps']
    data = tpstablelist
    worksheet.write_row('A1', headings, bold)
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    chart2 = workbook.add_chart({'type': 'line'})
    # Configure tps series.
    lineNumber = len(data[0])
    chart2.add_series({
        'name':       '=TPS!$C$1',
        'categories': '=TPS!$A$2:$A$' + str(lineNumber),
        'values':     '=TPS!$C$2:$C$' + str(lineNumber),
        'line':   {'color': 'red','width': 2.25}
    })
    '''
    chart2.add_series({
        'values':     '=TPS!$C$2:$C$3910',
        'trendline': {'type': 'linear',
                      'name': 'trendline linear',
                      'line': {'color': 'black','width': 1,'dash_type': 'long_dash',},
                      'DisplayEquation':True
                      },
    })'''
    # Add a chart title and some axis labels.
    #chart2.set_title ({'name': 'Peek Stacked Chart'})
    chart2.set_title({'none': True})
    chart2.set_x_axis({'name': 'Time Tag'})
    chart2.set_y_axis({'name': 'Tps'})
    # Set an Excel chart style.
    chart2.set_style(12)
    chart2.set_size({'width': 600, 'height': 450})
    chart2.set_legend({'position': 'top'})
    # Insert the chart into the worksheet (with an offset).
    worksheet.insert_chart('D3', chart2, {'x_offset': 25, 'y_offset': 10})
    workbook.close() 

if __name__ == "__main__":
    fpath = "D:\\tps"
