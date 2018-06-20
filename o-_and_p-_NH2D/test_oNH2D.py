import pyspeckit
from pyspeckit.spectrum.models import nh2d
import numpy as np

import astropy.units as u

cube = pyspeckit.Spectrum('h-mm1_onh2d.fits')
rms=0.09
cube.error[:] = rms
cube.xarr.refX = 85926.27e6*u.Hz
cube.xarr.velocity_convention = 'radio'
cube.xarr.convert_to_unit('km/s')
F=False
T=True
import matplotlib.pyplot as plt
plt.ion()
cube.Registry.add_fitter('nh2d_vtau', pyspeckit.models.nh2d.nh2d_vtau_fitter,4)
cube.specfit(fittype='nh2d_vtau', guesses=[3.94, 0.1, 0, 0.1], 
    verbose_level=4, signal_cut=1.5, limitedmax=[F,T,T,T], limitedmin=[T,T,T,T], 
    minpars=[0, 0, -1, 0.05], maxpars=[30.,50.,1,0.5], fixed=[F,F,F,F])
cube.plotter(errstyle='fill')
cube.specfit.plot_fit()
