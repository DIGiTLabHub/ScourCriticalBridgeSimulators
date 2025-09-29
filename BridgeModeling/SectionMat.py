import openseespy.opensees as ops

def defineSectionMaterials(fc, fy):
    """
    Define section materials using random input values:
    - fc: concrete compressive strength in MPa (positive value, will be negated internally)
    - fy: steel yield strength in MPa
    """

    # Material tags
    IDconcU = 1
    IDconcCCol = 2
    IDconcCCap = 3
    IDreinf = 4

    # Concrete01 parameters
    fcU = -abs(fc)
    eps_c0 = -0.002
    fcU_res = 0.2 * abs(fc)
    eps_u = -0.005
    
    # Define concrete materials using random fc
    ops.uniaxialMaterial("Concrete01", IDconcU, fcU, eps_c0, -fcU_res, eps_u)
    ops.uniaxialMaterial("Concrete01", IDconcCCol, fcU, eps_c0, -fcU_res, eps_u)
    ops.uniaxialMaterial("Concrete01", IDconcCCap, fcU, eps_c0, -fcU_res, eps_u)

    # Define steel material using random fy
    E0 = 200000.0  # MPa
    b = 0.007
    R0, cR1, cR2 = 15.0, 0.9, 0.2
    ops.uniaxialMaterial("Steel02", IDreinf, fy, E0, b, R0, cR1, cR2)

    # ops.uniaxialMaterial("Steel02", IDreinf, 420.0, 200000.0, 0, 18.0, 0.925, 0.15)
    # ops.uniaxialMaterial("Steel01", IDreinf, 420.0, 200000.0, 0.0066)
    
    # ops.uniaxialMaterial("Concrete01", IDconcU, -25.0, -0.0020, -5.0, -0.0050)
    # ops.uniaxialMaterial("Concrete01", IDconcCCol, -26.7, -0.0021, -5.3, -0.0131)
    # ops.uniaxialMaterial("Concrete01", IDconcCCap, -26.7, -0.0021, -5.3, -0.0131)
    # ops.uniaxialMaterial("Steel02", IDreinf, 420.0, 200000.0, 0.001, 15.0, 0.9, 0.2)
    
    # Define PySimple1 materials
    ops.uniaxialMaterial("Elastic", 21, 36902390435.1)
    ops.uniaxialMaterial("Elastic", 22, 17255729166.7)
    ops.uniaxialMaterial("Elastic", 31, 16963625131279872.0)
    ops.uniaxialMaterial("Elastic", 32, 5667317587876813.0)
    ops.uniaxialMaterial("ElasticPP", 51, 3500.0, 47.0)
    ops.uniaxialMaterial("ElasticPPGap", 52, 150383.1, -253338.0, -50.0)
    ops.uniaxialMaterial("ElasticPPGap", 53, 590534.7, -10000000000.0, -50.0)
    ops.uniaxialMaterial("ElasticPPGap", 54, 3401843.8, -1569750.0, -25.0)
    ops.uniaxialMaterial("ENT", 61, 70875.0)
    ops.uniaxialMaterial("ENT", 62, 10500.0)
    ops.uniaxialMaterial("Elastic", 63, 10500.0)
    ops.uniaxialMaterial("PySimple1", 101, 2, 90.54, 7.522, 1)
    ops.uniaxialMaterial("PySimple1", 102, 2, 11700, 9.720, 1)
    ops.uniaxialMaterial("PySimple1", 103, 2, 28800, 11.963, 1)
    ops.uniaxialMaterial("PySimple1", 104, 2, 51300, 14.206, 1)
    ops.uniaxialMaterial("PySimple1", 105, 2, 79200, 16.449, 1)
    ops.uniaxialMaterial("PySimple1", 106, 2, 112500, 18.692, 1)
    ops.uniaxialMaterial("PySimple1", 107, 2, 151200, 20.935, 1)
    ops.uniaxialMaterial("PySimple1", 108, 2, 195300, 23.178, 1)
    ops.uniaxialMaterial("PySimple1", 109, 2, 244800, 25.421, 1)
    ops.uniaxialMaterial("PySimple1", 110, 2, 299700, 27.664, 1)
    ops.uniaxialMaterial("PySimple1", 111, 2, 360000, 29.907, 1)
    ops.uniaxialMaterial("PySimple1", 112, 2, 425700, 32.150, 1)
    ops.uniaxialMaterial("PySimple1", 113, 2, 496800, 34.393, 1)
    ops.uniaxialMaterial("PySimple1", 114, 2, 573300, 36.636, 1)
    ops.uniaxialMaterial("PySimple1", 115, 2, 655200, 38.879, 1)
    ops.uniaxialMaterial("PySimple1", 116, 2, 742500, 41.122, 1)
    ops.uniaxialMaterial("PySimple1", 117, 2, 835200, 43.365, 1)
    ops.uniaxialMaterial("PySimple1", 118, 2, 933300, 45.608, 1)
    ops.uniaxialMaterial("PySimple1", 119, 2, 1036800, 47.851, 1)
    ops.uniaxialMaterial("PySimple1", 120, 2, 1145700, 50.094, 1)
    ops.uniaxialMaterial("PySimple1", 121, 2, 1260000, 52.337, 1)
    ops.uniaxialMaterial("PySimple1", 122, 2, 2970000, 56.075, 1)
    ops.uniaxialMaterial("PySimple1", 123, 2, 3240000, 56.075, 1)
    ops.uniaxialMaterial("PySimple1", 124, 2, 3510000, 56.075, 1)
    ops.uniaxialMaterial("PySimple1", 125, 2, 3780000, 56.075, 1)
    ops.uniaxialMaterial("PySimple1", 126, 2, 4050000, 56.075, 1)
    ops.uniaxialMaterial("PySimple1", 127, 2, 4320000, 56.075, 1)
    ops.uniaxialMaterial("PySimple1", 128, 2, 4590000, 56.075, 1)
    ops.uniaxialMaterial("PySimple1", 129, 2, 4860000, 56.075, 1)
    ops.uniaxialMaterial("PySimple1", 130, 2, 5130000, 56.075, 1)
    
    # Define TzSimple1 materials
    ops.uniaxialMaterial("TzSimple1", 201, 2, 20.58, 0.002)
    ops.uniaxialMaterial("TzSimple1", 202, 2, 2099.37, 0.186)
    ops.uniaxialMaterial("TzSimple1", 203, 2, 4157.57, 0.368)
    ops.uniaxialMaterial("TzSimple1", 204, 2, 6215.77, 0.550)
    ops.uniaxialMaterial("TzSimple1", 205, 2, 8273.98, 0.732)
    ops.uniaxialMaterial("TzSimple1", 206, 2, 10332.18, 0.914)
    ops.uniaxialMaterial("TzSimple1", 207, 2, 12390.38, 1.096)
    ops.uniaxialMaterial("TzSimple1", 208, 2, 14448.59, 1.278)
    ops.uniaxialMaterial("TzSimple1", 209, 2, 16506.79, 1.459)
    ops.uniaxialMaterial("TzSimple1", 210, 2, 18564.99, 1.641)
    ops.uniaxialMaterial("TzSimple1", 211, 2, 20623.20, 1.823)
    ops.uniaxialMaterial("TzSimple1", 212, 2, 22681.40, 2.005)
    ops.uniaxialMaterial("TzSimple1", 213, 2, 24739.60, 2.187)
    ops.uniaxialMaterial("TzSimple1", 214, 2, 26797.81, 2.369)
    ops.uniaxialMaterial("TzSimple1", 215, 2, 28856.01, 2.551)
    ops.uniaxialMaterial("TzSimple1", 216, 2, 30914.21, 2.733)
    ops.uniaxialMaterial("TzSimple1", 217, 2, 32972.42, 2.915)
    ops.uniaxialMaterial("TzSimple1", 218, 2, 35030.62, 3.097)
    ops.uniaxialMaterial("TzSimple1", 219, 2, 37088.82, 3.279)
    ops.uniaxialMaterial("TzSimple1", 220, 2, 39147.02, 3.461)
    ops.uniaxialMaterial("TzSimple1", 221, 2, 41205.23, 3.643)
    ops.uniaxialMaterial("TzSimple1", 222, 2, 86526.86, 7.650)
    ops.uniaxialMaterial("TzSimple1", 223, 2, 90643.27, 8.014)
    ops.uniaxialMaterial("TzSimple1", 224, 2, 94759.67, 8.378)
    ops.uniaxialMaterial("TzSimple1", 225, 2, 98876.08, 8.742)
    ops.uniaxialMaterial("TzSimple1", 226, 2, 102992.49, 9.106)
    ops.uniaxialMaterial("TzSimple1", 227, 2, 107108.89, 9.470)
    ops.uniaxialMaterial("TzSimple1", 228, 2, 111225.30, 9.834)
    ops.uniaxialMaterial("TzSimple1", 229, 2, 115341.71, 10.198)
    ops.uniaxialMaterial("TzSimple1", 230, 2, 119458.11, 10.562)

    # print("Section materials defined.")

