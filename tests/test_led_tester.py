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


