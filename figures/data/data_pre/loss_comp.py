import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# mpl.rcParams["font.sans-serif"] = ["SimHei"]
# mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(4)
y = [8.42, 42.23, 37.83, 26.78]
y1 = [7.91, 23.56, 18.28, 22.46]
# y2 = [0.5952, 0.0470, 0.0127]
# y3 = [0.3874, 0.0237, 0.0104]

bar_width = 0.3
tick_label = [r"$\rm{MRE}$", r"$\rm{MRE_{RoI}}$", r"$\rm{MRE}_{ma}$", r"$\rm{MRE}_{mo}$"]
# tick_label = [4,40,400]
plt.grid(linestyle='-.')
plt.bar(x, y, bar_width, align="center", color="tomato", label= r"$L_1$", alpha=0.5)

plt.bar(x+bar_width, y1, bar_width, color="skyblue", align="center", label=r"$L_{physical}$", alpha=0.5)
# plt.bar(x+bar_width*2, y2, bar_width, align="center", color="tomato", label=r"$\rm{Error}_{mo}$ of $L_1$", alpha=0.5)
# plt.bar(x+bar_width*3, y3, bar_width, color="skyblue", align="center", label=r"$\rm{Error}_{mo}$ of $L_{Physical}$", alpha=0.5)

plt.ylabel("Errors %",fontsize=20)

plt.xticks(x+bar_width*1/2, tick_label,fontsize=20)
plt.yticks(fontsize = 20)
plt.legend(loc = 'best',prop={'size':20})
plt.show()

