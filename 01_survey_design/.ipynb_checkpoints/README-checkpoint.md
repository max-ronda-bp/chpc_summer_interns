# Survey Design 

## Prompt:

Oil companies use several types of seismic acquisition to generate data that allows them to “see” beneath the surface of the Earth and predict where oil and gas might be found.  One of the means of acquisition is known as an ocean bottom node, or OBN.  These nodes are placed on the bottom of the sea floor.  A boat then crosses over the area with the nodes, using air guns to send a shock wave through the Earth.  These shock waves reflect off the layers in the subsurface and move the OBNs by a slight amount.  Each OBN records the movements it detects, and this data is processed to determine a picture of the subsurface. 

Your job is to help determine some of the specifics of the OBN placement.  Your colleagues know the dimensions for the rectangular area to be surveyed, and the amount of space needed between each node.  The **inputs** will be the **x and y of the rectangular** survey area, and **d, the distance between nodes.**  The **output** will be the **total number of nodes** needed for the survey.

The goal of this is to implement the function `calc_num_nodes()` and output the total number of nodes needed given specific inputs. 


### Ocean-Bottom Nodes Illustration (OBN)

<img src="images/01_img.PNG" align="center" width="600px">
<br>

### Helper Design:

<img src="images/02_img.PNG" align="left" width="400px">
<img src="images/03_img.PNG" align="left" width="400px">