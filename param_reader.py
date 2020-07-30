import json
import numpy as np
import colorsys
import subprocess

from os import path
from enum import Enum

MAX_GPU_TEMP = 99

def lerp(v0, v1, t):
    return (1 - t)*v0 + t*v1

class GpuStat:

    def __init__(self):
        self.value = 0
        self.color = np.array([0.0,0.0,0.0])
        self.transform = lambda x : x * 0.01

    def str_rgb_hex(self):
        color_rgb = colorsys.hsv_to_rgb(self.color[0], self.color[1], self.color[2])
        return '#%02x%02x%02x' % ( int(color_rgb[0] * 255), int(color_rgb[1] * 255), int(color_rgb[2] * 255))

    def update_color(self):
        self.value = self.transform(self.value)
        self.color = lerp(Colors.GREEN, Colors.RED, self.value)


#colors in hsv
class Colors:
    GREEN =  np.array([0.33, 1.0, 1.0])
    RED = np.array([0.0, 1.0, 1.0])

class EGpuStats(Enum):
    FAN = 0
    TEMP = 1
    UTIL = 2
    MEM = 3
    POWER = 4
    COUNT = 5

def main():
    result = subprocess.run(['gpustat', '--json'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    data = json.loads(output)

    data_names = ('fan.speed', 'temperature.gpu', 'utilization.gpu', 'memory.used', 'power.draw')

    for gpu in data['gpus']:

        stats = [GpuStat() for _ in range(EGpuStats.COUNT.value)]

        max_memory = gpu['memory.total']
        max_power = gpu['enforced.power.limit']

        stats[EGpuStats.TEMP.value].transform = lambda v : v / MAX_GPU_TEMP
        stats[EGpuStats.MEM.value].transform = lambda v : v / max_memory
        stats[EGpuStats.POWER.value].transform = lambda v : v / max_power

        for i in range(EGpuStats.COUNT.value):
            name = data_names[i]
            value = stats[i].value = gpu[name]
            stats[i].update_color()


        print('<txt><span foreground="#c4f9ff"> Temp: <span foreground="{8}">{0:5d}°C</span> Fan: <span foreground="{7}">{1:7d}%</span>\n Util: <span foreground="{9}">{2:8d}%</span>  Mem: <span foreground="{10}">{3:6d}/{4:d}Mb</span>\n Power: <span foreground="{11}">{5:3d}/{6}W</span> </span></txt>'.format(gpu['temperature.gpu'],
                                                                                        gpu['fan.speed'],
                                                                                        gpu['utilization.gpu'],
                                                                                        gpu['memory.used'],
                                                                                        gpu['memory.total'],
                                                                                        gpu['power.draw'],
                                                                                        gpu['enforced.power.limit'],
                                                                                        stats[EGpuStats.FAN.value].str_rgb_hex(),
                                                                                        stats[EGpuStats.TEMP.value].str_rgb_hex(),
                                                                                        stats[EGpuStats.UTIL.value].str_rgb_hex(),
                                                                                        stats[EGpuStats.MEM.value].str_rgb_hex(),
                                                                                        stats[EGpuStats.POWER.value].str_rgb_hex()))



if __name__ == "__main__":
    main()


