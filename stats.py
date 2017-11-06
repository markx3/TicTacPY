import numpy as np
import matplotlib as mpl

mpl.use('agg')

import matplotlib.pyplot as plt

m_file = open("testes_backup.txt", "r")

minimax   = []
alphabeta = []

count = 0
for line in m_file:
    count += 1
    if count <= 9:
        minimax.append(int(line) + 8)
    else:
        alphabeta.append(int(line) + 8)

print(minimax)
print(alphabeta)

print("\n\nMedia minimax:")
print(np.average(minimax))
print("STD Minimax: ")
print(np.std(minimax))

print("\n\nMedia AlphaBeta:")
print(np.average(alphabeta))
print("STD AlphaBeta:")
print(np.std(alphabeta))

m_file.close()

m_file = open("runtime.txt")

minimax_rt = []
alphabeta_rt = []
count = 0
for line in m_file:
    count += 1
    if count <= 9:
        minimax_rt.append(float(line))
    else:
        alphabeta_rt.append(float(line))

print("\n\n Media RT Minimax: ")
print(np.average(minimax_rt))
print("STD RT Minimax: ")
print(np.std(minimax_rt))

print("\n\n Media AlphaBeta: ")
print(np.average(alphabeta_rt))
print("STD RT AlphaBeta: ")
print(np.std(alphabeta_rt))

print("\nGanho de desempenho percentual médio RT ")
print(1 - (np.average(alphabeta_rt)/np.average(minimax_rt)))

print("\n Ganho de desempenho na taxa média de expansão")
print (1 - (np.average(alphabeta)/np.average(minimax)))

data_to_plot = [minimax]

fig = plt.figure(figsize=(9,6))
plt.title('Boxplot: Minimax', fontsize=20)
plt.ylabel('Expansões', fontsize=20)

bp = plt.boxplot(data_to_plot, showfliers=True)

fig.savefig('fig1.png')

fig = plt.figure(figsize=(9,6))
plt.title('Boxplot: Alpha-Beta', fontsize=20)
plt.ylabel('Expansões', fontsize=20)

bp = plt.boxplot([alphabeta], showfliers=True)

fig.savefig('fig2.png')
