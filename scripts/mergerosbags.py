!#/usr/bin/env python

import rosbag

def mergebags():
rbag_dir=("/home/jakob/catkin_ws/src/rpg_davis_simulator/datasets/rosbags")
rbag_left_name=("rollingball_2mps_left-20170629-100232.bag")
rbag_right_name=("rollingball_2mps_right-20170629-100833.bag")

bag1 = rosbag.Bag(rbag_dir + "/" + rbag_left_name,'r')
bag2 = rosbag.Bag(rbag_dir + "/" + rbag_right_name,'r')
bags = [bag1,bag2]
outputfile = rbag_left_name.split("_")[0] + "_merged"+".bag"

with rosbag.Bag(outputfile,"w") as op:
    for b in bags:
        for topic,msg, t in bag1.read_messages() 
            try: 
                op.write(topic,msg,t)




