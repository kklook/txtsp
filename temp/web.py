#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template,make_response,Response
import os
from werkzeug.routing import BaseConverter
import base64
class RC(BaseConverter):
    def __init__(self,map,*args):
        self.map=map
        self.regex=args[0]
app=Flask(__name__)
app.url_map.converters['regex']=RC
@app.route('/', methods=['GET', 'POST'])
def home():
    filelist=[]
    for temp in os.listdir(os.getcwd()+'/'+'static'):
        if temp.find('.')==-1 and temp!='static':
            filelist.append(temp)
    namelist=[]
    for t in filelist:
        with open('static'+'/'+t+'/'+'name.txt','r') as f:
            namelist.append(f.read())
    if(len(namelist)==len(filelist)):
        return render_template('home.html',dirlist=filelist,namelist=namelist,lenth=len(namelist))
    else:
        return None
@app.route('/<regex("\d{4}"):url>')
def imagepage(url):
    filepath=os.getcwd()+'/'+'static'+'/'+url+'/'
    name=None
    imagelist=[]
    with open(filepath+'name.txt','r') as f:
        name=f.read()
    for n in os.listdir(filepath):
        if n!='name.txt':
            imagelist.append(url+'/'+n)
    path='static'
    return render_template('a.html',name=name,imagelist=imagelist,path=path)
@app.route('/<regex("\d{4}"):url>/<regex("\d*"):filename>')
def image(url,filename):
    with open('static'+'/'+url+'/'+filename+'.jpg','rb') as f:
        img=f.read()
    return Response(img,mimetype='image/jpeg')
if __name__=='__main__':
    app.run(debug=True)