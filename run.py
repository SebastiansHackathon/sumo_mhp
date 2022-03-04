import os
import numpy as np
from matplotlib import pyplot as plt

import xml.etree.ElementTree as ET

def initialize(grids=5,lanes=1,length=200):
    os.system("netgenerate --grid --grid.number=5 -L="+str(lanes)+" --grid.length="+str(length)+" --default-junction-type=traffic_light --output-file=grid.net.xml")

def single(path,vehicles):
    #os.system("python 'C:\\Program Files (x86)\\Eclipse\\Sumo\\tools\\randomTrips.py' -n grid.net.xml -o flows.xml --begin 0 --end 1 --period 1 --flows "+str(vehicles))
    os.system("jtrrouter --flow-files=flows.xml --net-file=grid.net.xml --output-file=grid.rou.xml --begin 0 --end 10000 --accept-all-destinations")
    #os.system(path + "generateContinuousRerouters.py -n grid.net.xml --end 2000 -o rerouter.add.xml")
    tree = ET.parse("grid.sumocfg")
    root = tree.getroot()
    for child in root:        
        if (child.tag == 'output'):
            for child2 in child:
                child2.attrib['value'] = './out/grid.output'+str(vehicles)+'.xml'
    with open('grid.sumocfg', 'wb') as f:
        tree.write(f)
    os.system("sumo -c grid.sumocfg --device.fcd.period 50 --no-warnings")

if __name__ == '__main__':
    path = "\"C:/Program Files (x86)/Eclipse/Sumo/tools/\""
    initialize()


    for i in range(0,10):
        single(path,i)