import numpy as np 
from matplotlib import pyplot as plt 
import pandas as pd 

csv_name = input("csv file name...")

data = pd.read_csv(csv_name)  #csv読み込み
data_col = data.columns  #columnの名前を抽出した配列生成
plt.plot(data[data_col[0]],data[data_col[1]])
plt.show()

