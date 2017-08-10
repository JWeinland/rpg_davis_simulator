#!/usr/bin/env python


import rosbag

#header
__author__ = "Philip Keller, Jakob Weinland"
__email__ = "philipkellr@gmail.com, jakobweinland@gmail.com"

rbag_dir=("/home/jakob/catkin_ws/src/rpg_davis_simulator/datasets/rosbags")
rbag_left_name=("rollingball_2mps_left-20170629-100232.bag")
rbag_right_name=("rollingball_2mps_right-20170629-100833.bag")

bag1 = rosbag.Bag(rbag_dir + "/" + rbag_left_name,'r')
bag2 = rosbag.Bag(rbag_dir + "/" + rbag_right_name,'r')
bags = [bag1,bag2]
topics =  ["dvs_left","dvs_right"]

outputfile = rbag_left_name.split("_")[0] + "_merged"+".bag"


def mergebags():
    with rosbag.Bag(outputfile,"w") as op:
        for i, b in enumerate(bags):
            for topic,msg,t in b.read_messages(): 
                topic = topic.replace("dvs",topics[i])
                op.write(topic,msg,t)


if (__name__ == '__main__'):
    mergebags()
