# -*- coding: utf-8 -*-
"""
First created on Fri Mar 23 12:19:32 2018 (since updated)

@author: Baptiste Higgs
"""

from GridEyeKit import GridEYEKit
import time
import numpy as np
import keyboard
import json


import pickle
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd


def openClassifier(fileName):
    with open(fileName, "rb") as myFile:
        return pickle.load(myFile)


def timestamp():
    """
    return the current date and time 
    up to millisecond resolution
    requires time module
    """
    now = time.time()
    localtime = time.localtime(now)
    milliseconds = '%03d' % int((now - int(now)) *1000)
    return time.strftime('%Y-%m-%d %H:%M:%S.', localtime) + milliseconds


def checkClassifications():
    # "temps": [[int(num*4) for num in tempList] for tempList in therm_array.tolist()]
    #get an 8x8 matrix (2d list)
    therm_array = g.get_temperatures()
    therm_array = np.flip(therm_array,1)

    


logRegClassifier = openClassifier("logisticRegression_Ishaan.pkl")
svmClassifier = openClassifier("supportVectorMachine_Aiden.pkl")
nNetClassifier = openClassifier("neuralNetwork_Baptiste.pkl")

print("Connecting to grideye...\n")

g_status_connect = False
attempts = 0
while not g_status_connect:
    try:
        print("attempt {}".format(attempts))
        g = GridEYEKit()
        g_status_connect = g.connect()
        break
    except Exception as e:
        attempts += 1 
        print("attempt {} failed".format(attempts))
        g.close()

print("Connected\n")

while True:
    checkClassifications()