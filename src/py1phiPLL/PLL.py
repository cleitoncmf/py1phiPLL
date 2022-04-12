import numpy as np




# Function to represent the state equation of the SOGI 
# v_in must be an anonimous function (lambda function)
def SOGI(t,y,v_in,pll):

    """
    .. automodapi:: py1phiPLL.SOGI
    """
     
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


def SOGI_FLL(t,y,v_in,pll):

    """
    .. automodapi:: py1phiPLL.SOGI_FLL
    """

    v_alpha, v_beta, wi = y

    # stored constants
    K = pll.K
    Kfll = pll.Kfll
    w0 = pll.w0

    # Processing
    e = v_in(t) - v_alpha
    w = w0 + wi

    d_v_alpha = w*(K*e-v_beta)
    d_v_beta = w*v_alpha
    d_wi = Kfll*e*v_beta
  

    # Storing results
    pll.store(t=t, e=e, v_alpha=v_alpha, v_beta=v_beta, w=w)
  
    return [d_v_alpha,d_v_beta,d_wi]