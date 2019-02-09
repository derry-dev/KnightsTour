import glob
import matplotlib.pyplot as plt
import pandas as pd

files = [i for i in glob.glob('*.{}'.format("csv"))]
print(files)

files_random = []
files_frodsnraw = []
files_warnsdorf = []

for i in files:
    if "random" in i:
        files_random.append(pd.read_csv(i))
    elif "frodsnraw" in i:
        files_frodsnraw.append(pd.read_csv(i))
    elif "warnsdorf" in i:
        files_warnsdorf.append(pd.read_csv(i))
    
df_random = pd.concat(files_random, axis = 0, ignore_index = True)
df_frodsnraw = pd.concat(files_frodsnraw, axis = 0, ignore_index = True)
df_warnsdorf = pd.concat(files_warnsdorf, axis = 0, ignore_index = True)

df_random["Progress"] = [float(str(i).strip("%"))/100 for i in df_random["Progress"]]
df_frodsnraw["Progress"] = [float(str(i).strip("%"))/100 for i in df_frodsnraw["Progress"]]
df_warnsdorf["Progress"] = [float(str(i).strip("%"))/100 for i in df_warnsdorf["Progress"]]

plt.hist(df_random["Progress"], bins=50, color="g", label="Random")
plt.hist(df_frodsnraw["Progress"], bins=50, color="b", alpha=0.8, label="Frodsnraw")
plt.hist(df_warnsdorf["Progress"], bins=50, color="r", alpha=0.8, label="Warnsdorf")
plt.title("Progress Comparison")
plt.xlabel("Progress")
plt.ylabel("Frequency")
plt.legend()
plt.show()