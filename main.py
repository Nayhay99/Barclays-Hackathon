import pandas as pd
from flask import Flask ,  render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from flask import session as login_session
import json, urllib2

app = Flask(__name__)

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
        verb = ""
        if selling_query == 1:
            flag = 2
        elif buying_query>0:
            flag=1
        #print("here")
        if flag==2:
        	verb = "sell"

        elif flag==1:
        	verb ="buy"

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
        if company == "":
        	flag = 4
        # if flag == 4

        #print(companies[k])
        url = "https://stocknewsapi.com/api/v1?tickers="+companies[k]+"&items=50&token=dnsuyargynbavxxgytnvdzpbars91wp9s4bidzl1"
        sock = urllib2.urlopen(url)
        global json_obj
        json_obj=json.load(sock)
        objs = json_obj["data"]
        sentiments=[]
        ans = 0
        n = len(objs)

        for i in range(0,n):
            sentiments.append(objs[i]["sentiment"])
            if objs[i]["sentiment"] == "Positive" :
                ans = ans+1
            elif objs[i]["sentiment"] == "Negative":
                ans=ans-1
            else:
                ans=ans
        htmlsource = sock.read()
        json.load
        sock.close()
        new1=""
        news2=""
        if ans>0:
            url = "https://stocknewsapi.com/api/v1?tickers="+companies[k]+"&items=2&sentiment=positive&token=dnsuyargynbavxxgytnvdzpbars91wp9s4bidzl1"
            sock = urllib2.urlopen(url)
            json_obj=json.load(sock)
            news1 = json_obj["data"][0]["title"]
            news2 = json_obj["data"][1]["title"]
        if ans<0:
            url = "https://stocknewsapi.com/api/v1?tickers="+companies[k]+"&items=2&sentiment=negative&token=dnsuyargynbavxxgytnvdzpbars91wp9s4bidzl1"
            sock = urllib2.urlopen(url)
            json_obj=json.load(sock)
            news1 = json_obj["data"][0]["title"]
            news2 = json_obj["data"][1]["title"]
        else:
            url = "https://stocknewsapi.com/api/v1?tickers="+companies[k]+"&items=2&sentiment=neutral&token=dnsuyargynbavxxgytnvdzpbars91wp9s4bidzl1"
            sock = urllib2.urlopen(url)
            json_obj=json.load(sock)
            news1 = json_obj["data"][0]["title"]
            news2 = json_obj["data"][1]["title"]


        sentiments=[]
        ans = 0
        n = len(objs)
        return render_template("results.html",news1=news1,news2=news2,verb=verb, ans=ans, sentiments = sentiments,company = company)
    else:
        return render_template("home.html")

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
