import matplotlib.pyplot as plt
import numpy as np
import sys
import os

resultsFiles = os.listdir("results")
alldata = []
for resultFile in resultsFiles:
    with open("results/" + resultFile) as rawFile:
        data = []
        for line in rawFile:
            if "intervalDooms" in line:
                data.append(int(line.split("= ")[1]))

    alldata.append(data)

plt.boxplot(alldata,whis=10)

#plt.title('Simulation of Tracing Collector')
plt.xlabel('Interval between Garbage Collections')
plt.ylabel('Identified Unused')

axes = plt.axes()
axes.set_xticklabels(['50', '250', '500'])

plt.show()
