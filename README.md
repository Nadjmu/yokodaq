
# YokoDAQ

This code was developed to acquire data from the Yokogawa Darwin Series DAQ Unit DA100. 
It sets up a TCP socket with the Yokogawa DA100 Main Unit, starts the acquisition with a 
bytecode command, and then reads out and decodes the binary streams with a predefined 
frequency. The data is saved to a csv file or can be directly send to an existing InfluxDB
databases. 

It aims to help researches at the Research Institute IBK at ETH Zurich to conduct large 
scale monitoring projects. The configuration of the project can be individually adjusted 
to the needs of the experiment. 
## Prerequisites
The DAQ is written almost enitrely using the python3 standard library (except for a few 
packages used for the IndluxDB database). Install python3 through the package manager 
or by visiting: https://www.python.org/downloads/. 



Please note that while the DAQ should be compatible with all systems, it has only been 
tested on Linux and Windows.


## Manual 
This manual should help you
- configure the machine using the DAQ32 Software-
- explain step by step how to create a project and save the project settings for future reference 
- guide you through the usage of the User Interface as well as all additional features 
- setup a functional working environment in InfluxDB database/Grafana. 
## Getting started
The DAQ can be run from the command line by
```bash
python3 yokodaq.py
```
or by clicking on the application file in case it is installed.


## Feedback

If you have any feedback, please reach out to us at yimili@student.ethz.ch

