import pandas as pd

import matplotlib.pyplot as plt
import os

current_file = __file__
current_dir = os.path.dirname(current_file)

file_dir = os.path.join(current_dir + '/datadump_s5-000.csv')

dataset = pd.read_csv(file_dir)
df = pd.DataFrame(dataset)

df_Platform = df.groupby(['platform'])
df_PC = df_Platform[df_Platform['platform'] == 'PC']
