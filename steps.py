import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

final_moves=[]

step = 0
for i in range(100):
    steps_count=[0]
    for i in range(10):
        step = steps_count[-1]
        dice = np.random.randint(1,7)
        if dice <=2:
            step = max(0, step-1)
        elif dice > 2 and dice<6:
            step = step+1
        else:
            step = step + np.random.randint(1,7)
        steps_count.append(step)
    final_moves.append(steps_count)
print(final_moves)

final_moves = np.transpose(np.array(final_moves))
plt.plot(final_moves)
plt.show()
plt.clf
plt.hist(final_moves[-1,:])
plt.show()
