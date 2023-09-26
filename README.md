# Automatic Angle Calculation
This repository contains the implementation that we developed to perform automatic calculation 
and visualization of the horizontal and vertical angles as well as the auxilary lines and planes, as presented in the paper: 
"The impact of the size and angle of the cochlear basal turn on translocation of a pre-curved mid-scala cochlear implant electrode"

## 1. Download and Install 3D Slicer
3D Slicer can be downloaded from https://download.slicer.org/

## 2. Placing fiducials in 3D Slicer
Define the following five fiducials using ```Markups``` module provided by 3D Slicer. Please, ensure that you use the following names for the fiducials:\
a. IP RW \
b. IP Cochlea \
c. IP CN VIIa \
d. IP CN VIIb \
e. IP Incus 

## 3. Run the python script through 3D Slicer

a. Navigate to the menu bar and select View->Python Interactor \
b. Download the github repo to your desired path\
c. In the Python Interactor Shell, type: ```exec(open(r"/aut_angles_calc.py").read())``` \
d. Press ```ENTER``` to run the script and automatically calculate the vertical and horizontal angles




## Citation
If you use this code for your research, please cite our paper:

