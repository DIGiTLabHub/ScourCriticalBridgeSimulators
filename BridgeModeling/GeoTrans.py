import openseespy.opensees as ops
def defineGeoTrans():
    # Define transformation IDs and types
    IDTransCol = 1
    IDTransCap = 2
    IDTransDeck = 3
    ColTransfType = 'Linear'
    
    # Define geometric transformations
    ops.geomTransf(ColTransfType, IDTransCol, -1.0000, 0.0000, 0)
    ops.geomTransf('Linear', IDTransCap, 0, 0, -1)
    ops.geomTransf('Linear', IDTransDeck, 0, 0, -1)
    
    # print("Geometric transformations applied successfully.")