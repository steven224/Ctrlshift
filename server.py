# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:03:26 2019

@author: sfsong
"""
import numpy as np
from flask import Flask, request, jsonify
import pickle
import json
app = Flask(__name__)




@app.route('/api',methods=['POST','GET'])
def predict():
     if request.method == 'POST': 
         InNumber=request.form['InNumber'] 
         with open(r"xgboost.pickle", "rb") as input_file:
             model= pickle.load(input_file)
         InNumber=numsort(InNumber) 

         return render_template('test.html',result=InNumber) 
     else:  
         return render_template('test.html') 

def numsort(number):
    print(number)
#    tmp=number.split(' *')
    tmp=re.split("\s+",number)
    print(tmp)
    for i in range(len(tmp)):
        tmp[i]=int(tmp[i])
    print(tmp)
    tmp.sort()
    res=""
    for i in tmp:
        res+=(str(i)+" ")
    return res

    
   
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)