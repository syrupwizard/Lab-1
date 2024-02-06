#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:22:53 2024

@author: austin
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path

file_name = str(input("Enter name of file you'd like to open: "))

if os.path.exists(file_name):
    print("Loading file data...")
    ###load data
    SampleECG = np.genfromtxt(file_name)
    max_ecg = np.max(SampleECG)
    min_ecg = np.min(SampleECG)
    mean_ecg = np.mean(SampleECG)

    ###corrected data
    DCcorrected_ecg = np.subtract(SampleECG, mean_ecg)
    corrected_mean = np.mean(DCcorrected_ecg)

    ###plot both data sets
    plt.title("DC corrected signal for SampleECG Data")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(SampleECG, label = "Without DC offset")
    plt.plot(DCcorrected_ecg, label = "With DC offset")

    plt.legend()
    plt.show()

else:
    print(file_name, "could not be located...")
    print("Please ensure this file exists in your current working directory.")
    


