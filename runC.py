import os
import numpy as np
from matplotlib import pyplot as plt

import xml.etree.ElementTree as ET

def initialize(grids=5,lanes=1,length=200):
    os.system("netgenerate --grid --grid.number=5 -L="+str(lanes)+" --grid.length="+str(length)+" --default-junction-type=traffic_light --output-file=grid.net.xml")

def single():    
    os.system("sumo -c grid.sumocfg --device.fcd.period 10000 --no-warnings")

def learn():
    
    #modify_xml("grid.net.xml")

    for i in range(0,10):
        single()

if __name__ == '__main__':
    path = "\"C:/Program Files (x86)/Eclipse/Sumo/tools/\""
    initialize()    

    learn()