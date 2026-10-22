import math
import matplotlib.pyplot as plt

def concentration(c0, k, t):
    return c0 * math.exp(-k * t)

c0 = 20    # 初始浓度 mg/L
k = 0.2    # 清除速率常数 1/h

time = []
conc = []

plt.xlabel("Time (h)")
plt.ylabel("Concentration (mg/L)")
plt.xlim(0, 24)
plt.ylim(0, 22)
plt.grid(axis="y")

for t in range(0, 25):
    time.append(t)
    conc.append(concentration(c0, k, t))
    plt.plot(time, conc, color="blue")
    plt.pause(0.2)

plt.show()