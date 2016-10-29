import requests
import pandas as pd
from dateutil import parser, rrule
import time
import urllib2
import json

url_hit_count = 0   # to keep track of API hits ; to find thread sleep
path = 'E:/NEU/Sem 3/Data Science/Assignment 2/Assignment 2(1)/'
df = pd.DataFrame(columns=['year','month','day','hour','Temperature','Dew_PointF','Humidity','Sea_Level_PressureIn','VisibilityMPH','Wind_Direction','Wind_SpeedMPH','Conditions','WindDirDegrees'])
    # adding headers to the dataframe

def get_required_data(day,month,year):
    global url_hit_count
    url_hit_count = url_hit_count + 1   # increasing url_hit_count on every date call
    if url_hit_count % 10 ==0:      # if 10 calls, sleep
        time.sleep(62)
    try:
        url = 'http://api.wunderground.com/api/e40332dbb6c58359/history_{y}{m}{d}/q/MA/Boston.json'
        url = url.format(y = year,m = month, d = day)
        response = urllib2.urlopen(url) # reading data from urllib
        data = json.load(response)


        global df
        total_rows = len(data["history"]["observations"])
        for i in range(total_rows):
            hour_data = []
            hour_data.append(int(data["history"]["observations"][i]['date']['year']))   # gathering data from json
            hour_data.append(int(data["history"]["observations"][i]['date']['mon']))
            hour_data.append(int(data["history"]["observations"][i]['date']['mday']))
            hour_data.append(int(data["history"]["observations"][i]['date']['hour']))
            hour_data.append(float(data["history"]["observations"][i]['tempi']))
            hour_data.append(float(data["history"]["observations"][i]['dewpti']))
            hour_data.append(float(data["history"]["observations"][i]['hum']))
            hour_data.append(float(data["history"]["observations"][i]['pressurei']))
            hour_data.append(float(data["history"]["observations"][i]['visi']))
            hour_data.append(str(data["history"]["observations"][i]['wdire']))
            hour_data.append(float(data["history"]["observations"][i]['wspdi']))
            hour_data.append(str(data["history"]["observations"][i]['conds']))
            hour_data.append(float(data["history"]["observations"][i]['wdird']))


            df = df.append(pd.Series([hour_data[0],hour_data[1],hour_data[2],hour_data[3],hour_data[4],hour_data[5],hour_data[6],hour_data[7],
                                  hour_data[8],hour_data[9],hour_data[10],hour_data[11],hour_data[12]], index=['year','month','day','hour','Temperature','Dew_PointF','Humidity','Sea_Level_PressureIn','VisibilityMPH','Wind_Direction','Wind_SpeedMPH','Conditions','WindDirDegrees'
                      ]), ignore_index=True)    # appending the data in dataframe
    except:
            df.to_csv(path+'temp.csv', index=False)  # creating the temp file with existing dataframe data if any failure occures while gathering the data


start_date = "2014-01-01"   # desired starting date
end_date = "2014-12-31"     # desired ending date
start = parser.parse(start_date)
end = parser.parse(end_date)
dates = list(rrule.rrule(rrule.DAILY, dtstart=start, until=end))    # generating the dates between starting and ending date

for d in dates:
    get_required_data("%02d" %(d.day),"%02d" %(d.month),"%02d" %(d.year))   # calling function to get data from API

grouped=df.groupby(['year','month','day','hour'],as_index=False)
df3=grouped.mean()  # computing mean
df4=grouped.agg({'Conditions':lambda x:', '.join(x),
                 'Wind_Direction':lambda x:', '.join(x)})       # concatenating conditions and wind_directions data
df3['Conditions']=df4['Conditions']     # copying conditions data to original dataframe
df3['Wind_Direction']=df4['Wind_Direction']     # copying wind_direction data to original dataframe
df3.to_csv(path+'api_full_data.csv', index=False)