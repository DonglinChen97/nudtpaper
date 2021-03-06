import string
import numpy as np 
from pandas import Series,DataFrame
import pandas as pd
import matplotlib.pyplot as plt

import re
import math
 
 
def ConvertELogStrToValue(eLogStr):
    """
    convert string of natural logarithm base of E to value
    return (convertOK, convertedValue)
    eg:
    input:  -1.1694737e-03
    output: -0.001169
    input:  8.9455025e-04
    output: 0.000895
    """
 
    (convertOK, convertedValue) = (False, 0.0)
    foundEPower = re.search("(?P<coefficientPart>-?\d+\.\d+)e(?P<ePowerPart>-\d+)", eLogStr, re.I)
    #print "foundEPower=",foundEPower
    if(foundEPower):
        coefficientPart = foundEPower.group("coefficientPart")
        ePowerPart = foundEPower.group("ePowerPart")
        #print "coefficientPart=%s,ePower=%s"%(coefficientPart, ePower)
        coefficientValue = float(coefficientPart)
        ePowerValue = float(ePowerPart)
        #print "coefficientValue=%f,ePowerValue=%f"%(coefficientValue, ePowerValue)
        #math.e= 2.71828182846
        # wholeOrigValue = coefficientValue * math.pow(math.e, ePowerValue)
        wholeOrigValue = coefficientValue * math.pow(10, ePowerValue)
 
        #print "wholeOrigValue=",wholeOrigValue;
 
        (convertOK, convertedValue) = (True, wholeOrigValue)
    else:
        (convertOK, convertedValue) = (False, float(eLogStr))

    return (convertOK, convertedValue)


def df(file):
    with open(file) as f: 
        lines = f.readlines()

    index=[]
    loss=[]

    for line in lines:
        if 'Loss' in line:
            index.append(int(pre_line))
            
            st=line.split(':')[1]
            st = st.split('%')[0]
            loss.append(float(st)/100)

        pre_line = line
    return     index,loss

    
if __name__ == '__main__':
    
    font2 = {'family' : 'Times New Roman',
    'weight' : 'normal',
    'size'   : 30}

    index,loss = df("result_pruning.dat")

    plt.grid(linestyle='-.')
    
    plt.plot(index, loss, linewidth=1.0,label='Pruning model',
             color='orangered', alpha=0.8)
    plt.scatter(index, loss, color='#4169E2', edgecolor='none', s=7)

    plt.plot([0,700],[0.0513,0.0513],c='burlywood',linewidth=2.5,label='FlowDNN w/ AM')


    
    plt.legend(loc="upper left")
    #plt.ylabel('Validation Loss',size=18)
    plt.ylabel(r'$\rm{MRE}$',size=20)
    plt.xlabel('Number of pruned filters',size=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlim([0,700])
    #plt.ylim([0,0.01])

    ax = plt.gca()  
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    
    plt.show()
    #plt.savefig('demo2.pdf') 
    """
    plt.close()

    plt.subplots_adjust(bottom=0,top=0.6)
    
    sum_row=f_frame.iloc[:,0].size+1
    plt.scatter(np.arange(1,sum_row), f_frame.csr,c='r',marker='^',label='csr',s=20)
    plt.scatter(np.arange(1,sum_row), f_frame.csr5,c='b',marker='o',label='csr5',s=20)
    plt.scatter(np.arange(1,sum_row), f_frame.ell,c='y',marker='x',label='ell',s=20)
    plt.scatter(np.arange(1,sum_row), f_frame.hyb,c='c',marker='s',label='hyb',s=20)
    plt.scatter(np.arange(1,sum_row), f_frame.sell,c='w',marker='v',label='sell',s=20)

    #plt.title('ft2000p_thread64(mtx orderd by nnz)')
    plt.ylabel('GFlops',size=20)
    #plt.xlabel('mtx_num')
    plt.legend(loc='upper left',ncol=1)
    leg = plt.gca().get_legend()
    ltext  = leg.get_texts()
    plt.setp(ltext, fontsize=15)
    plt.xlim([0,1000])
    plt.ylim([0,60])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig('ft_scatter.pdf',dpi=400,bbox_inches='tight')
    """
    


    
