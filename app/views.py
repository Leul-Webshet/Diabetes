from curses import REPORT_MOUSE_POSITION
from pyexpat import model
import re
from statistics import mode
from telnetlib import BM
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
from numpy import result_type

model=load('model/model.joblib')
# Create your views here.

def predict(request):
    if request.method=='POST':
        Pregnancies=request.POST['Pregnancies']
        Glucose=request.POST['Glucose']
        BloodPressure=request.POST['BloodPressure']
        SkinThickness=request.POST['SkinThickness']
        Insulin=request.POST['Insulin']
        BMI=request.POST['BMI']
        DiabetesPedigreeFunction=request.POST['DiabetesPedigreeFunction']
        Age=request.POST['DiabetesPedigreeFunction']

        BloodPressure=request.POST['BloodPressure']
        Age=request.POST['DiabetesPedigreeFunction']
        y_predict=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if y_predict[0]==0:
            y_predict='No Diabetes'
        else:
            y_predict='Diabetes'
        return render(request,'index.html',{'result':y_predict})

    return render(request,'index.html')

def info(request):
    return render(request,'info.html')