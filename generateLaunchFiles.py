#!/usr/bin/env python

import os
import getpass

# General Parameters (Simulation)
# Note: contrast_threshold for 3planes was 0.15 by default.
params = {"scene_name":None,"dataset_name":None,"contrast_threshold":0.2,"blur_size":3,"event_streaming_rate":60.0,"image_streaming_rate":40.0,"write_to_bag":True}
pkg_path = "/home/"+getpass.getuser()+"/catkin_ws/src/rpg_davis_simulator/"


# Read templates
f = open(pkg_path+"launch/templates/template_render.txt", "r")
contents_render = f.readlines()
f.close()

f = open(pkg_path+"launch/templates/template_simulate.txt", "r")
contents_sim = f.readlines()
f.close()

# Create for each .blend-file the regarding .launch-files
for file in os.listdir(pkg_path+"datasets/scenes/."):
    if file.endswith(".blend"):
        blenderscene = file.split(".")[0]
        print(os.path.join(".", blenderscene))
        params["scene_name"] = blenderscene
        params["dataset_name"] = blenderscene
        
        # Create Render File
        c_contents = contents_render[:]

        for idx,line in enumerate(c_contents):
            for key in params:
                pos = line.find(key)
                if pos<0:
                    continue
                pos += len(key) + 9
                c_contents[idx] = contents_render[idx][:pos] + str(params[key]) + contents_render[idx][pos:]
                #del params[key]
                break

        f = open(pkg_path+"launch/" + blenderscene + "_render.launch", "w+")
        c_contents = "".join(c_contents)
        f.write(c_contents)
        f.close()
        
        # Create Simulate File
        c_contents = contents_sim[:]

        for idx,line in enumerate(c_contents):
            for key in params:
                pos = line.find(key)
                if pos<0:
                    continue
                pos += len(key) + 9
                c_contents[idx] = contents_sim[idx][:pos] + str(params[key]) + contents_sim[idx][pos:]
                #del params[key]
                break
                
                
        f = open(pkg_path+"launch/" + blenderscene + "_simulate.launch", "w+")
        c_contents = "".join(c_contents)
        f.write(c_contents)
        f.close()       
