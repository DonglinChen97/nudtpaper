import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# mpl.rcParams["font.sans-serif"] = ["SimHei"]
# mpl.rcParams["axes.unicode_minus"] = False

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(2)
y = [0.011, 0.011]
y1 = [5.277, 5.901]
y2 = [8.612, 8.590]
# y2 = [0.5952, 0.0470, 0.0127]
# y3 = [0.3874, 0.0237, 0.0104]

bar_width = 0.3
tick_label = ["内插数据集", "外推数据集"]
# tick_label = [4,40,400]
plt.grid(linestyle='-.')
plt.bar(x, y, bar_width, align="center", color="gray", label= r"GCN推理", alpha=0.5)
plt.bar(x, y1, bar_width, bottom=y, align="center", color="tomato", label= r"求解器优化", alpha=0.5)


plt.bar(x+bar_width, y2, bar_width, color="skyblue", align="center", label=r"传统CFD求解器", alpha=0.5)
# plt.bar(x+bar_width*2, y2, bar_width, align="center", color="tomato", label=r"$\rm{Error}_{mo}$ of $L_1$", alpha=0.5)
# plt.bar(x+bar_width*3, y3, bar_width, color="skyblue", align="center", label=r"$\rm{Error}_{mo}$ of $L_{Physical}$", alpha=0.5)

plt.ylabel("Time s",fontsize=20)

plt.xticks(x+bar_width*1/2, tick_label,fontsize=20)
plt.yticks(fontsize = 20)
plt.ylim([0,12])
plt.legend(loc = 'best',ncol = 3 ,prop={'size':20})
plt.show()

