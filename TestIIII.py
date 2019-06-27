import pandas as pd
import numpy as np
#How to convert list to row dataframe with Pandas?

path = r"C:\Users\Matthias\Desktop\ErsteErgebnisse\test.xlsx"
writer = pd.ExcelWriter(path, engine = 'xlsxwriter')

def write(list, i):
    print(list , i)

    df = pd.DataFrame(data = list).T

    df.to_excel(writer, startrow=i, startcol=0, index=False)


A = ['1', 'd', 'p', 'bab', '']
#df = pd.DataFrame(data = A).T
#df.to_excel(writer, startrow=0, startcol=0)

for i in range(1,6):
    write(A,i)


writer.save()
writer.close()