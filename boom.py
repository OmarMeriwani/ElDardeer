import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
locations = [ 0.225, 0.075, -0.075,0.225]

#* time_stamp location state time_stamp
df =pd.read_csv('Data 28_7/Linda 01/boardStates/data.log',header=None, delimiter=' ').values.tolist()
points = []
for i in df:
    if i[3] == 1:
        points.append([i[1],locations[int(i[2])],[],0,0])

df2 =pd.read_csv('Data 28_7/Linda 01/robotCartHotPointDumper/data.log',header=None, delimiter=' ').values.tolist()

cart = []
df3 = pd.DataFrame(columns=['time','mean','error','original'])
seq = 0
for i in range(0, len(points) - 1):
    cartM = [j[8] for j in df2 if j[1] >= points[i][0] and j[1] < points[i+ 1][0]]
    if i == 31:
        cartM = [j[8] for j in df2 if j[1] >= points[31][0]]
    error = [abs(points[i][1]) - abs(m) for m in cartM]
    error = sum(error) / len(error)
    cartmAVG = sum(cartM) / len(cartM)
    print([points[i][0],cartmAVG, error, points[i][1]])
    df3.loc[seq] = [points[i][0],cartmAVG, error, points[i][1]]
    seq += 1
ax = sns.lineplot(x="time", y="mean",markers=True, dashes=False,   data=df3)
plt.show()



#* time_stamp u v max mean std x y z  1,8