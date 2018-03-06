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

        
def parseInput(filename):
    """Read the file, if the file does not exist will return an error message."""
    if filename.startswith("http:"):
        uri=filename
        req=urllib.request.urlopen(uri)
        buffer=req.read().decode('utf-8')
    else:
        if os.path.exists(filename):
            buffer=open(filename).read().split("\n")
            size=int(buffer[0])
            instructions=[]
            for i in range(1,len(buffer)):
                pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
                l=pat.match(buffer[i])
                if l:
                    instructions.append(l)
        else:
            print("The file does not exits")
    return size,instructions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    N, instructions=parseInput(filename)
    led=LightTester(N)
    
