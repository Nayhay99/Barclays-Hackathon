#import packages
import pandas as pd
import numpy as np

#for normalizing data
#from sklearn.preprocessing import MinMaxScaler
#scaler = MinMaxScaler(feature_range=(0, 1))

#read the file
df = pd.read_csv('MSFT.csv')

#print the head
print(df.head())


#setting index as date
df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index = df['Date']

print(df.index)

data = df.sort_index(ascending=True, axis=0)
print(data.head())
new_data = pd.DataFrame(index=range(0,len(df)),columns=['Date', 'Close'])

for i in range(0,len(data)):
     new_data['Date'][i] = data['Date'][i]
     new_data['Close'][i] = data['Close'][i]

train = new_data[:251]
valid = new_data[251:]

print(new_data.shape)
print(train.shape)
print(valid.shape)

print(train['Date'].min())
print(train['Date'].max())
print(valid['Date'].min())
print(valid['Date'].max())


preds = []
for i in range(0,1):
    a = train['Close'][len(train)-251+i:].sum() + sum(preds)
    b = a/251
    preds.append(b)

#print(valid["Close"])
print(preds)
