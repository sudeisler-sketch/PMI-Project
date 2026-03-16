#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:56:42 2026

@author: muude
"""

import yfinance as yf
# Philip Morris (PM) hisse verisini aylık olarak çek
pm_data = yf.download("PM", start="2008-03-17", end="2026-03-16", interval="1mo")
print(pm_data.head())
print(pm_data.tail())