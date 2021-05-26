import sys
import os
from PySide2.QtCore import *
import psutil

class CpuUsage(QThread):
    CpuSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            # p = os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip("\n")
            p = psutil.cpu_percent(4)
            cpu_used = int(float(p))
            self.CpuSignal.emit(int(cpu_used))
            self.sleep(1)

class Cputemperature(QThread):
    CputemSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            f = open("/sys/class/thermal/thermal_zone0/temp",'r')
            temp = int(f.read().strip("\n"))/1000
            # print("Cputemperature",temp)
            self.CputemSignal.emit(int(temp))
            self.sleep(1)