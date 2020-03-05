#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    raise Exception('needs a filename')

kegg_name = 'NAME_NOT_FOUND'

num_atoms = 0
atom_list = []

filename = sys.argv[1]
with open(filename, 'r') as file:
    # get KEGG name
    tokens = file.readline().split()
    kegg_name = tokens[1]

    # get number of atoms
    tokens = file.readline().split()
    num_atoms = int(tokens[1])

    # read atoms into array
    for i in range(num_atoms):
        tokens = file.readline().split()
        atom = {tokens[1], (tokens[3], tokens[4])}
        atom_list.append(atom)

for atom in atom_list:
    print(atom)