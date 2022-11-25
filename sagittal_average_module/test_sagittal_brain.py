import subprocess
import numpy as np
from sagittal_brain import *


data_input = np.zeros((20, 20))
for i in range(1, 21):
    data_input[-i, :] = i

expected = np.array(
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
)
np.savetxt("brain_sample.csv", data_input, fmt="%d", delimiter=",")

subprocess.run(["python", "sagittal_brain.py"], shell=True)
output = np.loadtxt("brain_average.csv", dtype=int, delimiter=",")

np.testing.assert_array_equal(expected, output)
