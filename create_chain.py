"""
******************************************************************************
  Script used to generate a depletion chain
******************************************************************************
"""

#******************************************************************************
# PACKAGES
#******************************************************************************

import openmc
import openmc.deplete
import os
import glob
from datetime import datetime

#******************************************************************************
# FUNCTIONS
#******************************************************************************

#- Function for printing the date
def print_time(message):
    print()
    print(message+str(datetime.now()))

#******************************************************************************
# GENERATION OF DEPLETION CHAIN
#******************************************************************************

print_time('===> Running started on ')

#- Load ENDF sub-libraies: decay, fission product yield & neutrons
decay_files = glob.glob('ENDF-B-VIII.0_decay/*endf')
fpy_files = glob.glob('ENDF-B-VIII.0_nfy/*endf')
neutron_files = glob.glob('ENDF-B-VIII.0_neutrons/*endf')

#- Generate depletion chain
chain = openmc.deplete.Chain.from_endf(decay_files,fpy_files,neutron_files,reactions=('(n,2n)', '(n,3n)', '(n,4n)', '(n,gamma)', '(n,p)', '(n,a)', '(n,t)','(n,na)'),progress=True)
chain.export_to_xml('ENDF-B-VIII.0_chain_msr.xml')

print_time('===> Processing completed on ')
print()
