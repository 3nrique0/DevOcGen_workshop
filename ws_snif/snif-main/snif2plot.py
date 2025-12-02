#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 10:26:26 2025

@author: csteux
"""
import matplotlib.pyplot as plt
import matplotlib
import argparse
import numpy as np
import json
import matplotlib.gridspec as gridspec

# command line arguments
parser = argparse.ArgumentParser(description="Plot SNIF output.")
parser.add_argument("--basename", "-bn", type=str, required=True, help = "basename of the snif output to plot")
parser.add_argument("--generation_time", "-g", type=float, required=True, help = "generation time")
parser.add_argument("--target", "-t", type=str, nargs='?', help = "path to the json scenario to plot")

args = parser.parse_args()
    
print("Plotting ", args.basename)


# read .json and get necessary parameters
json_file = open(args.basename+"_settings.json")
settings = json.load(json_file)
json_file.close()
c = settings["inference_parameters"]["number_of_components"]
xmin, xmax = settings["inference_parameters"]["data_cutoff_bounds"]
nmin, nmax = settings["inference_parameters"]["bounds_islands"]
Nmin, Nmax = settings["inference_parameters"]["bounds_effective_size"]
if len(settings["inference_parameters"]["bounds_migrations_rates"]) == 2:
    Mmin, Mmax = settings["inference_parameters"]["bounds_migrations_rates"]
else:
    Mmax = max([elem[1] for elem in settings["inference_parameters"]["bounds_migrations_rates"]]) 
    Mmin = min([elem[0] for elem in settings["inference_parameters"]["bounds_migrations_rates"]]) 
datamin, datamax = settings["inference_parameters"]["distance_computation_interval"]


# read curves.csv
f=open(args.basename+"_curves.csv", "r")
curves = f.readlines()
f.close()
times = [float(i)*args.generation_time for i in curves[0].split(",")[2:]]
source = [float(i) for i in curves[1].split(",")[2:]]
inf_iicr = []
for line in curves:
    if "inferred-iicr" in line:
        inf_iicr += [[float(i) for i in line.split(",")[2:]]]


# get the inferred scenarios
f=open(args.basename+".csv", "r")
param = f.readlines()
f.close()    
n_list = []
N_list = []
T_list = []
M_list = []
for line in param[2:]:
    param_line = line.split(",")
    n_list.append(int(param_line[7]))
    N_list.append(float(param_line[7+3*c+1]))
    T_list.append([float(element) for element in param_line[7+1:7+c+1]])
    M_list.append([float(element) for element in param_line[7+c+1:7+2*c+1]])

# get the scenario of the json file to plot
if args.target != None:
    target_file = open(args.target)
    target_param = json.load(target_file)
    target_file.close()
    M_target = target_param["PSNIC"]["M"]
    T_target = target_param["PSNIC"]["t"]
    N_target = target_param["PSNIC"]["Nref"]
    n_target = target_param["PSNIC"]["n"]
    print(T_target, N_target, n_target, M_target)



# create IICR figures
fig, ax = plt.subplots()
fig.tight_layout(pad=0.2)

ax.plot(times, source, label = "Source IICR", color = "dodgerblue", drawstyle='steps-post')
for rep in range(len(inf_iicr)):
    if rep == 1:
        lab = 'Inferred IICR'
    else:
        lab = ""
    ax.plot(times, inf_iicr[rep], label = lab, color = "red", drawstyle='steps-post', alpha = 0.8)
    for tp in T_list[rep]:
        ax.vlines(x = tp*args.generation_time, ymin = -1e7, ymax = 1e7, alpha = 0.2, color = "red")


ax.set_xscale('log')
ax.set_xlim((xmin*args.generation_time, xmax*args.generation_time))
ax.set_ylim((0, np.max([np.max(i) for i in inf_iicr+source])*1.2))
ax.legend(loc="upper left")
ax.set_ylabel("IICR")
ax.set_xlabel("Time (in years)")

fig.set_figheight(5)
fig.set_figwidth(9)
fig.savefig(args.basename+"_IICR.pdf", bbox_inches='tight')
plt.close()


# create figures with inferred parameters
fig2 = plt.figure(constrained_layout=True)
gs = fig2.add_gridspec(4, 10)
ax1 = fig2.add_subplot(gs[:, 0:9])
ax2 = fig2.add_subplot(gs[0:2, 9])
ax3 = fig2.add_subplot(gs[2:4, 9])

#CG
if args.target != None:
    ax1.plot([i*args.generation_time for i in T_target]+[datamax*args.generation_time], M_target+[M_target[-1]], drawstyle='steps-post', label = "target scenario", color = "black")
for rep in range(len(T_list)):
    miginf = M_list[rep] + [M_list[rep][-1]]
    timesinf = [element*args.generation_time for element in T_list[rep]]
    timesinf[0] = datamin*args.generation_time
    ax1.plot(timesinf + [datamax*args.generation_time], miginf, drawstyle='steps-post', label = "repetition " + str(rep+1), alpha = 0.7)

    
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlim((xmin*args.generation_time, xmax*args.generation_time))
ax1.set_ylim((Mmin, Mmax))
ax1.set_xlabel("Time (in years)")
ax1.set_ylabel("Migration rate")
ax1.legend(loc="upper right")

#N
for r in range(len(N_list)):
    ax2.scatter([1], N_list[r], marker = "x", alpha = 0.7)
if args.target != None:
    ax2.scatter([1], N_target, marker = "x", color = "black")
ax2.set_ylabel("Diploid deme size")
ax2.set_ylim((Nmin, Nmax))
ax2.xaxis.set_visible(False)

#n
for r in range(len(n_list)):
    ax3.scatter([1], n_list[r], marker = "x", alpha = 0.7)
if args.target != None:
    ax3.scatter([1], n_target, marker = "x", color = "black")
ax3.set_ylabel("Number of demes")
ax3.set_ylim((nmin, nmax))
ax3.xaxis.set_visible(False)

plt.close()
fig2.set_figheight(5)
fig2.set_figwidth(9)
fig2.savefig(args.basename+"_CG.pdf", bbox_inches='tight')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
