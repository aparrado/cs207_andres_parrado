#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Tests for L2_doc.py
Created on Sat Jul 11 11:58:26 2020

@author: andresparrado
"""

import pytest
import L2_doc
import numpy as np


v = np.array([10,14,16])
w = np.array([0.5,0.5,0.5])

def test_normal_vector():
    assert L2_doc.L2(v,w) == 11.74734012447073

def test_types_mismatch():
    with pytest.raises(TypeError):
        L2_doc.L2(np.array(['a','b']))

def test_size_mismatch():
    with pytest.raises(ValueError):
        L2_doc.L2(np.array([1,2,3]),np.array([4,5]))
