import pandas as pd
from flask import Flask ,  render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from flask import session as login_session
import json, urllib2

app = Flask(__name__)

# Taking input from user
#s1 = raw_input("Enter input to test raw_input() function: ")
#s1 = str(s1)
#s1 = s1.lower()
# words = []
# words = s1.split()
# print(words)
# print(s1)
# # Searching for buy keyword in the given query
# s2 = s1.find("buy")
# buying_query = 0
# selling_query = 0
#
# # If "buy" is found increase buying query to 1
# if s2!=-1:
# 	global buying
# 	buying_query = 1;
# # If "bought" is found increase buying query to 2
# s3 = s1.find("bought")
# if s3!=-1:
# 	buying_query = 2;
#
# # Searching for "sell" keyword in the given question.
# s4 = s1.find("sell")
#
# # If "sell" is found, increase the selling_query to 1.
# if s4!=-1:
#     selling_query = 1
#
# # Flag is used for checking. If flag == 1, its buying query. If flag == 2, its selling_queryself.
# # if Flag == 0. query is invalid
# flag = 0
# if selling_query == 1:
#     flag = 2
# elif buying_query>0:
#     flag=1
# print("here")
# if flag==2:
# 	print("sell")
#
# elif flag==1:
# 	print("BUY")
#
# else:
#     print("Invalid Query")
#
# df = pd.read_csv("companylist.csv")
# saved_column = df.Name #you can also use df['column_name']
# #print(type(saved_column))
# print(type(saved_column[1]))
# companies=[]
# list=[]
#
# for i in range(0,3482):
# 	z = saved_column[i].split()[0]
# 	z=z.split(',')[0]
# 	z=z.split('.')[0]
# 	list.append(z)
#
# print(list[0])
# company = ""
# for j in words:
# 	for k in list:
# 		k = k.lower()
# 		if k==j:
# 			company = j
# 			break
# print("ans")
# if company == "":
# 	flag = 4

# if flag == 4:

#print(company)
@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        query = request.form["query"]
        query = str(query)
        query = query.lower()
        words = []
        words = query.split()
        s2 = query.find("buy")
        buying_query = 0
        selling_query = 0

        # If "buy" is found increase buying query to 1
        if s2!=-1:
        	buying_query = 1;
        # If "bought" is found increase buying query to 2
        s3 = query.find("bought")
        if s3!=-1:
        	buying_query = 2;

        # Searching for "sell" keyword in the given question.
        s4 = query.find("sell")

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
        print("here")
        if flag==2:
        	print("sell")

        elif flag==1:
        	print("BUY")

        else:
            print("Invalid Query")

        df = pd.read_csv("companylist.csv")
        saved_column = df.Name
        company_tag = df.Symbol
        companies=[]
        list=[]

        for i in range(0,3482):
        	z = saved_column[i].split()[0]
        	z=z.split(',')[0]
        	z=z.split('.')[0]
        	list.append(z)
            	companies.append(company_tag[i])

        print(list[0])
        company = ""
        for j in words:
        	for k in range(0,3482):
        		list[k] = list[k].lower()
        		if list[k]==j:
        			company = j
        			break
        print("ans")
        if company == "":
        	flag = 4
        # if flag == 4

        print(companies[k])
        url = "https://stocknewsapi.com/api/v1?tickers="+companies[k]+"&items=50&token=2rxzbj7p0byo3112gizrcvauspbotqoztagzp5ij"
        sock = urllib2.urlopen(url)
        global json_obj
        json_obj=json.load(sock)
        objs = json_obj["data"]
        sentiments=[]
        n = len(objs)
        for i in range(0,n):
            sentiments.append(objs[i]["sentiment"])
        htmlsource = sock.read()
        json.load
        sock.close()
        return render_template("results.html",sentiments = sentiments)
    else:
        return render_template("home.html")

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
