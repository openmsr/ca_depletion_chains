import xml.etree.cElementTree as et
import pandas as pd
import re

regex = re.compile(r'(\d+|\s+)')
tree=et.parse("chain_endfb71_pwr_volatile.xml")
root=tree.getroot()

FPs = ["Zr","Sr","Xe","Kr","Tc","Ru","Rh","Pd","Ag","Mo","Zn","Ga","Ge","As","Se","Br","Nb","Cd","In","Sn","Sb","Te"]
LANTHANIDES = ["La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"]
target = 'He4'

for dep in root.iter('depletion_chain'):
    root1=et.Element('root')
    root1=dep
    for nuc in root1.iter('nuclide'):
        root2=et.Element('root')
        root2=(nuc)

        if regex.split(nuc.attrib.get('name'))[0] in FPs + LANTHANIDES:

            if int(nuc.attrib.get('reactions')) > 0:
                for reac in root2.iter('reaction'):
                    root3=et.Element('root')
                    root3=reac
                    reac.set('target',target)

            if nuc.attrib.get('decay_modes'):
                for dec in root2.iter('decay'):
                    root4=et.Element('root')
                    root4=dec
                    dec.set('target',target)
tree.write("chain_endfb71_pwr_fp_lanth_removal.xml")
