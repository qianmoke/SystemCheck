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
    
def peekChartAll(workbook, worksheet, lineNumber):
    chart2 = workbook.add_chart({'type': 'area', 'subtype': 'stacked'})
    # Configure the '+TClassINFO+' series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$B$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$B$2:$B$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'cyan'}
    })    
    # Configure TClassINFO02 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$C$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$C$2:$C$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': '#B22222'}
    })
    # Configure TClassINFO03 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$D$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$D$2:$D$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'yellow'}
    })    
    # Configure TClassINFO04 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$E$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$E$2:$E$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'green'}
    })
    # Configure TClassINFO05 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$F$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$F$2:$F$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'brown'}
    })    
    # Configure TClassINFO06 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$G$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$G$2:$G$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': '#FF9912'}
    })
    # Configure the TClassINFO07 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$H$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$H$2:$H$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': '#F0E68C'}
    })    
    # Configure TClassINFO08 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$I$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$I$2:$I$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'red'}
    })
    # Configure TClassINFO09 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$J$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$J$2:$J$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'purple'}
    })    
    # Configure TClassINFO10 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$K$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$K$2:$K$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'orange'}
    })
    # Configure the BANCS000 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$L$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$L$2:$L$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'lime'}
    })    
    # Configure CMS00000 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$M$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$M$2:$M$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'pink'}
    })
    # Configure HDQS0000 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$N$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$N$2:$N$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': 'blue'}
    })    
    # Configure RCPS0001 series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$O$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$O$2:$O$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': '#FFD700'}
    })
    # Configure '+TClassINFO+' series.
    chart2.add_series({
        'name':       '=TclassPeekStacked!$P$1',
        'categories': '=TclassPeekStacked!$A$2:$A$'+ str(lineNumber),
        'values':     '=TclassPeekStacked!$P$2:$P$'+ str(lineNumber),
        'line':   {'none': True},
        'fill':   {'color': '#B03060'}
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
