<<<<<<< HEAD
import numpy
import pandas
import matplotlib
import scipy
import sklearn

print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("Matplotlib:", matplotlib.__version__)
print("SciPy:", scipy.__version__)
print("Scikit-learn:", sklearn.__version__)

print("すべて正常に読み込めました！")
=======
<<<<<<< HEAD
print("hello world")
=======
import numpy as np
import matplotlib.pyplot as plt

# 再現性のための乱数設定
np.random.seed(42)

# 時間
time = np.linspace(0, 10, 1000)

# -------------------------
# 通常時のダミーCSI
# -------------------------
normal = 1.0 + 0.05 * np.random.randn(1000)

# -------------------------
# 転倒時のダミーCSI
# -------------------------
fall = normal.copy()

# 6秒付近で大きな変化を発生させる
fall_event = (time > 5.8) & (time < 6.2)
fall[fall_event] += 1.5 * np.sin(
    np.linspace(0, 10 * np.pi, np.sum(fall_event))
)

# 転倒後に少し揺らぎを残す
after_fall = time >= 6.2
fall[after_fall] += 0.3 * np.random.randn(np.sum(after_fall))

# -------------------------
# グラフ表示
# -------------------------
plt.figure(figsize=(10, 5))

plt.plot(time, normal, label="Normal")
plt.plot(time, fall, label="Fall")

plt.xlabel("Time [s]")
plt.ylabel("CSI Amplitude")
plt.title("Dummy CSI Data")
plt.legend()
plt.grid()

plt.show()
>>>>>>> 51ed46f53b2828a757239f633193cd07b772947b
>>>>>>> ad923c2c383aff14d73472c61da77b2b9f6f1a5d
