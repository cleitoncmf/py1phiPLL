import numpy as np


# Function to represent the state equation of the SOGI 
# v_in must be an anonimous function (lambda function)
def SOGI(t,y,v_in,pll):

    """
    teste
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

# Function
def SOGI_FLL(t,y,v_in,pll):

    """
    asdsdasdsa
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


# EPLL
def EPLL(y,t,v_in,pll):

    theta,wi,A = y


    # stored constants
    Kia = pll.Kia
    Kif = pll.Kif
    Kpf = pll.Kpf
    w0 = pll.w0


    # Processing
    y = A*np.sin(theta)
    e = v_in(t) - y
    ef = e*np.cos(theta)
    ea = e*np.sin(theta)
    w = wi + Kpf*ef + w0

    d_theta = w
    d_wi = Kif*ef
    d_A = Kia*ea

    # Storing results
    pll.store(t=t, e=e, w=w, y=y, A=A, ef=ef, ea=ea, wi=wi, theta=theta)

    return [d_theta, d_wi, d_A]


# SOGI-SRF-PLL
def SOGI_SRF_PLL(t,y,v_in,pll):


    theta, wi, A, v_alpha, v_beta = y


    # stored constants
    Kif = pll.Kif
    Kpf = pll.Kpf
    w0 = pll.w0
    wc = pll.wc
    K = pll.K


    # Processing
    y = A*np.sin(theta)
    v_d = np.cos(theta)*v_alpha + np.sin(theta)*v_beta 
    v_q = -np.sin(theta)*v_alpha + np.cos(theta)*v_beta
    
    w = wi + Kpf*v_d + w0

    e = v_in(t) - v_alpha
    d_v_alpha = w*(K*e-v_beta)
    d_v_beta = w*v_alpha

    d_theta = w
    d_wi = Kif*v_d
    d_A = - wc*(v_q + A)

    # Storing results
    pll.t = np.append(pll.t,t)
    pll.y = np.append(pll.y,y)
    pll.A = np.append(pll.A,A)
    pll.v_d = np.append(pll.v_d,v_d)
    pll.v_q = np.append(pll.v_q,v_q)
    pll.w = np.append(pll.w,w)
    pll.wi = np.append(pll.wi,wi)
    pll.theta = np.append(pll.theta,theta)
    pll.e = np.append(pll.e,e)
    pll.v_alpha = np.append(pll.v_alpha,v_alpha)
    pll.v_beta = np.append(pll.v_beta,v_beta) 

    return [d_theta, d_wi, d_A, d_v_alpha, d_v_beta]


# APF-SRF-PLL
def APF_SRF_PLL(t,y,v_in,pll):

    theta, wi, A, v_sigma= y


    # stored constants
    Kif = pll.Kif
    Kpf = pll.Kpf
    w0 = pll.w0
    wc = pll.wc
    


    # Processing

    v_alpha = v_in(t)
    v_beta = v_sigma - v_in(t) 

    y = A*np.sin(theta)
    v_d = np.cos(theta)*v_alpha + np.sin(theta)*v_beta
    v_q = -np.sin(theta)*v_alpha + np.cos(theta)*v_beta
    
    w = wi + Kpf*v_d + w0

    
    
    d_v_sigma = w*(v_in(t) - v_beta)
    d_theta = w
    d_wi = Kif*v_d
    d_A = - wc*(v_q + A)

    # Storing results
    pll.t = np.append(pll.t,t)
    pll.y = np.append(pll.y,y)
    pll.A = np.append(pll.A,A)
    pll.v_d = np.append(pll.v_d,v_d)
    pll.v_q = np.append(pll.v_q,v_q)
    pll.w = np.append(pll.w,w)
    pll.wi = np.append(pll.wi,wi)
    pll.theta = np.append(pll.theta,theta)
    
    pll.v_alpha = np.append(pll.v_alpha,v_alpha)
    pll.v_beta = np.append(pll.v_beta,v_beta) 
    pll.v_sigma = np.append(pll.v_sigma,v_sigma) 

    return [d_theta, d_wi, d_A, d_v_sigma]