# XfceGpuPanelMonitor
A very simple gpu monitor for Xfce panel, based on basic xfce generic monitor

## Dependencies
* python3 required
* gpustat https://github.com/wookayin/gpustat required to be installed
* numpy, colorsys required to be installed

## Installation
0) Install dependencies

1) Create an xfce panel and add a "Generic Monitor" plugin
![Example 1](/images/GenericMonitor.png)
2) Clone the repository to a desired destination
3) Open the gpustat.sh file and write the correct full path to the python script (param_reader.py)
4) Make an executable the gpustat.sh file (chmod +x)
5) Open the "Generic Monitor" settings and enter the full path of the gpustat.sh file
6) Configure the update interval based on your system speed

![Example 2](/images/GenericMonitorExample.png)

command - path to the gpustat.sh goes here
label - write gpu, untick it if you don't need it

## Result
![Example result](/images/Monitor.png)

(1.5 update interval and Moto Sans with 11 size is used)

## Example of xfce panel
![Example result](/images/Example.png)
