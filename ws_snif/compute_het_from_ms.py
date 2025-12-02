# -*- coding: utf-8 -*-
"""
Spyder Editor
@author: csteux
24-11-2025
"""

import argparse
import numpy as np
import re

# command line arguments
parser = argparse.ArgumentParser(description="Computing individual heterozygosity from ms simulated genomic sequences.")
parser.add_argument("--ms_out", "-ms", type=str, required=True, help = "path to the ms output")
args = parser.parse_args()
    
print("Computing individual heterozygosity.")

def compute_hetsites(seq1, seq2):
    if len(seq1) != len(seq2):
        return("error: sequences do not have the same length.")
    nhet = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            nhet += 1
    return nhet
        

het_list = []

with open(args.ms_out, "r") as msout:
    line = msout.readline()
    seqlen = int(line.split(" ")[7])
    nind = int(line.split(" ")[1])
    while line != "":
        if re.search("^[01]+$", line) != None:
            seq1 = line
            line = msout.readline()
            seq2 = line
            het_list += [compute_hetsites(seq1, seq2)/seqlen]
        line = msout.readline()

print(round(np.mean(het_list), ndigits=6), " (", round(np.quantile(het_list, 0.25), ndigits=6), ",", round(np.quantile(het_list, 0.75), ndigits=6), ")")


