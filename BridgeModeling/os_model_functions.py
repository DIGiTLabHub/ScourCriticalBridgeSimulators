# some opensees-py common unitility functions are defined here.
import openseespy.opensees as ops
import numpy as np

# Function to define nodes
def define_nodes(nodes):
    for node_id, x, y, z in nodes:
        ops.node(node_id, x, y, z)


# Function to apply restraints including nodal fixity
def apply_restraints(restraints):
    for node_id, dx, dy, dz, rx, ry, rz in restraints:
        ops.fix(node_id, dx, dy, dz, rx, ry, rz)  # Apply fixity
        # print(f"Applied fixity to node {node_id}: [{dx}, {dy}, {dz}, {rx}, {ry}, {rz}]")

# Function to apply constraints using OpenSeesPy
def apply_constraints(constraints):
    for retained, constrained, dof in constraints:
        ops.equalDOF(retained, constrained, *dof)  # Apply equalDOF constraint
        # print(f"✔ Constraint applied: Node {constrained} follows Node {retained} on DOFs {dof}")

# Function to apply structural masses
def apply_masses(masses):
    """
    Applies mass to each node using OpenSeesPy.
    """
    for mass in masses:
        nodeTag, mX, mY, mZ, mRX, mRY, mRZ = mass
        ops.mass(nodeTag, mX, mY, mZ, mRX, mRY, mRZ)  # Apply nodal mass
        # print(f"✔ Mass applied at Node {nodeTag}: {mX}, {mY}, {mZ}, {mRX}, {mRY}, {mRZ}")
    
    return masses  # ✅ Return applied mass list for verification




def eigen_analysis(n_modes):
    """
    Perform eigenvalue analysis and return the first n_modes natural frequencies.
    
    Parameters:
        n_modes (int): Number of modes to compute.
    
    Returns:
        list: The first n_modes natural frequencies in Hz.
    """
    eigenvalues = ops.eigen('-genBandArpack', n_modes)  # Correct syntax
    
    if not eigenvalues:
        print("Error: Eigenvalue analysis failed.")
        return []

    # Convert eigenvalues to natural frequencies (Hz)
    frequencies = [np.sqrt(lam) / (2 * np.pi) if lam > 0 else 0 for lam in eigenvalues]
    
    return frequencies
