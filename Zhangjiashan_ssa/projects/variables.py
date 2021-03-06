import pandas as pd
import logging
logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s] %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)

import os
root_path = os.path.dirname(os.path.abspath('__file__'))
import json
with open(root_path+'/config/config.json') as handle:
    dictdump = json.loads(handle.read())
data_part=dictdump['data_part']

pacf_data = pd.read_csv(root_path+'/Zhangjiashan_ssa/data/PACF.csv')
up_bounds=pacf_data['UP']
lo_bounds=pacf_data['LOW']
subsignals_pacf = pacf_data.drop(['ORIG','UP','LOW'],axis=1)
lags_dict={}
for signal in subsignals_pacf.columns.tolist():
    # print(subsignals_pacf[signal])
    lag=0
    for i in range(subsignals_pacf[signal].shape[0]):
        if abs(subsignals_pacf[signal][i])>0.5 and abs(subsignals_pacf[signal][i])>up_bounds[0]:
            lag=i
    lags_dict[signal]=lag  

variables={
    'lags_dict':{
        'Trend':14,
        'Periodic1':4,
        'Periodic2':15,
        'Periodic3':17,
        'Periodic4':15,
        'Periodic5':17,
        'Periodic6':20,
        'Periodic7':19,
        'Periodic8':19,
        'Periodic9':18,
        'Periodic10':18,
        'Noise':18,
    },
    'full_len' :data_part['full_len'],
    'train_len' :data_part['train_len'],
    'dev_len' : data_part['dev_len'],
    'test_len' : data_part['test_len'],
}
logger.debug('variables:{}'.format(variables))

# one_step_lags = [
#     3,#Trend
#     4,#Periodic1
#     3,#Periodic2
#     4,#Periodic3
#     5,#Periodic4
#     4,#Periodic5
#     5,#Periodic6
#     4,#Periodic7
#     5,#Periodic8
#     4,#Periodic9
#     4,#Periodic10
#     5,#Noise
# ]

# multi_step_lags = [
#     3,#Trend
#     4,#Periodic1
#     3,#Periodic2
#     4,#Periodic3
#     5,#Periodic4
#     4,#Periodic5
#     5,#Periodic6
#     4,#Periodic7
#     5,#Periodic8
#     4,#Periodic9
#     4,#Periodic10
#     5,#Noise
# ]
