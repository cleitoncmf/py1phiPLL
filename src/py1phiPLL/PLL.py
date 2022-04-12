import numpy as np




# Function to represent the state equation of the SOGI 
# v_in must be an anonimous function (lambda function)
def SOGI(y,t,v_in,pll):
     
    v_alpha, v_beta = y
  
    # stored constants
    K = pll.K
    w = pll.w
  
    # Processing
    e = v_in(t) - v_alpha

    d_v_alpha = w*(K*e-v_beta)
    d_v_beta = w*v_alpha

    # Storing results
    pll.store(t=t,e=e,v_alpha=v_alpha,v_beta=v_beta)

    return [d_v_alpha,d_v_beta]