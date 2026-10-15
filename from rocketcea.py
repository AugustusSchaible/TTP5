from rocketcea.cea_obj import CEA_Obj
import numpy as np
import matplotlib.pyplot as plt

g = 9.81 # assigns 9.81 to the variable g
mix_eff = 0.8
p_amb = 14.7

feetToMeters = 0.3048
psiToPa = 6894.76

cea = CEA_Obj(oxName = "LOX", fuelName = "CH4")


# Function to translate of, pc, thrust to a throat diameter
def exhaust_vel(isp, mix_eff):
    # Use CEA to get exhaust velocity
    # Can't use get_Throat_Isp() because it returns vacuum isp, not ambient
    # Instead, we will use Coefficient of Thrust (CF)
    # ISP (m/s) = c* x CF
    
    # Line above takes all of those inputs, and gives an array of outputs
    # where the first output [0] is your CF. So adding [0] will only return
    # CF back.

    
    print(f"ISP(m/s): {isp}") # print format to give the title (ISP) and units (m/s)
    v_e = isp * mix_eff # you must use a mixing efficiency debuff because perfect
    # combustion does not exist 
    print(f"Exhaust Velocity (m/s): {v_e}")
    return v_e
    ### Work through the rest of your code to return desired outputs ###

# def create_Cstar_array( p_c, o_f_array):
#     array = []
#     for i in o_f_array:
#         current = cea.get_Cstar(Pc=p_c, MR=o_f_array) * feetToMeters
#         array.append(current)
#     Cstar_array = np.array(array)
#     return Cstar_array



def create_o_f_array(o_f_end, iteration):
    array = []
    current = 0
    while current <= o_f_end:
        array.append(current)
        current += iteration
    o_f_array = np.array(array)
    return o_f_array

#def create_

def create_temp_array(p_c, o_f_array):
    array = []
    
    for i in o_f_array:
        current = cea.get_Tcomb(p_c, i) * (5/9)
        array.append(current)
    temp_array = np.array(array)
    return temp_array

def plot_temp_o_f(temp_array, o_f_array):
    plt.plot(o_f_array,temp_array)
    plt.title("Chamber temp over OF ratio")
    plt.xlabel("OF ratio")
    plt.ylabel("Chamber Temp [K]")
    plt.show()

def size_throat(mdot, pc, cstar): 
    At = mdot* (cstar/pc)
    return At


def main():
    o_f_end = 5
    iteration = .005
    pc = 10 #bar
    pc *= 14.504 #convert to psi 
    F = 15 # N  # F being capital is probably better in this situation 
    o_f_array = create_o_f_array(o_f_end, iteration)
    temp_array = create_temp_array(pc, o_f_array)
    #Cstar_array = create_Cstar_array(pc, o_f_array) 
    
    cstar =  cea.get_Cstar(Pc=145.04, MR= 3) *  0.3048 #get Cstar multiplied by conversion for ft to m
    
    of = 3
    Cf = cea.get_PambCf(Pamb = p_amb, Pc=pc, MR = of, eps=1)[0] # returns CF
    print(f'Cf = {Cf}')
    print(f'Cstar = {cstar}')
    isp = cstar*Cf
    ve= exhaust_vel(isp, mix_eff)
    mdot = F/ve
    at = size_throat(mdot, pc, cstar)
    print(f'Throat area: {at} m^2')
    



    plot_temp_o_f(temp_array, o_f_array)

  

#did u take a screenshot of the plot that got u a OF of 3

if __name__ == "__main__":
    main()