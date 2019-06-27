import pandas as pd

# Taking input from user
s1 = raw_input("Enter input to test raw_input() function: ")
s1.lower()
# Searching for buy keyword in the given query
s2 = s1.find("buy")
buying_query = 0
selling_query = 0

# If "buy" is found increase buying query to 1
if s2!=-1:
	global buying
	buying_query = 1;
# If "bought" is found increase buying query to 2
s3 = s1.find("bought")
if s3!=-1:
	buying_query = 2;

# Searching for "sell" keyword in the given question.
s4 = s1.find("sell")

# If "sell" is found, increase the selling_query to 1.
if s4!=-1:
    selling_query = 1

# Flag is used for checking. If flag == 1, its buying query. If flag == 2, its selling_queryself.
# if Flag == 0. query is invalid
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

