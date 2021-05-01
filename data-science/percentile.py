#!/usr/bin/python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Tree Davies
import numpy as np
import sys


def make_dat(ds, name, stepping):
	name = name + ".dat"
	with open(name, "w") as ff:
		for tup in ds:
			p = tup[0]
			metric = tup[1]
			string = str(p) + " " + str(metric) + '\n'
			ff.write(string)


if __name__ == '__main__':
	
	dataset = []

	if sys.argv[1] == '--fio' and sys.argv[2] != '':
		filename = "./" + str(sys.argv[2])
		with open(filename, "r") as fd:
			lines = fd.readlines()
			for ln in lines:
				lst = ln.split(',')
				metric = int(lst[1])
				dataset.append(metric)
	else:  
		filename = "./" + str(sys.argv[1])
		with open(filename, "r") as fd:
			lines = fd.readlines()
			for ln in lines:
				val = ln.lstrip().rstrip()
				dataset.append(int(val))


	P = []

	qth = str(np.percentile(dataset, 1, interpolation='lower'))
	P.append((1,qth))
	print("P"+str(1)+": "+ qth)

	stepping = 5
	for p in range(5, 96, stepping):
		qth = str(np.percentile(dataset, p, interpolation='lower'))
		P.append((p,qth))
		print("P"+str(p)+": "+ qth)
	qth = str(np.percentile(dataset, 99, interpolation='lower'))
	P.append((99,qth))
	print("P"+str(99)+": "+ qth)
	make_dat(P, filename, stepping)

	print("\nMin: " + str(min(dataset)))
	print("Max: " + str(max(dataset)))


