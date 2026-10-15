from rocketcea.cea_obj import CEA_Obj
import numpy as np
import math

# Constants
g = 9.81 # assigns 9.81 to the variable g
mix_eff = 0.8
p_amb = 14.7

# Conversion Ratios
feetToMeters = 0.3048
psiToPa = 6894.76


# ________Setpoints_________

# Running Stoich GH2/GOx:
o_f = 140
p_c = 13 # psia
thrust = 235 # N


def calculate_throat_area
    At=((mdot*math.sqrt(T0))/p0)*math.sqrt(((R/kt)*(((kt+1)/(2))**((kt+1)/(kt-1)))))
    print(f'Area: {At} m^2')
    dia=2*math.sqrt((At/math.pi))
    print(f'Diameter: {dia} m')
    diain = dia*39.37
    print(f'Diameter (in): {diain} in')

# Function to translate of, pc, thrust to a throat diameter
def GH2GOx_throat_sizing_function(of, pc, F):
    # Line above creates a function called GH2GOx_throat_sizing_function 
    # with inputs: of, pc, and F


    # Create a CEA Rocket Problem
    cea = CEA_Obj(oxName = "GOX", fuelName = "CH4")

    # Get Cstar
    cea.get_Cstar(Pc=pc, MR=of) * feetToMeters #returns c*

    # Use CEA to get exhaust velocity
    # Can't use get_Throat_Isp() because it returns vacuum isp, not ambient
    # Instead, we will use Coefficient of Thrust (CF)
    # ISP (m/s) = c* x CF
    cea.get_PambCf(Pamb = p_amb, Pc=pc, MR = of, eps=1)[0] # returns CF
    # Line above takes all of those inputs, and gives an array of outputs
    # where the first output [0] is your CF. So adding [0] will only return
    # CF back.


    print (g) # prints the value of variable g 


    print(f"ISP(m/s): {isp}") # print format to give the title (ISP) and units (m/s)
    v_e = isp * mix_eff # you must use a mixing efficiency debuff because perfect
    # combustion does not exist 
    print(f"Exhaust Velocity (m/s): {v_e}")

    ### Work through the rest of your code to return desired outputs ###


def main():
    GH2GOx_throat_sizing_function(o_f, p_c, thrust)

if __name__ == "__main__":
    main()