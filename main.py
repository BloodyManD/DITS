import pandas as pd
import matplotlib.pyplot as plt
nn_result = pd.read_csv('NN result.csv', sep=';')

print(nn_result)

fig, ax1 = plt.subplots()
ax1.plot(nn_result['epoch'], nn_result['correct'])
ax1.set_ylabel('Процент совпадений')
ax1.set_xlabel('Эпоха')
ax1.grid()
plt.show()
fig, ax2 = plt.subplots()
ax2.plot(nn_result['epoch'], nn_result['error'])
ax2.set_ylabel('Ошибка')
ax2.set_xlabel('Эпоха')
ax2.grid()

plt.show()
