# -*- coding: utf-8 -*-

import urllib.request
import re
import pytest
import os

"""Main module."""
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

