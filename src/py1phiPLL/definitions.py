# Used Packages
import numpy as np
import pandas as pd


# Class 
class varPLL():


    """
    This class describes objects used to store results of the different types of single-phase PLLs.
    """
    def __init__(self,type):
        if(type == "SOGI"):
            var_keys = {'v_alpha', 'v_beta', 'e','t'}
            cons_keys = {('K',2.0),('w',120*np.pi)}
        elif(type == "SOGI-FLL"):
            var_keys = {'v_alpha', 'v_beta', 'e','wi','w','t'}
            cons_keys = {('K',2.0),('Kfll',-2000.0),('w0',300.0)}
        elif(type == "EPLL"):
            var_keys = {'e', 'ea', 'ef','wi','w','A','y','theta','t'}
            cons_keys = {('Kia',5000.0),('Kif',5000.0),('Kpf',100.0),('w0',300.0)}
        elif(type == "SRF-PLL"):
            var_keys = {'v_alpha', 'v_beta', 'v_d','v_q','wi','w','theta','A','y','t'}
            cons_keys = {('Kpf',50.0),('Kif',5000.0),('w0',300.0),('wc',120.0)}
        elif(type == "SOGI-SRF-PLL"):
            var_keys = {'v_alpha', 'v_beta', 'v_d','v_q','wi','w','theta','A','y','e','t'}
            cons_keys = {('Kpf',30.0),('Kif',1000.0),('w0',300.0),('wc',120.0),('K',2.0)}
        elif(type == "APF-SRF-PLL"):
            var_keys = {'v_alpha', 'v_beta', 'v_sigma','v_d','v_q','wi','w','theta','A','y','t'}
            cons_keys = {('Kpf',30.0),('Kif',1000.0),('w0',300.0),('wc',120.0)}

        self.__dict__.update((item, np.array([])) for item in var_keys)
        self.__dict__.update((item, valor) for item,valor in cons_keys)


    # Method for storing the results
    # Follow the var_keys order 
    def store(self,**kwargs):
        keys = list(self.__dict__.keys())        

        for item in keys:
            if (isinstance(self.__dict__[item], np.ndarray)):

                if(item in kwargs.keys()):
                    self.__dict__[item] = np.append(self.__dict__[item],kwargs[item])
    
    # Method to export dataframe
    def exportDF(self):
        keys = list(self.__dict__.keys())

        DF = pd.DataFrame(columns=[item for item in keys if isinstance(self.__dict__[item], np.ndarray)])

        for item in keys:
            if (isinstance(self.__dict__[item], np.ndarray)):
                DF[item] = self.__dict__[item]
        
        return DF

                


    

         