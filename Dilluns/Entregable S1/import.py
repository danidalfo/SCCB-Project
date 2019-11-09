import pandas as pd
import numpy as np
import seaborn as sns

data=pd.DataFrame(mydataset)

mydataset = pd.read_csv('UJIIndoorLoc_B0-ID-01.csv')

mydataset.isnull().sum()

sns.pairplot(mydataset)