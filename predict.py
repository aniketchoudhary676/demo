import pandas as pd
import numpy as np

df = pd.read_csv('predict.csv')
print(df.to_string())
print('-' * 150)
df['Calender_Date'] = pd.to_datetime(df.Calender_Date, format = '%d/%m/Y')
df['Calender_Date'] = df['Calender_Date'].dt.strftime('%Y-%m-%d')
df['Calender_Date'] = pd.to_datetime(df['Calender_Date'])
df['Weekend'] = df['Calender_Date'].dt.weekday > 4

df['New_Revenue'] = np.where(df['Weekend'],0,df['Total_Revenue'])

print(df.to_string())

#df.to_csv(r'C:\Users\achaud12\PycharmProjects\pythonProject\file.csv')
