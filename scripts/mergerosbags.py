#!/usr/bin/env python

#header
__author__ = "Philip Keller, Jakob Weinland"
__email__ = "philipkellr@gmail.com, jakobweinland@gmail.com"
import rosbag


rbag_dir=("")
rbag_left_name=("")
rbag_right_name=("")

bag1 = rosbag.Bag(rbag_dir + "/" + rbag_left_name,'r')
bag2 = rosbag.Bag(rbag_dir + "/" + rbag_right_name,'r')
bags = [bag1,bag2]
outputfile = rbag_left_name.split("_")[0] + "_merged"+".bag"


def mergebags():
	with rosbag.Bag(outputfile,"w") as op:
    	for b in bags:
        	for topic,msg, t in bag1.read_messages() 
            	try: 
                	op.write(topic,msg,t)




