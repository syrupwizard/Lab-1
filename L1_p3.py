#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 12:16:56 2024

@author: austin huerta
"""
import numpy as np
import matplotlib.pyplot as plt


###load data
bad_ecg = np.genfromtxt("badECG.txt")
mean_ecg = np.mean(bad_ecg)


###Correct DC offset
corrected_ecg = np.subtract(bad_ecg, mean_ecg)
corrected_mean = np.mean(corrected_ecg)

###Flip data
corrected_ecg *= -1

###Increase amplitude
max_ecg = np.max(corrected_ecg)
corrected_ecg *= (10/max_ecg)

###step over 3 seconds
step = np.linspace(0,3,len(corrected_ecg))

###Plot original and corrected
plt.title("Bad versus Corrected ECG data over 3 second")
plt.xlabel("Seconds")
plt.ylabel("Voltage")
plt.plot(step,bad_ecg, color ="r", label = "Bad ECG")
plt.plot(step,corrected_ecg, color = "g", label = "Corrected ECG")

plt.legend(loc='lower center')
plt.show()