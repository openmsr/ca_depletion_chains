# MSR depletion chain
- `ENDF-B-VII.1_chain_msr.xml`
- `ENDF-B-VIII.0_chain_msr.xml`

ENDF-B Nuclear reaction, Neutron Induced Fission Product Yields and Decay Reaction libraries downloaded from :point_right: [nndc](https://www.nndc.bnl.gov/).

The xml files are generated using `create_chain.py` script, including `'(n,2n)', '(n,3n)', '(n,4n)', '(n,gamma)', '(n,p)', '(n,a)', '(n,t)','(n,na)'` nuclear reactions.

# Modified depletion chains  
The following chains are retrieved from the OpenMC official depletion data library :point_right: [Openmc official data library](https://openmc.org/official-data-libraries/) and modified as stated below:
- ``chain_endfb71_pwr.xml``: added (n,t) reaction of Li6  
- ``chain_endfb71_pwr_volatile.xml``: Only Xe and Kr set to decay to He4
- ``chain_endfb71_pwr_fp_removal.xml``: All fp set to decay to He4
- ``chain_endfb71_pwr_fp_lanth_removal.xml``: All fp and lanthanides set to decay to He4

The script ``modify_xml.py`` can be used to easly modify the ``xml`` depletion chain files.
