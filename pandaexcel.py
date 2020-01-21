import pandas as pd
import tkinter as tk
from tkinter import filedialog
# 關閉tkinter內建根視窗
root = tk.Tk()
root.withdraw()
# 取得路徑
path = filedialog.askopenfilename()

# 這個會直接預設讀取到這個Excel的第一個表單
df=pd.read_excel(path)

print(df)
'''for x in len(df.ix):
    data=df.ix[x].values#0表示第一行 這裡讀取資料並不包含表頭，要注意哦！
    print("讀取指定行的資料：\n{0}".format(data))'''
i=0;
try:
    while df['材料名稱'][i]!="":
        print(df['材料名稱'][i])
        i=i+1
except KeyError:
    print('資料讀取結束')

url='http://www.stockq.org/market/asia.php'
pd.read_html(url)[4]