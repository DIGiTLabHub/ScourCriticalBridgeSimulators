#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import openseespy.opensees as op

def define_recorders(folder='RecorderData'):
    os.makedirs(folder, exist_ok=True)

    # Column 3101
    op.recorder('Element', '-file', os.path.join(folder, 'ColLocForce.3101.out'), '-time', '-ele', 3101, 'localForce')
    for col_id in [3201, 3301]:
        op.recorder('Element', '-file', os.path.join(folder, f'ColLocForce.{col_id}.out'), '-time', '-ele', col_id, 'localForce')


def define_displacement_recorders(folder='RecorderData'):
    os.makedirs(folder, exist_ok=True)
    # Column node displacements
    op.recorder('Node', '-file', os.path.join(folder, 'ColDisplacement.3101.out'), '-time',
                '-node', 3101, 3102, '-dof', 1, 2, 3, 4, 5, 6, 'disp')
    op.recorder('Node', '-file', os.path.join(folder, 'ColDisplacement.3201.out'), '-time',
                '-node', 3201, 3202, '-dof', 1, 2, 3, 4, 5, 6, 'disp')
    op.recorder('Node', '-file', os.path.join(folder, 'ColDisplacement.3301.out'), '-time',
                '-node', 3301, 3302, '-dof', 1, 2, 3, 4, 5, 6, 'disp')
# [5101, 5201, 5301]
    # Individual node displacements (6 DOF)
    for node_id in [5201]:
        op.recorder('Node', '-file', os.path.join(folder, f'Displacement.{node_id}.out'), '-time',
                    '-node', node_id, '-dof', 1, 2, 3, 4, 5, 6, 'disp')
