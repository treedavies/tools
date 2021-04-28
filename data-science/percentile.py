#!/usr/bin/python3
import numpy as np
import sys

dataset = []
filename = "./" + str(sys.argv[1])
with open(filename, "r") as fd:
  lines = fd.readlines()
  for ln in lines:
    val = ln.lstrip().rstrip()
    dataset.append(int(val))

for p in range(1,101):
  qth = str(np.percentile(dataset, p, interpolation='lower'))
  print("P"+str(p)+": "+ qth )

