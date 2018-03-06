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
    
'''def test_command_line_interface():
    ifile = "./data/test_data.txt"
    N, instructions = led_tester.parseInput(ifile)
    assert N==10'''

