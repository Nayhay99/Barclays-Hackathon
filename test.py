import pandas as pd
df = pd.read_csv("companylist.csv")
saved_column = df.Name #you can also use df['column_name']
print(type(saved_column))
print(type(saved_column[1]))
list=[]
for i in range(0,3482):
    z = saved_column[i].split()[0]
    z = z.split(',')[0]
    list.append(z)
print(list[0])
