#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np


array=np.zeros((2, 3, 4), dtype=np.int)

print(array)
print(len(array))
print(len(array[0]))
print(len(array[0][0]))

for row in range(0,10):
	print(row)


