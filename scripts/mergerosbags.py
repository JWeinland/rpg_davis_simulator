#!/usr/bin/env python


import rosbag

#header
__author__ = "Philip Keller, Jakob Weinland"
__email__ = "philipkellr@gmail.com, jakobweinland@gmail.com"

rbag_dir=("/media/jakob/Toshiba 8 G/datasets/rosbags")
rbag_left_name=("rollingball_2mps_left-20170629-174716.bag")
rbag_right_name=("rollingball_2mps_right-20170629-175637.bag")

bag1 = rosbag.Bag(rbag_dir + "/" + rbag_left_name,'r')
bag2 = rosbag.Bag(rbag_dir + "/" + rbag_right_name,'r')
bags = [bag1,bag2]
outputfile = rbag_left_name.split("_")[0] + "_merged"+".bag"


def mergebags():
    with rosbag.Bag(outputfile,"w") as op:
        for b in bags:
            for topic,msg,t in b.read_messages(): 
                op.write(topic,msg,t)


if (__name__ == '__main__'):
    mergebags()
