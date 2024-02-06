#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:15:12 2024

@author: austin
"""

import numpy as np
import matplotlib.pyplot as plt

"""


"""

###load data
SampleECG = np.genfromtxt("SampleECGdata.txt")
max_ecg = np.max(SampleECG)
min_ecg = np.min(SampleECG)
mean_ecg = np.mean(SampleECG)

###corrected data

DCcorrected_ecg = np.subtract(SampleECG, mean_ecg)
corrected_mean = np.mean(DCcorrected_ecg)


###print
#print(f'MIN = {min_ecg:.3f}, MAX: {max_ecg:.1f} and the MEAN is {mean_ecg:.5e}')

#print(f' {corrected_mean:.5e}')

###plot both data sets
plt.title("DC corrected signal for SampleECG Data")

plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(SampleECG, label = "Without DC offset")
plt.plot(DCcorrected_ecg, label = "With DC offset")

plt.legend()
plt.show()

###get input for subsample
#subsample_rate = int((input)("Please enter the desired subsample rate: "))

#subsampled_data = SampleECG[0::subsample_rate]
#print(np.size(SampleECG))
#print(np.size(subsampled_data))

##should cover 1 second in total
step = np.linspace(0,1,num=256)


subsampled_data2 = SampleECG[0::2]
step2 = step[0::2]
print(len(step))
print(len(step2))

subsampled_data10 = SampleECG[0::10]
step10 = step[0::10]

#print('step: ', step)
###plot of the original ECG waveform, a subsampled version for n=2, and n=10. 
plt.title("Sample ECG data over 1 second")

plt.xlabel("Sec")
plt.ylabel("Voltage")

plt.plot(step,SampleECG)
#plt.plot(step2,subsampled_data2, label = "Subsampled at n = 2")

#plt.plot(step10,subsampled_data10, label = "Subsampled at n = 10")

plt.legend()
plt.show()


