import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
tau_m = 10.0   # мс (постоянная времени)
R_m = 1.0      # МОм (мембранное сопротивление)
V_rest = -70.0 # мВ (потенциал покоя)
V_th = -56.0   # мВ (порог спайка)
V_reset = -75.0# мВ (сброс после спайка)
dt = 0.1       # мс (шаг времени)
T = 100        # мс (время симуляции)
I = 15.0       # нА (постоянный входной ток)

# Инициализация
steps = int(T / dt)
V = V_rest * np.ones(steps)
spike_times = []

# Интегрирование
for t in range(1, steps):
    dV = (-(V[t-1] - V_rest) + R_m * I) * (dt / tau_m)
    V[t] = V[t-1] + dV
    
    # Проверка на спайк
    if V[t] >= V_th:
        V[t] = V_reset
        spike_times.append(t * dt)

# Визуализация
plt.plot(np.arange(steps) * dt, V)
plt.xlabel("Время (мс)")
plt.ylabel("Мембранный потенциал (мВ)")
plt.axhline(y=V_th, color='r', linestyle='--', label="Порог")
plt.title("LIF-модель нейрона")
plt.legend()
plt.show()