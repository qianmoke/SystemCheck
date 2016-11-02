'''
Created on Dec 21, 2015

@author: joy
'''
def tpsChart(workbook,worksheet,lineNumber):
    chart3 = workbook.add_chart({'type': 'line'})

    chart3.add_series({
        'name':       '=Tps!$C$1',
        'categories': '=Tps!$A$2:$A$' + str(lineNumber),
        'values':     '=Tps!$C$2:$C$' + str(lineNumber),
        'line':   {'color': 'red','width': 2.25}
    })
    # Add a chart title and some axis labels.
    #chart2.set_title ({'name': 'Peek Stacked Chart'})
    chart3.set_title({'none': True})
    chart3.set_x_axis({'name': 'Time Tag'})
    chart3.set_y_axis({'name': 'Tps'})
    # Set an Excel chart style.
    chart3.set_style(12)
    chart3.set_size({'width': 600, 'height': 450})
    chart3.set_legend({'position': 'top'})
    worksheet.insert_chart('D3', chart3, {'x_offset': 25, 'y_offset': 10})
    
def peekChartAll(workbook, worksheet, lineNumber, clomCount):
    chart2 = workbook.add_chart({'type': 'area', 'subtype': 'stacked'})
    # Configure the '+TClassINFO+' series.
    colorList=['cyan','#B22222','yellow','green','brown','#FF9912','#F0E68C','red','purple','orange','lime','pink','blue','#FFD700','#B03060']
    clomChar=['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    for clom in xrange(0,clomCount-1):
        chart2.add_series({
            'name':       '=TclassPeekStacked!$'+clomChar[clom]+'$1',
            'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
            'values':     '=TclassPeekStacked!$'+clomChar[clom]+'$2:$'+clomChar[clom]+'$'+ str(lineNumber),
            'line':   {'none': True},
            'fill':   {'color': colorList[clom]}
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
    

def peekChartOne(TClassINFO, tclassnum, workbook,worksheet,lineNumber):
    chart21 = workbook.add_chart({'type': 'area'})    
    # Configure the '+TClassINFO+' series.
    colorList=['cyan','#B22222','yellow','green','brown','#FF9912','#F0E68C','red','purple','orange','lime','pink','blue','#FFD700','#B03060']
    chart21.add_series({
                            'name':       '='+TClassINFO+'!$B$1',
                            'categories': '='+TClassINFO+'!$A$2:$A$'+ str(lineNumber),
                            'values':     '='+TClassINFO+'!$B$2:$B$'+ str(lineNumber),
                            'line':   {'none': True},
                            'fill':   {'color': colorList[tclassnum]}
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
    worksheet.insert_chart('D3', chart21, {'x_offset': 25, 'y_offset': 10})
