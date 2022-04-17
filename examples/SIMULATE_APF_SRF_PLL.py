import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Modules of the package py1phiPLL
from py1phiPLL.definitions import varPLL
from py1phiPLL.PLL import APF_SRF_PLL 

# set the font globally
plt.rcParams.update({'font.family':'sans-serif'})

# defining the object to store the results and control settings
apf_srf_1 = varPLL("APF-SRF-PLL")

# Defining the input signal
w_1 = 120*np.pi 
v_in = lambda ti: 5*np.sin(w_1*ti) 

# Simulation
t_start = 0
t_end = 0.2
t = np.linspace(t_start,t_end,5000)
y0 = [0.0, 0.0, 0.0, 0.0]
sol = solve_ivp(fun=APF_SRF_PLL,t_span=(t_start,t_end), y0=y0, t_eval=t, args=(v_in,apf_srf_1), method='BDF')


# Plotting the results: v_in, v_alpha, v_beta
fig_v = plt.figure() 
plt.plot(apf_srf_1.t,v_in(apf_srf_1.t),'k--',linewidth=2)
plt.plot(apf_srf_1.t,apf_srf_1.v_alpha,linewidth=3,alpha=0.7)
plt.plot(apf_srf_1.t,apf_srf_1.v_beta,linewidth=3)
plt.grid()
plt.legend(['$v_{in}$','$v_{\\alpha}$','$v_{\\beta}$'],loc='upper right')
plt.xlim([0,0.1])
plt.xlabel('Tempo - s')
plt.ylabel('Amplitude - V')


# # Plotting the results: error
fig_e = plt.figure()
plt.plot(apf_srf_1.t,apf_srf_1.w,linewidth=2)
plt.grid()
plt.legend(['$\omega$'],loc='upper right')
plt.xlim([0,0.1])
plt.xlabel('Tempo - s')
plt.ylabel('Amplitude - rad/s') 




# exporting the results
DF = apf_srf_1.exportDF()
#DF.to_csv('python_APF_SRF_PLL.csv')