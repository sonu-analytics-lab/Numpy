import numpy as np
tempreatures = [32.5, 31.8, 33.0, 35.2, 36.6]

total = 0

for temp in tempreatures:
    total += temp

avg = total/(len(tempreatures))
print(avg)

# -----------------------------------------------------

tempreatures = np.array([32.5, 31.8, 33.0, 35.2, 36.6])
average = np.mean(tempreatures)
print(average)
