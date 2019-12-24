#%%
import numpy as np
from numpy import pi
import pandas as pd
import matplotlib.pyplot as plt

import os
root_path = os.path.dirname(os.path.abspath('__file__'))
parent_path = os.path.abspath(os.path.join(root_path, os.path.pardir))
grandpa_path = os.path.abspath(os.path.join(parent_path, os.path.pardir))
data_path = root_path + '\\Xianyang_ssa\\data\\'
print(10 * '-' + ' Current Path: {}'.format(root_path))
print(10 * '-' + ' Parent Path: {}'.format(parent_path)) 
print(10 * '-' + ' Grandpa Path: {}'.format(grandpa_path)) 
print(10 * '-' + ' Data Path: {}'.format(data_path)) 

import sys
sys.path.append(root_path+'/tools/')
from ssa import SSA
# Loading the monthly runoff of xianyang station
xianyang = pd.read_excel(root_path+'/time_series/XianyangRunoff1951-2018(1953-2018).xlsx')
xianyang = xianyang['MonthlyRunoff']
xianyang.plot()
plt.title("Monthly Runoff of Xianyang station")
plt.xlabel("Time(1953/01-2008/12)")
plt.ylabel(r"Runoff($m^3/s$)")
plt.tight_layout()

start=24
stop=696#576
train = xianyang[start:stop] #(train)from 1953/01 to 1998/12, 552 samples
train = train.reset_index(drop=True)
full = xianyang[start:] #(full)from 1953/01 to 2018/12 792 samples
full = full.reset_index(drop=True)
train.plot()


#%%
# Decompose the monthly runoff of xianyang
window = 12 #45% of 552
xianyang_ssa = SSA(full,window)
F0 = xianyang_ssa.reconstruct(0)
F1 = xianyang_ssa.reconstruct(1)
F2 = xianyang_ssa.reconstruct(2)
F3 = xianyang_ssa.reconstruct(3)
F4 = xianyang_ssa.reconstruct(4)
F5 = xianyang_ssa.reconstruct(5)
F6 = xianyang_ssa.reconstruct(6)
F7 = xianyang_ssa.reconstruct(7)
F8 = xianyang_ssa.reconstruct(8)
F9 = xianyang_ssa.reconstruct(9)
F10 = xianyang_ssa.reconstruct(10)
F11 = xianyang_ssa.reconstruct(11)
orig_TS = xianyang_ssa.orig_TS
df = pd.concat([F0,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,orig_TS],axis=1)
df = pd.DataFrame(df.values,columns=[
    'Trend',#F0
    'Periodic1',#F1
    'Periodic2',#F2
    'Periodic3',#F3
    'Periodic4',#F4
    'Periodic5',#F5
    'Periodic6',#F6
    'Periodic7',#F7
    'Periodic8',#F8
    'Periodic9',#F9
    'Periodic10',#F10
    'Noise',#F11
    'ORIG'#orig_TS
    ])
df.to_csv(data_path+'SSA_FULL.csv',index=None)
df

#%%
xianyang_ssa = SSA(train,window)
F0 = xianyang_ssa.reconstruct(0)
F1 = xianyang_ssa.reconstruct(1)
F2 = xianyang_ssa.reconstruct(2)
F3 = xianyang_ssa.reconstruct(3)
F4 = xianyang_ssa.reconstruct(4)
F5 = xianyang_ssa.reconstruct(5)
F6 = xianyang_ssa.reconstruct(6)
F7 = xianyang_ssa.reconstruct(7)
F8 = xianyang_ssa.reconstruct(8)
F9 = xianyang_ssa.reconstruct(9)
F10 = xianyang_ssa.reconstruct(10)
F11 = xianyang_ssa.reconstruct(11)
orig_TS = xianyang_ssa.orig_TS
df = pd.concat([F0,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,orig_TS],axis=1)
df = pd.DataFrame(df.values,columns=[
    'Trend',#F0
    'Periodic1',#F1
    'Periodic2',#F2
    'Periodic3',#F3
    'Periodic4',#F4
    'Periodic5',#F5
    'Periodic6',#F6
    'Periodic7',#F7
    'Periodic8',#F8
    'Periodic9',#F9
    'Periodic10',#F10
    'Noise',#F11
    'ORIG'#orig_TS
    ])
df.to_csv(data_path+'SSA_TRAINDEV.csv',index=None)

#%%
# if not os.path.exists(data_path+'ssa-test'):
#     os.makedirs(data_path+'ssa-test')
# for i in range(1,241):
#     data = xianyang[start:stop+i]
#     data = data.reset_index(drop=True)
#     xianyang_ssa = SSA(data,window)
#     F0 = xianyang_ssa.reconstruct(0)
#     F1 = xianyang_ssa.reconstruct(1)
#     F2 = xianyang_ssa.reconstruct(2)
#     F3 = xianyang_ssa.reconstruct(3)
#     F4 = xianyang_ssa.reconstruct(4)
#     F5 = xianyang_ssa.reconstruct(5)
#     F6 = xianyang_ssa.reconstruct(6)
#     F7 = xianyang_ssa.reconstruct(7)
#     F8 = xianyang_ssa.reconstruct(8)
#     F9 = xianyang_ssa.reconstruct(9)
#     F10 = xianyang_ssa.reconstruct(10)
#     F11 = xianyang_ssa.reconstruct(11)
#     orig_TS = xianyang_ssa.orig_TS
#     df = pd.concat([F0,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,orig_TS],axis=1)
#     df = pd.DataFrame(df.values,columns=[
#         'Trend',#F0
#         'Periodic1',#F1
#         'Periodic2',#F2
#         'Periodic3',#F3
#         'Periodic4',#F4
#         'Periodic5',#F5
#         'Periodic6',#F6
#         'Periodic7',#F7
#         'Periodic8',#F8
#         'Periodic9',#F9
#         'Periodic10',#F10
#         'Noise',#F11
#         'ORIG'#orig_TS
#         ])
#     df.to_csv(data_path+'ssa-test/ssa_appended_test'+str(552+i)+'.csv',index=None)

#%%