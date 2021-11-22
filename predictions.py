import numpy as np
import matplotlib.pyplot as plt

import pandas   as pd


a = np.array([1,2,3,4,5])
b = np.array([9,18,27,36,45])
x = pd.DataFrame({"student":["arun","mahesh","ajith","suvin","dhanush"],"year":[1,2,3,4,5],"yearwisemark":[9,18,27,36,45]})
print(x)

plt.plot(a,b,Linestyle = "dotted")
plt.title("mark representation")
plt.xlabel("year")
plt.ylabel(" year  wise mark")
plt.show()



