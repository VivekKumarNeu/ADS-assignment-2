import csv
import copy
import datetime
import os

def Select_Numeric_Day(date):   # calculating the numberic day
    day_dictionary = {'Sunday' : 0, 'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6}

    month, day, year = (int(x) for x in date.split('/'))
    ans = datetime.date(year, month, day)
    weekday_number = day_dictionary[ans.strftime("%A")]
    return weekday_number

def is_a_Weekend(date): # calculating if the day is a weekend
    weekend_selector = Select_Numeric_Day(date)
    if weekend_selector != 0:
        return 1;
    else:
        return 0;

def is_a_peakhour(hour):  # calculating if the hour is a peakhour
    if hour>=7 and hour<19:
        return 1
    else:
        return 0

path = 'E:/NEU/Sem 3/Data Science/Assignment 2/Assignment 2(1)/'
source_file1 = path+'rawData1.csv'  # reading input file 1
source_file2 = path+'rawData2.csv'  # reading input file 2
output = path+'output.csv'

files = os.listdir(path)    # removing if file exists
if 'output.csv' in files:
    os.remove(path+'output.csv')

flag = True
input_file_list = [source_file1,source_file2]

for source_file in input_file_list:     # opening file to read
    with open(source_file, "rb") as source_file:
        reader = csv.reader(source_file)
        with open(output, "a") as output_file:
            writer = csv.writer(output_file,lineterminator='\n')
            input_file_read = csv.reader(source_file);
            if flag:
                header = ["Account","Date","kWh","month","day","year","hour","Day of Week","Weekday","Peakhour"]    # adding header to csv
                writer.writerow(header)

            for rows in input_file_read:
                if rows[2] == 'MILDRED SCHOOL 1':   # getting data for only row with value as "MILDRED SCHOOL 1"
                    temp_row = []
                    temp_row.append(rows[0])
                    temp_row.append(rows[1])
                    date_split = rows[1].split('/') # splitting date for day,date,month
                    num_cols = len(reader.next())
                    i=0
                    sum=0
                    hours = 0
                    for cells in range(4,num_cols):
                        if((i / 12) == 0):
                            if(rows[cells] != ''):      # handling data not present
                                sum += float(rows[cells])
                            else:
                                sum +=0
                            i=i+1
                        else:
                            local_kwh = copy.deepcopy(temp_row)     # adding all the date from csv to list to write in csv
                            local_kwh.append(sum)
                            local_kwh.append(date_split[0])
                            local_kwh.append(date_split[1])
                            local_kwh.append(date_split[2])
                            local_kwh.append(hours)
                            local_kwh.append(Select_Numeric_Day(rows[1]))
                            local_kwh.append(is_a_Weekend(rows[1]))
                            local_kwh.append(is_a_peakhour(hours))
                            writer.writerow(local_kwh)
                            hours = hours+1
                            if(rows[cells] != ''):
                                sum = float(rows[cells])
                            else:
                                sum =0
                            i=1
                    local_kwh = copy.deepcopy(temp_row)
                    local_kwh.append(sum)
                    local_kwh.append(date_split[0])
                    local_kwh.append(date_split[1])
                    local_kwh.append(date_split[2])
                    local_kwh.append(hours)
                    local_kwh.append(Select_Numeric_Day(rows[1]))
                    local_kwh.append(is_a_Weekend(rows[1]))
                    local_kwh.append(is_a_peakhour(hours))
                    writer.writerow(local_kwh)
    flag = False
    source_file.close() # closing the file
    output_file.close()

