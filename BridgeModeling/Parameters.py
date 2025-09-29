#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Parameters to be used during modeling, static, and dynamic analyses

# ----------------------------
#      Modeling parameters
# ----------------------------

# Gravity Analysis parameters
grav_tol = 1.0e-8   # Convergence tolerance for gravity analysis
grav_iter = 3000    # Maximum number of iterations for gravity analysis
grav_incr = 0.1     # Load increment for gravity analysis
grav_nincr = 10     # Number of increments for gravity load analysis

# ----------------------------
# Dynamic Analysis parameters
# ----------------------------
dyn_tol = 1.0e-8    # Convergence tolerance for dynamic analysis
dyn_iter = 10       # Maximum number of iterations for dynamic analysis
dyn2_tol = 1.0e-6   # Secondary convergence tolerance for dynamic analysis
dyn2_iter = 200     # Secondary maximum iterations
dyn3_tol = 1.0e-4   # Tertiary convergence tolerance for dynamic analysis
dyn3_iter = 4000    # Tertiary maximum iterations
BroyCount = 8       # Broyden count for iterative solver
