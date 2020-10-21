################
#
# Deep Flow Prediction - N. Thuerey, K. Weissenov, H. Mehrotra, N. Mainali, L. Prantl, X. Hu (TUM)
#
# Generate training data via OpenFOAM
#
################

import os, math, uuid, sys, random
import numpy as np
from push_back import get_setup, push_output


from pandas import DataFrame
import pandas as pd
import os


if __name__ == '__main__':


    frame1 =  pd.read_csv('result_raw.csv')
    lis_raw = list(frame1['Time']) 
    frame2 =  pd.read_csv('result_gcn.csv')
    lis_gcn = list(frame2['Time']) 

    speedup_lis = []

    for i,j in zip(lis_raw, lis_gcn):
        speedup = i / j

        speedup_lis.append(speedup)

        # print(speedup)

    tot_speedup = sum(speedup_lis) / len(speedup_lis)
    print ('average speedup: {}, max speedup: {}, min speedup: {}'.format(tot_speedup, max(speedup_lis), min(speedup_lis)))

    #draw

    
