'''
MUSE gas velocities produces a velocity map for a given MUSE data cube with a Gaussian pixel-by-pixel fitting routine. 
This code is an scripted version of the MUSE examples on http://pyspeckit.readthedocs.io/




Velocities can be computed for the main nebular emission lines, as well as for a stack of lines for better sampling.

Please report requests/bugs/issues to anna.mcleod@canterbury.ac.nz.

Please aknowledge this script if you use it for your publications (see README)!
'''


class MUSEpy:
    def __init__(self):
        self



from astropy import units as u
import numpy as np, spectral_cube, pyspeckit
from astropy.io import fits





def velocity(cube, wavelength, velocity_range, multicore, outfile):

    '''
    
    cube: str
        The cube path and filename, e.g. path_to_cube/cube_filename.fits

    wavelength: str
        The line one wishes to compute the velocity map for, e.g. Ha, SII6717, or stacked for the stacked version. Default is stacked. 
        Available lines are SII6717, SII6731, Ha, NII6548, NII6584, Hb, OIII5007, SIII9068, OI6300.

    velocity_range: array
        The velocity range, e.g. [-200,200]. Default is [-300,300].

    multicore: int
        The number of cores for the parallelization. Default is 3.

    outfile: str
        The name of the output file. Default is wavelength+'_velocity.fits'.

    '''


    cube = spectral_cube.SpectralCube.read(str(cube), hdu=1)
    hd = cube.header
    ## NEED TO IMPLEMENT CONTINUUM SUBTRACTION BASED ON SPECIFIED WAVELENGTH ##
    slabs = [cube.with_spectral_unit(u.km/u.s, 'optical', wl).spectral_slab(velocity_range[0]*u.km/u.s, velocity_range[1]*u.km/u.s)for wl in wavelength]
    newcube_shape = (sum(s.shape[0] for s in slabs),) + slabs[0].shape[1:]
    newcube_spaxis = np.concatenate([s.spectral_axis for s in slabs]).value*u.km/u.s
    sortvect = newcube_spaxis.argsort()
    sortspaxis = newcube_spaxis[sortvect]
    newcube = np.empty(newcube_shape)
    ind = 0
    for ii,slab in enumerate(slabs):
        data = slab.filled_data[:] / slab.sum(axis=0)
        newcube[ind:ind+data.shape[0], :, :] = data
        ind += data.shape[0]
            
    supercube = newcube[sortvect, :, :]
    pxarr = pyspeckit.units.SpectroscopicAxis(sortspaxis.value, unit='km/s')
    print pxarr
    pcube = pyspeckit.Cube(cube=supercube, xarr=pxarr, header=hd)
    pcube.fiteach(fittype='gaussian', guesses=[1/np.sqrt(np.pi), 5, 20.0],errmap=np.ones(supercube.shape[1:])/100., multicore=3)
    ff = fits.PrimaryHDU(data=pcube.parcube[1], header=hd)
    ff.writeto(outfile,clobber=True)