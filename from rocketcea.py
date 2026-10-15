from rocketcea.cea_obj import CEA_Obj
import numpy as np

g = 9.81 # assigns 9.81 to the variable g
mix_eff = 0.8
p_amb = 14.7

feetToMeters = 0.3048
psiToPa = 6894.76

"""
o_f = 140
p_c = 13 # psia
thrust = 235 # N
# Thrust 
F = 66.7233
#Specific Heat
kc = 1.1404
kt = 1.1426
ke = 1.1995
kn = 1.2
#O/F Ratio
OF = 5
#Exit Pressure (atm)
Peatm = 1
#Temperatures (K)
T0 = 2952.39
Te = 2220.51
#Molar Weight at Throat (mwt, from NASA CEA)
mwt=26.404
#Chamber Pressure (psi)
p0psi = 100
"""
cea = CEA_Obj(oxName = "LOX", fuelName = "RP1")


# Function to translate of, pc, thrust to a throat diameter
def GH2GOx_throat_sizing_function(of, pc, F):
    # Line above creates a function called GH2GOx_throat_sizing_function 
    # with inputs: of, pc, and F


    # Create a CEA Rocket Problem
    cea = CEA_Obj(oxName = "GOX", fuelName = "RP1")

    # Get Cstar

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


def create_o_f_array(o_f_end, iteration):
    array = []
    current = 0
    while current <= o_f_end:
        array.append(current)
        current += iteration
    return array


def main():
   o_f_end = float(input("input the last value in the OF ratio array: "))
   iteration = float(input("enter the iteration value in the array (ex: steps of 0.005): "))
   thrust = float(input("enter the thrust: "))
   o_f_array = create_o_f_array(o_f_end, iteration)
   print (o_f_array)

#hi gus part 2


if __name__ == "__main__":
    main()