import pandas as pd

s1 = raw_input("Enter input to test raw_input() function: ")
print('\n')
s2 = s1.find("buy")
buying_query = 0
selling_query = 0
if s2!=-1:
	global buying
	buying_query = 1;
s3 = s1.find("bought")
if s3!=-1:
	buying_query = 2;
s4 = s1.find("sell")
if s4!=-1:
    selling_query = 1
flag = 0
if selling_query == 1:
    flag = 2
elif buying_query>0:
    flag=1
       




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

