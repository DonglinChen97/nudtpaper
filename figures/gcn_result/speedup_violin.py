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

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


if __name__ == '__main__':


    speedup_lis = []
    kind = []
    index = []

    frame1 =  pd.read_csv('./chapter4/result_raw.csv')
    lis_raw = list(frame1['Time']) 
    frame2 =  pd.read_csv('./chapter4/result_gcn.csv')
    lis_gcn = list(frame2['Time']) 

    k = 0 
    for i,j in zip(lis_raw, lis_gcn):
        speedup = i / j
        k = k + 1
        index.append(k)
        speedup_lis.append(speedup)
        kind.append('内插集')

    frame1 =  pd.read_csv('./chapter4_extend/result_raw.csv')
    lis_raw = list(frame1['Time']) 
    frame2 =  pd.read_csv('./chapter4_extend/result_gcn.csv')
    lis_gcn = list(frame2['Time']) 


    for i,j in zip(lis_raw, lis_gcn):
        speedup = i / j
        k = k + 1
        index.append(k)
        speedup_lis.append(speedup)
        kind.append('外推集')

    data={'Speedup' :speedup_lis, 'kind':kind}
    frame=DataFrame(data,index=index)
    print (frame)

    ax = sns.violinplot(x="kind", y="Speedup", data=frame, scale='count',linewidth=4,
                        palette="muted", scale_hue=False, cut=0)#, order=['csr','csr5','ell','hyb','sell'])
    #ax2 = sns.swarmplot(x="format", y="speed", data=tips, color="w",alpha=.1)

    #plt.plot([-1000,1000], [1,1],c='grey',ls=':',ms=0.1)

    plt.grid(linestyle='-.')

    # plt.text(0.6, 1.5, r"$Mean$", fontdict=font2)
    # plt.text(0.8, 1.5, r"${Error}_s$", fontdict=font2) 
    # plt.text(0.6, 1.2, r"$SF-Net: 0.2356$", fontdict=font2)
    # plt.text(0.6, 0.9, r"$SF-Net$", fontdict=font2) 
    # plt.text(0.9, 0.9, r"$w/ AM: 0.0917$", fontdict=font2)

    plt.ylim(1,2.8)
    plt.ylabel(r"speedup",size=20)
    plt.xlabel('')

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.subplots_adjust(bottom=0.3,top=0.8,left=0.15)   
    # plt.savefig("error_s_compare_violin.pdf",dpi=400,bbox_inches='tight')
    # ax = plt.gca()  
    # ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    # plt.text(0,6,'1e-1',fontsize=20)

    plt.show()
