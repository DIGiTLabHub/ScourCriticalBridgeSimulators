#!/usr/bin/env python
# coding: utf-8

# In[1]:


# model_setup.py
import openseespy.opensees as ops
from os_model_functions import *
from Node import nodes
from Restraint import restraints
from Constraint import constraints
from Mass import masses
from GeoTrans import defineGeoTrans
from SectionMat import defineSectionMaterials
from ColSection import defineColSection
from Element import define_elements
from ZeroLengthElement import defineZeroLengthElement
from GravityLoad import  defineLoads 

def build_model(fc, fy, scourDepth=0):
    ops.wipe()
    ops.model('basic', '-ndm', 3, '-ndf', 6)
    define_nodes(nodes)
    apply_restraints(restraints)
    apply_constraints(constraints)
    apply_masses(masses)
    defineGeoTrans()
    defineSectionMaterials(fc, fy)  # ← Pass random fc and fy here
    defineColSection()
    define_elements()
    defineZeroLengthElement(scourDepth)
    defineLoads()



