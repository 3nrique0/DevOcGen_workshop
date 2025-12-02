# DevOcGen Workshop

Installation of software necessary for the workshop of DevOcGen project held on 1-4 december 2025.

**Requirements**: A Linux computer or a MacOS computer. The environments contain mostly python and R libraries that could work on windows, however we cannot grant they will.

[Information about the venue](https://biodivoc.edu.umontpellier.fr/recherche/projets-consortium/projet-de-consortium-devocgen/semaine-de-restitution-du-projet-devocgen/)

## Update your installation

Last update: **2nd december 2025 11h33**
If you have already cloned this repository before the date above, pull this repo again.

## Installation Instructions

Each workshop has it's own directory and it's own pixi environment.

1. To install pixi follow the instructions for your OS. [Install Pixi](https://pixi.sh/latest/installation/)
1. Clone this repo
1. Change directory to the repo of this git and to the workshop directory: `cd DevOcGen_workshop/ws_selnetime`
1. Install the workspace: `pixi install`
    - This will create a `.pixi\` where the packages will be installed
1. The workshop **RZooRoh** require some extra steps. Further information in the README.md of each workshop.


## Run Instructions

There are two ways to acces the software in this workspace:

1. **Activate a pixi shell**
    - This allows you to change directories and acces the workshop tools wherever your work directory will be.

2. **Prefix commands** with `pixi run`
    - This allows you to change environment with just changing your working directory.

### 1. Pixi shell

Run `pixi shell`. The prompt will change on your environment it should look like a conda environment.
Type `exit` to close the environment.

Shell example:

```
user@computer:ws_rzooroh$ pixi shell
(devocgen_workshop_installs) user@computer:ws_rzooroh$

(devocgen_workshop_installs) user@computer:ws_rzoorohp$ exit

user@computer:ws_rzooroh$
```

### 2. Preffix commands: Activate environment on request before running a command


Prefix `pixi run` to your usual commands.
It will make the workspace run the software without "permamently activating" the environment.

```
# Shell example
user@computer:ws_rzoorohp$ pixi run bcftools

Program: bcftools (Tools for variant calling and manipulating VCFs and BCFs)
License: GNU GPLv3+, due to use of the GNU Scientific Library
Version: 1.22 (using htslib 1.22.1)


```

---

## Thank you

We would like to thank our kind sponsors:

![BioDivOc](.img/biodivoc.png)

![Region Occitanie](.img/region_resized.png)

![Université de Montpellier](.img/UM_resized.png)
