# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 15:27:00 2017

@author: 丁思凡
"""

import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import dates
from matplotlib.finance import candlestick_ohlc

class historyData:    
    def __init__(self,code,startTime,endTime):
        self.code=code;
        self.start=startTime;
        self.end=endTime;
        self.data=ts.get_hist_data(code,start=startTime,end=endTime);
        self.ohlc = zip(self.data.index.map(self.stringToFloatDate),self.data.open,self.data.high,self.data.low,self.data.close)
     
    def stringToFloatDate(self,myString):
        myDate=datetime.strptime(myString, '%Y-%m-%d');
        return dates.date2num(myDate);
     
    def plotCandleStick(self):
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        fig.set_figheight(7)
        fig.set_figwidth(15)
        ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)
        candlestick_ohlc(ax,self.ohlc,width =0.4,colorup='#77d879',colordown='#db3f3f')
        fig.savefig(self.code+'_'+self.start+'_'+self.end+'.png')
        
    def plotCloseLine(self):
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        fig.set_figheight(7)
        fig.set_figwidth(15)
        ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)
        plt.plot(self.data.index.map(self.stringToFloatDate), self.data.close)
        fig.savefig(self.code+'_'+self.start+'_'+self.end+'.png')
        