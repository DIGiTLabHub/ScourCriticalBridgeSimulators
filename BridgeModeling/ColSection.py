#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import openseespy.opensees as ops
def defineColSection():

    # Define material IDs
    IDconcU = 1
    IDconcCCol = 2
    IDreinf = 4
    
    # Define fiber section
    ops.section('Fiber', 11, '-torsion', 31)
    
    # Define patches
    ops.patch('quad', IDconcU, 56, 1, -1400.0, -600.0, 1400.0, -600.0, 1400.0, -550.0, -1400.0, -550.0)
    ops.patch('quad', IDconcU, 56, 1, -1400.0, 550.0, 1400.0, 550.0, 1400.0, 600.0, -1400.0, 600.0)
    ops.patch('circ', IDconcU, 12, 1, -1400.0, 0.0, 550.0, 600.0, 90.0, 270.0)
    ops.patch('circ', IDconcU, 12, 1, 1400.0, 0.0, 550.0, 600.0, 270.0, 450.0)
    ops.patch('quad', IDconcCCol, 56, 22, -1400.0, -550.0, 1400.0, -550.0, 1400.0, 550.0, -1400.0, 550.0)
    ops.patch('circ', IDconcCCol, 12, 11, -1400.0, 0.0, 0.0, 550.0, 90.0, 270.0)
    ops.patch('circ', IDconcCCol, 12, 11, 1400.0, 0.0, 0.0, 550.0, 270.0, 450.0)
    
    # Define reinforcement layers
    ops.layer('straight', IDreinf, 17, 804.2, -1241.4, -522.0, 1241.4, -522.0)
    ops.layer('straight', IDreinf, 17, 804.2, -1241.4, 522.0, 1241.4, 522.0)
    ops.layer('circ', IDreinf, 11, 804.2, -1400.0, 0.0, 522.0, 90.0, 270.0)
    ops.layer('circ', IDreinf, 11, 804.2, 1400.0, 0.0, 522.0, 270.0, 450.0)
    
    # Define aggregator section
    ops.section('Aggregator', 1, 21, 'Vy', 21, 'Vz', 31, 'T', '-section', 11)
    
    # print("ColSection defined.")
