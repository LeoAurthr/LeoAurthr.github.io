
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import sys
print(sys.argv[0])
import os
path = os.getcwd()
print(path)

path = "/Users/likaixuan/Documents/IBI1_2020-21/IBI1_2020-21/Practical7"
os.chdir(path)
dirs = os.listdir( path )
for file in dirs:
    print (file)

covid_data = pd.read_csv("full_data-2.csv")

covid_data.head(5)
print(covid_data.head(5))
covid_data.info()
covid_data.describe()
print(covid_data.describe())
covid_data.iloc[0,1]
print(covid_data.iloc[0,1])
covid_data.iloc[2,0:5]
covid_data.iloc[0:2,:]
covid_data.iloc[0:10:2,0:5]
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
covid_data.iloc[0:3,[0,1,3]]
print(covid_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3,my_columns]
print(covid_data.iloc[0:3,my_columns])
covid_data.loc[2:4,"date"]
print(covid_data.loc[2:4,"date"])
covid_data.loc[4,"total_cases"]
print(covid_data.loc[4,"total_cases"])
covid_data.loc[0:81,"total_cases"]
print(covid_data.loc[0:81,"total_cases"])
m = []
for i in range(7996):
    if covid_data.loc[i,"location"] == "Afghanistan":
        m.append(True)
    else:
        m.append(False)
print(covid_data.loc[m,"total_cases"])
covid_data.loc[0:81,"total_cases"]
print(covid_data.loc[0:81,"total_cases"])
covid_data.loc[0:81,"total_cases"]
print(covid_data.loc[0:81,"total_cases"])
m = []
for i in range(7996):
    if covid_data.loc[i,"location"] == "World":
        m.append(True)
    else:
        m.append(False)
world_dates = covid_data.loc[m,"date"]
world_new_cases = covid_data.loc[m,"new_cases"]
import numpy as np
plt.plot(world_dates, world_new_cases, 'b+')
plt.show()
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()