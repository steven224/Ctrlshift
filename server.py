# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:03:26 2019

@author: sfsong
"""
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify,render_template
from flask import Flask
import pickle
import json
import datetime
app = Flask(__name__)




@app.route('/impressions',methods=['POST','GET'])
def predict():
     if request.method == 'POST': 
         total_spend_cpm=request.form['total_spend_cpm']
         D2FD=request.form['D2FD']
         Goal_type=request.form['Goal_type']
         Country=request.form['Country']
         Date=request.form['Date']
         Channel=request.form['Channel']
         BV=request.form['Business_vertical']
         
         cate=[Goal_type,Country,Channel,BV]
       
         
         inputdf=pd.DataFrame(columns=['total_spend_cpm','D2FD','type0','type1','type2','Australia','Hong Kong','Indonesia',
 'Malaysia','New Zealand','Philippines','Somalia','reserved/private','Friday','Monday','Saturday','Sunday','Thursday',
 'Tuesday','Wednesday','Display','Mobile','channelunknown','Finance','bvunknown'])
        
         for a in cate:
             for i in inputdf.columns:
                 if a==i:
                     inputdf.loc[0,[i]]=1
                    
         
         inputdf.loc[0,['total_spend_cpm']]=total_spend_cpm
         inputdf.loc[0,['D2FD']]=D2FD
                
         
         
         
         Date=pd.to_datetime(Date)
         weekday=Date.strftime('%A')
         for i in inputdf.columns:
             if weekday==i:
                     inputdf.loc[0,[i]]=1
         
         
         inputdf=inputdf.fillna(0)   
         inputf=np.array([inputdf.iloc[0,:].tolist()])
         
         with open(r"xgboost.pickle", "rb") as input_file:
             model= pickle.load(input_file)
             
         prediction=model.predict(inputf)
         
         #click prediction
         impressions=pd.DataFrame(prediction,columns=['impressions'])
         inputclass=pd.concat([impressions,inputdf],axis=1)
         with open(r"clf.pickle", "rb") as input_file:
             class_model= pickle.load(input_file)
         with open(r"rftrain_click.pickle", "rb") as input_file:
             regress_model= pickle.load(input_file)
        
         def predic_click(inputclass):
             if class_model.predict(inputclass)==0:
                 click_result=0
             else:
                 click_result=regress_model.predict(inputclass)
             return click_result
         
         click_result=predic_click(inputclass)
         
         
         
         
         
         return render_template('test.html',result=prediction, click_result=click_result) 
     else:  
         return render_template('test.html') 


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    
@app.route('/clicks',methods=['POST','GET'])
def predict():
     if request.method == 'POST':
         
         
         
         
         
         return render_template('clicks.html')
if __name__ == '__main__':
    app.run(port=5000, debug=True)    
    
