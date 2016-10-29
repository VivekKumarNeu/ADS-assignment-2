import pandas as pd
from pandas import DataFrame,read_csv
import numpy as np
st=pd.read_csv('forecastData.csv')
# df2=pd.DataFrame(np.array(st[['Time','TemperatureF','Dew_PointF','Humidity','Sea_Level_PressureIn','VisibilityMPH','Wind_Direction','Wind_SpeedMPH','Gust_SpeedMPH','PrecipitationIn','Events','Conditions','WindDirDegrees']]))
df2=pd.DataFrame()
df2['Date']=pd.DatetimeIndex(st['Time']).date
df2['month']=pd.DatetimeIndex(st['Time']).month
df2['Day']=pd.DatetimeIndex(st['Time']).day
df2['Year']=pd.DatetimeIndex(st['Time']).year
df2['hour']=pd.DatetimeIndex(st['Time']).hour
df2['Peakhour']=[1 if (x >=7 and x <19 ) else 0 for x in pd.DatetimeIndex(st['Time']).hour]
# df2['DayOfWeek']=pd.DatetimeIndex(st['Time']).dayofweek
# df2['WeekDay']=[0 if (x == 0 or x == 6) else 1 for x in pd.DatetimeIndex(st['Time']).weekday]
df2['Temperature']=st['TemperatureF']
df2['Dew_PointF']=st['Dew_PointF']
df2['Humidity']=st['Humidity']
# df2['Sea_Level_PressureIn']=st['Sea_Level_PressureIn']
# df2['VisibilityMPH']=st['VisibilityMPH']
# df2['Wind_Direction']=st['Wind_Direction']
# df2['Wind_SpeedMPH']=st['Wind_SpeedMPH']
# df2['PrecipitationIn']=st['PrecipitationIn']
# df2['Events']=st['Events']
# df2['Conditions']=st['Conditions']
# df2['WindDirDegrees']=st['WindDirDegrees']
# df2.set_index('Date',inplace=True)
grouped=df2.groupby(['Date','month','Day','Year','hour'])
df3=grouped.mean()
df3.to_csv('forecastInput.csv',index=True)
# df5=pd.read_csv('output.csv')
# st=pd.read_csv('RegOutputs.csv')
# outerList=['Day','Hr','Temp','KWH']
# mainList=[]
# # mainList.append(outerList)
# for index, row in st.iterrows():
#     # print row['Account No'], row['Constant']
#     outputList = []
#     print(type(row))
#     for insideIndex,insideRow in df5.iterrows():
#         outputList.insert(outerList.index("Day"), insideRow["Date"])
#         outputList.insert(outerList.index("Hr"), insideRow["Hour"])
#         tempValue=insideRow["TemperatureF"]
#         outputList.insert(outerList.index("Temp"), tempValue)
#         kwhValue=row['Constant']+(row['TemperatureF']*insideRow['TemperatureF'])+(row['Dew_PointF']*insideRow['Dew_PointF'])+\
#                  (row['Humidity']*insideRow['Humidity'])+(row['Sea_Level_PressureIn']*insideRow['Sea_Level_PressureIn'])+\
#                  (row['VisibilityMPH']*insideRow['VisibilityMPH'])+(row['PrecipitationIn']*insideRow['PrecipitationIn'])\
#                  +(row['WindDirDegrees']*insideRow['WindDirDegrees'])
#         outputList.insert(outerList.index("KWH"), kwhValue)
#         mainList.append(outputList)
#         outputList = []
#     df4=DataFrame(mainList,columns=outerList)
#     df4.to_csv('forecastOutput_'+str(row['Account No'])+'.csv')