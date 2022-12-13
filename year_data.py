import pandas as pd

def avg_PM_2013():
    average=[]
    for rows in pd.read_csv(f'AQI/aqi2013.csv',chunksize=24):
        add_var=0
        avg=0
        ls=[]
        df=pd.DataFrame(data=rows)
        for _,rows in df.iterrows():
            ls.append(rows['PM2.5'])
            
        for i in ls:
            if type(i) is int or type(i) is float:
                add_var+=i
            elif i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                add_var+=float(i)
                
        avg=add_var/24
        average.append(avg)
    return average

def avg_PM_2014():
    average=[]
    for rows in pd.read_csv(f'AQI/aqi2014.csv',chunksize=24):
        add_var=0
        avg=0
        ls=[]
        df=pd.DataFrame(data=rows)
        for _,rows in df.iterrows():
            ls.append(rows['PM2.5'])
            
        for i in ls:
            if type(i) is int or type(i) is float:
                add_var+=i
            elif i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                add_var+=float(i)
                
        avg=add_var/24
        average.append(avg)
    return average

def avg_PM_2015():
    average=[]
    for rows in pd.read_csv(f'AQI/aqi2015.csv',chunksize=24):
        add_var=0
        avg=0
        ls=[]
        df=pd.DataFrame(data=rows)
        for _,rows in df.iterrows():
            ls.append(rows['PM2.5'])
            
        for i in ls:
            if type(i) is int or type(i) is float:
                add_var+=i
            elif i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                add_var+=float(i)
                
        avg=add_var/24
        average.append(avg)
    return average

def avg_PM_2016():
    average=[]
    for rows in pd.read_csv(f'AQI/aqi2016.csv',chunksize=24):
        add_var=0
        avg=0
        ls=[]
        df=pd.DataFrame(data=rows)
        for _,rows in df.iterrows():
            ls.append(rows['PM2.5'])
            
        for i in ls:
            if type(i) is int or type(i) is float:
                add_var+=i
            elif i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                add_var+=float(i)
                
        avg=add_var/24
        average.append(avg)
    return average

def avg_PM_2017():
    average=[]
    for rows in pd.read_csv(f'AQI/aqi2017.csv',chunksize=24):
        add_var=0
        avg=0
        ls=[]
        df=pd.DataFrame(data=rows)
        for _,rows in df.iterrows():
            ls.append(rows['PM2.5'])
            
        for i in ls:
            if type(i) is int or type(i) is float:
                add_var+=i
            elif i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                add_var+=float(i)
                
        avg=add_var/24
        average.append(avg)
    return average

def avg_PM_2018():
    average=[]
    for rows in pd.read_csv(f'AQI/aqi2018.csv',chunksize=24):
        add_var=0
        avg=0
        ls=[]
        df=pd.DataFrame(data=rows)
        for _,rows in df.iterrows():
            ls.append(rows['PM2.5'])
            
        for i in ls:
            if type(i) is int or type(i) is float:
                add_var+=i
            elif i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                add_var+=float(i)
                
        avg=add_var/24
        average.append(avg)
    return average