# XfceGpuPanelMonitor
A very simple gpu monitor for Xfce panel, based on basic xfce generic monitor

## Dependencies
* python3 required
* gpustat https://github.com/wookayin/gpustat required to be installed
* numpy, colorsys required to be installed

## Installation
1) Create an xfce panel and add a "Generic Monitor" plugin
![Example 1](/images/GenericMonitor.png)
2) Clone the repository to a desired destination
3) Make an executable the gpustat.sh file (chmod +x)
4) Open the "Generic Monitor" settings and enter the full path to the gpustat.sh file
5) Configure the update interval based on your system speed

![Example 2](/images/GenericMonitorExample.png)

## Result
![Example result](/images/Monitor.png)

## Example of xfce panel
![Example result](/images/Example.png)
