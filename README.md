
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



## Installation
Since the DAQ is written entirely in python, nothing needs to be compiled to run. Simply
download or clone the entire DAQ directory to a user writeable directory. Example of 
cloning the DAQ into a directory called 'yoko_daq'

```bash
git clone https://gitlab.ethz.ch/yimili/yokogawa-2.git yoko_daq
```

If you are mainly interested in working with the User-Interface you can change to the directory 
with an installer file which lets you download the entire DAQ as well as an executable file
for the application. 
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
## Collaborators
This project was initiated and kept under guidance of Dominik Werne and Martin Viertel at IBK

## To DO
import sys 
sys.platform.starts with win or linux: Different sizes in the labels bug

mV, V, °C different colours


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback, please reach out to us at yimili@student.ethz.ch

