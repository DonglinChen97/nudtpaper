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

def df(name):
    with open('./model1_error'+ name+'.txt') as f: 
        lines = f.readlines()
    with open('./model2_error'+ name+'.txt') as f1: 
        lines1 = f1.readlines()
    with open('./model3_error'+ name+'.txt') as f2: 
        lines2 = f2.readlines()
    with open('./model4_error'+ name+'.txt') as f3: 
        lines3 = f3.readlines()
    with open('./model5_error'+ name+'.txt') as f4: 
        lines4 = f4.readlines()


    index=[]
    velocity = []
    kind = []
    i = 1

    for line in lines: 
        index.append(int(i))
        i = i + 1

        st = line
        velocity.append(float(st))
        kind.append('U-Net')

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
        kind.append('FlowDNN')

    for line in lines4: 
        index.append(int(i))
        i = i + 1

        st = line
        velocity.append(float(st))
        kind.append('FlowDNN AP')



    data={'velocity' :velocity, 'kind':kind}
    frame=DataFrame(data,index=index)
    return frame

if __name__ == '__main__':

    dataf = df("")
    # print dataf
    plt.subplot(221)
    ax = sns.violinplot(x="kind", y="velocity", data=dataf, scale='count', linewidth=3,
                        palette="muted", scale_hue=False, cut=0)#, order=['csr','csr5','ell','hyb','sell'])
    #ax2 = sns.swarmplot(x="format", y="speed", data=tips, color="w",alpha=.1)
    #plt.plot([-1000,1000], [1,1],c='grey',ls=':',ms=0.1)
    plt.grid(linestyle='-.')
    plt.ylim(0,0.7)
    plt.ylabel(r"$\rm{MRE}$",size=18)
    plt.xlabel('')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.subplots_adjust(bottom=0.3,top=0.8,left=0.15)   
    # plt.savefig("error_s_compare_violin.pdf",dpi=400,bbox_inches='tight')
    # ax = plt.gca()  
    # ax.yaxis.get_major_formatter().set_powerlimits((0,1))

    dataf = df("_s")
    # print dataf
    plt.subplot(222)
    ax = sns.violinplot(x="kind", y="velocity", data=dataf, scale='count', linewidth=3,
                        palette="muted", scale_hue=False, cut=0)#, order=['csr','csr5','ell','hyb','sell'])
    #ax2 = sns.swarmplot(x="format", y="speed", data=tips, color="w",alpha=.1)
    #plt.plot([-1000,1000], [1,1],c='grey',ls=':',ms=0.1)
    plt.grid(linestyle='-.')
    plt.ylim(0,1.85)
    plt.ylabel(r"$\rm{MRE_{RoI}}$",size=18)
    plt.xlabel('')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.subplots_adjust(bottom=0.3,top=0.8,left=0.15)   
    # plt.savefig("error_s_compare_violin.pdf",dpi=400,bbox_inches='tight')
    ax = plt.gca()  
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))

    dataf = df("_ma")
    # print dataf
    plt.subplot(223)
    ax = sns.violinplot(x="kind", y="velocity", data=dataf, scale='count',linewidth=3,
                        palette="muted", scale_hue=False, cut=0)#, order=['csr','csr5','ell','hyb','sell'])
    #ax2 = sns.swarmplot(x="format", y="speed", data=tips, color="w",alpha=.1)
    #plt.plot([-1000,1000], [1,1],c='grey',ls=':',ms=0.1)
    plt.grid(linestyle='-.')
    plt.ylim(0,1.6)
    plt.ylabel(r"$\rm{MRE}_{ma}$",size=18)
    plt.xlabel('')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.subplots_adjust(bottom=0.3,top=0.8,left=0.15)   
    # plt.savefig("error_s_compare_violin.pdf",dpi=400,bbox_inches='tight')
    ax = plt.gca()  
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))

    dataf = df("_mo")
    # print dataf
    plt.subplot(224)
    ax = sns.violinplot(x="kind", y="velocity", data=dataf, scale='count', linewidth=3,
                        palette="muted", scale_hue=False, cut=0)#, order=['csr','csr5','ell','hyb','sell'])
    #ax2 = sns.swarmplot(x="format", y="speed", data=tips, color="w",alpha=.1)
    #plt.plot([-1000,1000], [1,1],c='grey',ls=':',ms=0.1)
    plt.grid(linestyle='-.')
    plt.ylim(0,2.3)
    plt.ylabel(r"$\rm{MRE}_{mo}$",size=18)
    plt.xlabel('')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.subplots_adjust(bottom=0.3,top=0.8,left=0.15)   
    # plt.savefig("error_s_compare_violin.pdf",dpi=400,bbox_inches='tight')
    ax = plt.gca()  
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))

    plt.show()
