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

## The workshops's tools

### MG 

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


