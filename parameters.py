
# =======================================
# Central Parameter File: params.py
# For Surrogate Learning of Scoured Bridges
# =======================================

# 1. Geometry & Structural Dimensions
span_length_m = 35
deck_width_m = 12
num_spans = 4
column_height_m = 8.0  # assumed or to be updated

# 2. Material Properties
fc_mean = 27.0  # MPa
fc_std = 1.0
fy_mean = 420.0  # MPa
fy_std = 4.2

# 3. Soil-Spring Modeling
py_spring_type = 'PySimple1'
soil_spring_behavior = ['p-y', 't-z', 'q-z']
scour_increment_m = 0.25  # assumed scour step

# 4. Pushover Simulation
max_drift_ratio = 0.05
pushover_direction_dof = 2
num_integration_pts = 5
solver_strategy = ['Newton', 'Broyden', 'Krylov']

# 5. Flow Scenarios (velocity in m/s)
flow_scenarios = {
    "missouri": 2.9,
    "colorado": 6.5,
    "extreme": 10.0
}

# 6. Erosion Rates (mm/h)
erosion_rates_mm_per_hr = {
    "missouri": 100,
    "colorado": 500,
    "extreme": 1000
}

# 7. Scour Hazard Modeling
kinematic_viscosity = 1.0e-6  # m²/s (approximate for water at 20°C)
pier_diameter_m = 1.5  # assumed
density_water = 1000  # kg/m³
years_of_exposure = 50
num_lhs_samples_per_scenario = 1000

# 8. Surrogate Modeling Features
use_engineered_features = True
engineered_features = [
    "Sz", "Sz_sq", "Sz_cu", "log_Sz", "inv_Sz", "sqrt_Sz"
]

# 9. Surrogate Modeling Targets
capacity_tuple = ['Vy', 'Dy', 'My', 'Thy']

# 10. SVR Hyperparameters
svr_kernel = 'rbf'
svr_C = 100
svr_epsilon = 0.01
svr_gamma = 0.1

# 11. GBR Hyperparameters
gbr_num_trees = 700
gbr_learning_rate = 0.015
gbr_max_depth = 3
gbr_subsample = 0.85

# 12. Bootstrap Ensemble Settings
bootstrap_ensemble_size = 30

# 13. Uncertainty Quantification
scour_distribution_type = 'lognormal'
credal_prediction_method = 'bootstrap'
credal_prediction_bounds = ['min', 'max']

# 14. Output Variables
output_variables = {
    "Vy": "yield_base_shear",
    "Dy": "yield_displacement",
    "My": "yield_moment",
    "Thy": "yield_rotation"
}
