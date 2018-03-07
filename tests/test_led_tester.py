#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import pytest
import numpy as np
from click.testing import CliRunner
from led_tester import run


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    
def test_apply_turn_on():
    '''test the behaviour of turn on the lights'''
    size=5
    led=run.LightTester(size)
    led.apply("turn on",0,0,2,2)
    assert np.sum(led.lights==1)==9

def test_apply_turn_off():
    '''test the behaviour of turn off the lights'''
    size=6
    led=run.LightTester(size)
    led.apply("turn on",0,0,2,2)
    led.apply("turn off",0,0,1,1)
    assert np.sum(led.lights==1)==5

def test_apply_switch():
    '''test the behaviour of switch the lights'''
    size=5
    led=run.LightTester(size)
    led.apply("switch",0,0,2,2)
    assert np.sum(led.lights==1)==9

def test_apply_wrong_cmd():
    '''test the behaviour of dealing with other commands'''
    size=5
    led=run.LightTester(size)
    led.apply("abcd",0,0,2,2)
    assert np.sum(led.lights==0)==25

def test_range():
    '''test whether the region inside the range'''
    x1,x2,y1,y2=run.checkRange(-1,-1,5,3,10)
    assert x1==0 and x2==0 and y1==3 and y2==5

    x1,x2,y1,y2=run.checkRange(10,2,10,2,10)
    assert x1==2 and x2==9 and y1==2 and y2==9

    x1,x2,y1,y2=run.checkRange(2,7,2,7,10)
    assert x1==2 and x2==7 and y1==2 and y2==7
    
def test_initialize():
    size=20
    led=run.LightTester(size)
    assert np.sum(led.lights==0)==size*size 
    
def test_file():
    '''test wheather a file or url exists or not'''
    ifile = "./data/test_data.txt"
    N, instructions = run.parseInput(ifile)
    assert N==10
    
    ifile = "./data/test_data1.txt"
    N, instructions = run.parseInput(ifile)
    assert N==0 and instructions==[]
    
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = run.parseInput(ifile)
    assert N==1000 and instructions[0][1]=='turn off' and instructions[2][1]=="turn off"


