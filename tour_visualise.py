import ast
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import string

files = [i for i in glob.glob('*.{}'.format("csv"))]
print(files)

board_size = 8
board = np.array(([([1,0]*board_size)[:board_size],([0,1]*board_size)[:board_size]]*board_size)[:board_size])
row_labels = range(board_size,0,-1)
col_labels = list(string.ascii_uppercase[:board_size])

for j in range(len(files)):
    
    df = pd.read_csv(files[j])
    
    for i in random.choices(range(len(df)),k=3):
        plt.matshow(board, cmap="Greys")
        plt.xticks(range(board_size), col_labels)
        plt.yticks(range(board_size), row_labels)
        moves = ast.literal_eval(df["Moves"][i])
        y = [i[0] for i in moves]
        x = [j[1] for j in moves]
        plt.plot(x, y, color="g")
        plt.scatter(x, y, s=180, marker="x", color="r")
        plt.title("{} {}".format(" ".join([(files[j].split(".")[0]).split("_")[k] for k in [1,3]]),i+1), y=1.08)
        plt.show()
        
