# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 11:28:41 2017

@author: Luddite
"""

import tushare as ts
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import dates

class tickData:    
    def __init__(self,code,date):
        self.code=code;
        self.date=date;
        if(str(dt.date.today())==date):
            self.data=ts.get_today_ticks(code);
        else:
            self.data=ts.get_tick_data(code,date);
        
    def stringToFloatDate(self,myString):
        myDate=dt.datetime.strptime(myString, '%H:%M:%S');
        return dates.date2num(myDate);
       
    def plotTickLine(self):
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
        plt.xticks(rotation=45)
        plt.plot(self.data.time.map(self.stringToFloatDate), self.data.price)
        fig.savefig(self.code+'_'+self.date+'.png')
        