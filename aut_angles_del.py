#todo exec(open(r"C:\PhD\Irumee/calc_angles.py").read())
#todo the above is needed in Slicer to run the following script
#todo exec(open(r"C:\PhD\Irumee/aut_angles_del.py").read())

import numpy as np

# Print angles between slice nodes
def ShowAngle(unused1=None, unused2=None,lineNodeNames=None):

  lineDirectionVectors = []
  for lineNodeName in lineNodeNames:
    lineNode = slicer.util.getFirstNodeByClassByName("vtkMRMLMarkupsLineNode", lineNodeName)
    lineStartPos = np.zeros(3)
    lineEndPos = np.zeros(3)
    lineNode.GetNthControlPointPositionWorld(0, lineStartPos)
    lineNode.GetNthControlPointPositionWorld(1, lineEndPos)
    lineDirectionVector = (lineEndPos-lineStartPos)/np.linalg.norm(lineEndPos-lineStartPos)
    lineDirectionVectors.append(lineDirectionVector)
  angleRad = vtk.vtkMath.AngleBetweenVectors(lineDirectionVectors[0], lineDirectionVectors[1])
  angleDeg = vtk.vtkMath.DegreesFromRadians(angleRad)
  #print("Angle between lines {0} and {1} = {2:0.3f}".format(lineNodeNames[0], lineNodeNames[1], angleDeg))
  return angleDeg


# Read line 'IP Cochlea' (created from 'MarkupsFiducial_1' and 'MarkupsFiducial_2')
#line_IP_Cochlea = slicer.util.getFirstNodeByClassByName("vtkMRMLMarkupsLineNode", "IP Cochlea")

# Create line 'IP Cochlea' (automatically created from 'IP RW' and 'IP Cochlea')
# Read 'IP RW' and 'IP Cochlea'
pos1 = vtk.vtkVector3d(0,0,0)
node1 = slicer.util.getNode("IP RW")
node1.GetNthControlPointPositionWorld(0,pos1)

pos2 = vtk.vtkVector3d(0,0,0)
node2 = slicer.util.getNode("IP Cochlea")
node2.GetNthControlPointPositionWorld(0,pos2)

line_IP_Cochlea = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode","IP Cochlea line aut")
line_IP_Cochlea.AddControlPoint(pos1)
line_IP_Cochlea.AddControlPoint(pos2)
DisplayNode = getNode('IP Cochlea line aut').GetDisplayNode()
DisplayNode.SetSelectedColor(1,0,0)
#print(line_IP_Cochlea)

# Read line 'IP CNVII' (created from 'MarkupsFiducial_3' and 'MarkupsFiducial_5')
#line_IP_CNVII = slicer.util.getFirstNodeByClassByName("vtkMRMLMarkupsLineNode", "IP CNVII")


# Create line 'IP CNVII' (automatically created from 'MarkupsFiducial_3' and 'MarkupsFiducial_5')
# Read MarkupsFiducial_3 and MarkupsFiducial_5
pos3 = vtk.vtkVector3d(0,0,0)
node3 = slicer.util.getNode("IP CN VIIa")
node3.GetNthControlPointPositionWorld(0,pos3)

pos5 = vtk.vtkVector3d(0,0,0)
node5 = slicer.util.getNode("IP CN VIIb")
node5.GetNthControlPointPositionWorld(0,pos5)

line_IP_CNVII = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode","IP CNVII line aut")
line_IP_CNVII.AddControlPoint(pos3)
line_IP_CNVII.AddControlPoint(pos5)
DisplayNode = getNode('IP CNVII line aut').GetDisplayNode()
DisplayNode.SetSelectedColor(0,1,0)


# Calculate 'IP horizontal angle'
lineNodeNames = ["IP Cochlea line aut", "IP CNVII line aut"]
horizontal_angle=ShowAngle(line_IP_Cochlea,line_IP_CNVII,lineNodeNames)
print("IP horizontal angle",horizontal_angle)


# #############################################################################################################
# #############################################################################################################
#
# # Plane is created automatically by adding the control points
#
# #############################################################################################################
# Plane is calculated from 'IP CN VIIa' , 'IP CN VIIb' , 'IP Incus'

#
new_planeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode","IP Plane aut")
pos3 = vtk.vtkVector3d(0,0,0)
node3 = slicer.util.getNode("IP CN VIIa")
node3.GetNthControlPointPositionWorld(0,pos3)

node5 = slicer.util.getNode("IP CN VIIb")
pos5 = vtk.vtkVector3d(0,0,0)
node5.GetNthControlPointPositionWorld(0,pos5)

node6 = slicer.util.getNode("IP Incus")
pos6 = vtk.vtkVector3d(0,0,0)
node6.GetNthControlPointPositionWorld(0,pos6)
new_planeNode.AddControlPoint(pos6)
new_planeNode.AddControlPoint(pos5)
new_planeNode.AddControlPoint(pos3)


# Get Normal Vector from plane
planeNode = new_planeNode
planeNormalVector = [0.0, 0.0, 0.0]
planeNode.GetNormalWorld(planeNormalVector)

# Calculate the vector which is perpedicular to the IP CN VII line and belongs to the plane
# So cross product is used.
resultVector = [0.0, 0.0, 0.0]

CNVIIlineNode = slicer.util.getFirstNodeByClassByName("vtkMRMLMarkupsLineNode", "IP CNVII line aut")
lineStartPos = np.zeros(3)
lineEndPos = np.zeros(3)
CNVIIlineNode.GetNthControlPointPositionWorld(0, lineStartPos)
CNVIIlineNode.GetNthControlPointPositionWorld(1, lineEndPos)
CNVIIlineDirectionVector = (lineEndPos-lineStartPos)/np.linalg.norm(lineEndPos-lineStartPos)

vtk.vtkMath.Cross(planeNormalVector, CNVIIlineDirectionVector,resultVector)


COCHLlineNode = slicer.util.getFirstNodeByClassByName("vtkMRMLMarkupsLineNode", "IP Cochlea line aut")
lineStartPos = np.zeros(3)
lineEndPos = np.zeros(3)
COCHLlineNode.GetNthControlPointPositionWorld(0, lineStartPos)
COCHLlineNode.GetNthControlPointPositionWorld(1, lineEndPos)
COCHLlineDirectionVector = (lineEndPos-lineStartPos)/np.linalg.norm(lineEndPos-lineStartPos)


# Calculate 'Vertical Angle IP'
# Calculate the angle between normal vector and vector of line
angleRad = vtk.vtkMath.AngleBetweenVectors(resultVector, COCHLlineDirectionVector)
vertical_angle = vtk.vtkMath.DegreesFromRadians(angleRad)
print("IP vertical angle: ",vertical_angle )


