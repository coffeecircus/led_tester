# -*- coding: utf-8 -*-

import urllib.request
import re
import pytest
import os
import argparse
import numpy as np

"""Main module."""

class LightTester:
    lights=None
    def __init__(self,N):
        self.size=N
        self.lights=np.zeros((N,N),dtype=bool)
        
    def apply(self,cmd,x1,y1,x2,y2):
        if cmd=="turn on":
            self.lights[x1:x2+1,y1:y2+1]=True
        elif cmd=="turn off":
            self.lights[x1:x2+1,y1:y2+1]=False
        elif cmd=="switch":
            self.lights[x1:x2+1,y1:y2+1]^=True
           
def getInstructions(buffer):
    ins=[]
    for i in range(1,len(buffer)):
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        l=pat.match(buffer[i])
        if l:
            ins.append(l)               
    return ins

def parseInput(filename):
    """Read the file, if the file does not exist will return an error message."""
    size_input=0
    instructions=[]
    if filename.startswith("http:"):
        try:
            uri=filename
            req=urllib.request.urlopen(uri)
            buffer=req.read().decode('utf-8').split("\n")
            size_input=int(buffer[0])
            instructions=getInstructions(buffer)
        except urllib.error.HTTPError:
            print("The URL is Error")
    else:
        if os.path.exists(filename):
            buffer=open(filename).read().split("\n")
            size_input=int(buffer[0])
            instructions=getInstructions(buffer)
        else:
            print("The file does not exits")
    return size_input,instructions

def checkRange(x1,x2,y1,y2,N):
    '''Make the region valid'''
    a1,a2,b1,b2=x1,x2,y1,y2
    a1=min(max(0,a1),N-1)
    a2=min(max(0,a2),N-1)
    b1=min(max(0,b1),N-1)
    b2=min(max(0,b2),N-1)
    if a1>a2:
        a1,a2=a2,a1
        b1,b2=b2,b1
    elif a1==a2 and b1>b2:
        b1,b2=b2,b1
    return(a1,a2,b1,b2)
        
def main():
    x1,x2,y1,y2=0,0,0,0
    cmd=[]
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    N, instruction=parseInput(filename)
    led=LightTester(N)
    length=len(instruction)
    for i in range(length):
        cmd=instruction[i][1]
        x1=int(instruction[i][2])
        y1=int(instruction[i][3])
        x2=int(instruction[i][4])
        y2=int(instruction[i][5])
        x1,x2,y1,y2=checkRange(x1,x2,y1,y2,N)
        led.apply(cmd,x1,y1,x2,y2)
    ans=np.sum(led.lights==1)
    print("There are ",ans,' lights on. ')

if __name__=="__main__":
	main()
