import unittest
import numpy as np
from xfab import tools
from xrd_simulator.polycrystal import Polycrystal
import matplotlib.pyplot as plt
from scipy.signal import convolve
from xfab import tools
import time
from xrd_simulator import laue, utils

np.random.seed(5)
U = np.eye(3,3)
strain_tensor = np.zeros((6,))
unit_cell = [4.926, 4.926, 5.4189, 90., 90., 120.]
B = tools.epsilon_to_b( strain_tensor, unit_cell )
wavelength = 0.285227
D = 142938.28756189224 #microns
detector = np.zeros((2048,2048))
pixsize = 75 #microns

x = np.array([1.,0.,0.])
omega = np.linspace(0., np.pi, 9)
ks = np.array( [ np.array([[np.cos(om),-np.sin(om),0],[np.sin(om),np.cos(om),0],[0,0,1]]).dot(x) for om in omega])
ks = 2*np.pi*ks/wavelength

hklrange = 5
for _ in range(25): # sample of 10 crystals

    phi1, PHI, phi2 = np.random.rand(3,)*2*np.pi
    U = tools.euler_to_u(phi1, PHI, phi2)
    for hmiller in range(-hklrange,hklrange):
        for kmiller in range(-hklrange,hklrange):
            for lmiller in range(-hklrange,hklrange):
                G_hkl = np.array( [hmiller,kmiller,lmiller] )
                for i in range(len(ks)-1):
                    
                    G             = laue.get_G(U, B, G_hkl)
                    theta         = laue.get_bragg_angle(G, wavelength)                    
                    rotator       = utils.PlanarRodriguezRotator( ks[i], ks[i+1] )
                    c_0, c_1, c_2 = laue.get_tangens_half_angle_equation(ks[i], theta, G, rotator.rhat ) 
                    s1, s2        = laue.find_solutions_to_tangens_half_angle_equation( c_0, c_1, c_2, rotator.alpha )

                    for j,s in enumerate([s1, s2]):
                        if s is not None:
                            
                            wavevector =  rotator(ks[i],s)
                            kprime = G + wavevector

                            ang = alpha*s
                            sin = np.sin( -(omega[i]+ang) )
                            cos = np.cos( -(omega[i]+ang) )
                            R = np.array([[cos,-sin,0],[sin,cos,0],[0,0,1]])
                            kprime = R.dot(kprime)
                            khat = kprime/np.linalg.norm(kprime)
                            sd = D / khat[0]

                            yd = khat[1]*sd
                            zd = khat[2]*sd

                            col = ( -(yd/pixsize) + detector.shape[1]//2 ).astype(int)
                            row = ( -(zd/pixsize) + detector.shape[0]//2 ).astype(int)

                            if col>0 and col<detector.shape[1] and row>0 and row<detector.shape[0]:
                                detector[col, row] += 1


kernel = np.ones((5,5))
detector = convolve(detector, kernel, mode='full', method='auto')
plt.imshow(detector, cmap='gray')
plt.title("Hits: "+str(np.sum(detector)/np.sum(kernel) ))
plt.show()
                        
