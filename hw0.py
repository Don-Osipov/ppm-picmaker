import numpy as np
import random

f = open("picmaker.ppm", "w")
header = "P3\n512 512\n255\n"
f.write(header)


bodyArr = np.empty((512, 512, 3)).astype(int)

for i, row in enumerate(bodyArr):
    for j, col in enumerate(row):
        for k, rgb in enumerate(col):
            if k == 0:
                rgb = round((pow(i, 1.5) + pow(j, 1.5)), 5) % 130
            else:
                rgb = round((pow(i, 1.5) + pow(j, 1.5)), 5) % 255
            # 1.5 is like a wave ripple
            f.write(f"{rgb} ")
    f.write("\n")

f.close()

