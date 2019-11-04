#!/usr/bin/python

"""
Main file for the computational model Herice C. and Sakata S. (2019)

Sleep/wake regulation model and synapses alterations.
Original model from Costa et al. (2016) and Diniz Behn et al. (2012).

Charlotte HERICE AND SHUZO SAKATA - NOVEMBER 2019
"""


import os
import sleepCompModel
import numpy as np

# os.path.join()

print("--")

simDuration = 24
nbSims = 8
toShow = "n"



# default params
g_RRe = 1.6
g_RWe = 1.0
g_WNi = -2.0
g_WRi = -4.0
g_NRi = -1.3
g_NWi = -1.68
	
Ratios = np.array([0, 1/8, 1/4, 1/2, 1, 2, 4, 8])

# core - REM
dirName = "REM"

for simNumber in range(1, nbSims):
	ctr1 = 0
	for i in Ratios:
		ctr1 += 1
		ctr2 = 0
		for j in Ratios:
			ctr2 += 1
			alterationSite = "REM"+"_R"+str(ctr1)+"_W"+str(ctr2)
			print(alterationSite)

			sleepCompModel.RunSim(simDuration, simNumber, alterationSite, dirName, g_RRe*i, g_RWe*j, g_WNi, g_WRi, g_NRi, g_NWi) 

# core - AW
dirName = "AW"

for simNumber in range(1, nbSims):
	ctr1 = 0
	for i in Ratios:
		ctr1 += 1
		ctr2 = 0
		for j in Ratios:
			ctr2 += 1
			alterationSite = "AW"+"_N"+str(ctr1)+"_R"+str(ctr2)
			print(alterationSite)

			sleepCompModel.RunSim(simDuration, simNumber, alterationSite, dirName, g_RRe, g_RWe, g_WNi*i, g_WRi*j, g_NRi, g_NWi) 

# core - NREM
dirName = "NREM"

for simNumber in range(1, nbSims):
	ctr1 = 0
	for i in Ratios:
		ctr1 += 1
		ctr2 = 0
		for j in Ratios:
			ctr2 += 1
			alterationSite = "NREM"+"_R"+str(ctr1)+"_W"+str(ctr2)
			print(alterationSite)

			sleepCompModel.RunSim(simDuration, simNumber, alterationSite, dirName, g_RRe, g_RWe, g_WNi, g_WRi, g_NRi*i, g_NWi*j) 

