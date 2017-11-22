
import sys
from musevel import velocity
from astropy import units as u
from termcolor import colored


lines = {'SII6717':6718.32, 'SII6731':6732.71, 'Ha':6564.61, 'NII6548':6549.84, 'NII6584':6585.23, 'Hb':4862.69, 'OIII5007':5008.24, 'SIII9068':9071.1, 'OI6300':6302.04}

stacked = [6549.84, 6564.61, 6585.23, 6718.32, 6732.71, 6679.996, 6302.04]*u.AA




if len(sys.argv) < 2:
	print colored('Please provide the name and path of the cube, e.g. path_to_cube/cube_name.fits', 'blue')

if len(sys.argv) == 2:
	cube, wavelength, velocity_range, multicore, outfile = str(sys.argv[1]), 'stacked', [-300,300], 3, 'velocity.fits'
	print colored('Line map,velocity range and oufile not provided, using defaults: stacked, [-300,300], wavelength+velocity.fits', 'blue')

elif len(sys.argv) == 3:
	cube, wavelength, velocity_range, multicore, outfile = str(sys.argv[1]), str(sys.argv[2]), [-300,300], 3, 'velocity.fits'
	print colored('Velocity range and outfile not specified, adopting default ([-300,300] km/s, wavelength+velocity.fits)', 'blue')

elif len(sys.argv) == 4:
	cube, wavelength, velocity_range, multicore, outfile = str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4])
	print colored('Outfile not specified, adopting default (wavelength+velocity.fits)', 'blue') 



if wavelength == 'stacked':
	velocity(cube, stacked, velocity_range, multicore, 'stacked_velocity.fits')
else:
	velocity(cube, [wl[1] for wl in lines.items() if wl[0]==wavelength]*u.AA, velocity_range, multicore, str([wl[0] for wl in lines.items() if wl[0]==wavelength])+'_velocity.fits')
