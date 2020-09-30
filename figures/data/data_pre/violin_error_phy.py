"""
Violinplot from a wide-form dataset
===================================

_thumb: .6, .45
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import string
import numpy as np 
from pandas import Series,DataFrame

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 18}

def df():
    with open('./model1_error_ma.txt') as f: 
        lines = f.readlines()
    with open('./model2_error_ma.txt') as f1: 
        lines1 = f1.readlines()
    with open('./model1_error_mo.txt') as f2: 
        lines2 = f2.readlines()
    with open('./model2_error_mo.txt') as f3: 
        lines3 = f3.readlines()



    index=[]
    velocity = []
    kind = []
    i = 1

    for line in lines: 
        index.append(int(i))
        i = i + 1

        st = line
        velocity.append(float(st))
        kind.append(r"$L_1$")

    for line in lines1: 
        index.append(int(i))
        i = i + 1

        st = line
        velocity.append(float(st))
        kind.append('C-Net')

    for line in lines2: 
        index.append(int(i))
        i = i + 1

        st = line
        velocity.append(float(st))
        kind.append('T-Net')

    for line in lines3: 

        index.append(int(i))
        i = i + 1
        
        st = line
        velocity.append(float(st))
        kind.append('SF-Net')


    data={'velocity' :velocity, 'kind':kind}
    frame=DataFrame(data,index=index)
    return frame

if __name__ == '__main__':

    dataf = df()
    # print dataf
    ax = sns.violinplot(x="kind", y="velocity", data=dataf, scale='count',
                        palette="muted", scale_hue=False, cut=0)#, order=['csr','csr5','ell','hyb','sell'])
    #ax2 = sns.swarmplot(x="format", y="speed", data=tips, color="w",alpha=.1)

    #plt.plot([-1000,1000], [1,1],c='grey',ls=':',ms=0.1)

    plt.grid(linestyle='-.')

    # plt.text(0.6, 1.5, r"$Mean$", fontdict=font2)
    # plt.text(0.8, 1.5, r"${Error}_s$", fontdict=font2) 
    # plt.text(0.6, 1.2, r"$SF-Net: 0.2356$", fontdict=font2)
    # plt.text(0.6, 0.9, r"$SF-Net$", fontdict=font2) 
    # plt.text(0.9, 0.9, r"$w/ AM: 0.0917$", fontdict=font2)

    # plt.ylim(0,0.7)
    plt.ylabel("Errors %" , size=18)
    plt.xlabel('')

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.subplots_adjust(bottom=0.3,top=0.8,left=0.15)   
    # plt.savefig("error_s_compare_violin.pdf",dpi=400,bbox_inches='tight')
    ax = plt.gca()  
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.show()
