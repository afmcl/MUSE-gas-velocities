# MUSE-gas-velocities: given a MUSE data cube, compute gas velocities on a pixel-by-pixel base. This code is a scripted version of the MUSE examples on http://pyspeckit.readthedocs.io/.


 If you are using this code, please cite http://adsabs.harvard.edu/abs/2015MNRAS.450.1057M for the method, Pyspeckit (http://pyspeckit.readthedocs.io/), and https://zenodo.org/badge/latestdoi/111626913 for this code.

 Gas velocities can be computed for single lines (e.g. H alpha, [SII], [NII], etc), or by stacking several emission lines in a specific wavelength range, achieving better sampling

Examples.

1. Starting from a fully reduced MUSE datacube, make an H alpha velocity map in a range [-300,300] km/s and process the fit on 2 cores

  python musevel_run.py path_to_cube/cube_name.fits Halpha [-300,300] 2


2. Make a [SII] velocity map

  python musevel_run.py path_to_cube/cube_name.fits SII6717 [-300,300] 2


3. Make a stacked map

  python musevel_run.py path_to_cube/cube_name.fits stacked [-300,300] 2




Available lines: SII6717, SII6731, Ha, NII6548, NII6584, Hb, OIII5007, SIII9068, OI6300

The stacked version stacks 7 emission lines in the 6300-67500 Angstrom range ([NII]6548, [NII]6584, H alpha, [SII]6717, [SII]6731, [HeI]6678 and [OI]6300). The assumtion is that all the lines are emitted from the same region.

Please contact me for new line requests!
