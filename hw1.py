from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "/Users/Fei/Desktop/gighub/data/"
txt_file = "File1_small/File1_small.txt"

df = pd.read_table(main_dir + txt_file,sep=" ")

a=df[60:100]
a

b=df[df.kwh>30]
b