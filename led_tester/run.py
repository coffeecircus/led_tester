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
           
def getInstructions(buffer):
    ins=[]
    for i in range(1,len(buffer)):
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        l=pat.match(buffer[i])
        if l:
            ins.append(l)
    return ins

def parseInput(filename):
    size_input=0
    instructions=[]
    """Read the file, if the file does not exist will return an error message."""
    if filename.startswith("http:"):
        uri=filename
        req=urllib.request.urlopen(uri)
        buffer=req.read().decode('utf-8').split("\n")
        size_input=int(buffer[0])
        instructions=getInstructions(buffer)
    else:
        if os.path.exists(filename):
            buffer=open(filename).read().split("\n")
            size_input=int(buffer[0])
            instructions=getInstructions(buffer)
        else:
            print("The file does not exits")
    return size_input,instructions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    N, instructions=parseInput(filename)
    led=LightTester(N)
    length=len(instructions)
    for i in len:
        cmd=instruction[i][0]
        x1=int(instruction[i][1])
        y1=int(instruction[i][2])
        x2=int(instruction[i][3])
        x2=int(instruction[i][4])
        
    
