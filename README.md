# Depletion chains 
Depletion chains repository for OpenMC depletion simulations. 
The following chains are retrieved from the OpenMC official depletion data library and modified as stated below:
- ``chain_endfb71_pwr.xml``: added (n,t) reaction of Li6  
- ``chain_endfb71_pwr_volatile.xml``: Only Xe and Kr set to decay to He4
- ``chain_endfb71_pwr_fp_removal.xml``: All fp set to decay to He4
- ``chain_endfb71_pwr_fp_lanth_removal.xml``: All fp and lanthanides set to decay to He4

The script ``modify_xml.py`` can be used to easly modify the ``xml`` depletion chain files. 


