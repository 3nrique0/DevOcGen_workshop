# DevOcGen_workshop

Installation of software necessary for the workshop of DevOcGen project held on december 2025.

**This is under development and under tests**

## Environment or Container

Tools: Pixi or Apptainer

### Environment and package managers - Pixi
They are easier to install and smaller to convey.
If all the software is available to be installed, this will be the prioritary choice.

So far the test is ongoing with **PIXI**.

### Containers - Apptainer
Containers are more replicable since they replicate the OS environment.
There are 2 ways to transmit the container:

* From a `.def` file: Creating a .sif from a .def can be a bit slow since it means to insall the OS and then install (maybe compile) each piece of software.

* From a `.sif` file: This file will contin all the software, environment and os to run the software.

---

## Instructions -- Install

Each workshop will have it's own directory and it's own workspace/environment

1. [Install Pixi](https://pixi.sh/latest/installation/)
1. Clone this repo
1. Change directory to the repo of this git and to the workshop directory: `cd DevOcGen_workshop/ws_rzooroh`
1. Install the workspace: `pixi install`
    - This will create a `.pixi\` where the packages will be installed
1. Run the task to install RZooRoh since it is neither available on conda-forge nor bioconda: `pixi run install_rzooroh`
1. Test if the package is loaded correctly from R with another task: 'pixi run test rlibs'

## Instructions -- Run

There are two ways to acces the software in this workspace:

### 1- Pixi shell

Run `pixi shell`. The prompt will change on your environment it should look like a conda environment:

```
# Shell example
user@computer:ws_rzooroh$ pixi shell
(devocgen_workshop_installs) user@computer:ws_rzooroh$

(devocgen_workshop_installs) user@computer:ws_rzoorohp$ exit
user@computer:ws_rzooroh$
```

### 2- Activate environment on request before running a command


Prefix `pixi run` to your usual commands.
It will make the workspace run the software without "activating" the environment.

```
# Shell example
user@computer:DevOcGen_workshop$ pixi run bcftools

Program: bcftools (Tools for variant calling and manipulating VCFs and BCFs)
License: GNU GPLv3+, due to use of the GNU Scientific Library
Version: 1.22 (using htslib 1.22.1)


```

---

## The workshops's tools

### RZooRoH 

Tools:
* R 
* RZooRoH
* Plink
* Samtools
* BCFtools

- [x] Installation process
- [x] Replication on the same computer
- [ ] Replication on a different computer
- [ ] Replilcation on a different OS 

### Selnetime

* snakemake-minimal
* matplotlib
* graphviz
* scipy
* sympy
* numba
* pandas
* tbb
* r-base
* r-essentials
* r-tidyverse
* r-scales
* r-patchwork
* selnetime

- [x] Installation process
    - [x] Use Pypi dependencies from pixi
* There is a warning from `graphviz`.
    - [ ] Is it important ?
- [ ] Replication on the same computer
- [ ] Replication on a different computer
- [ ] Replilcation on a different OS 