#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Aretas
"""

# Accepts vina config file and location of vina as input
import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--vina_config_file',
    help='choose a vina configuration file', required=True)
parser.add_argument('-vina', '--vina_location',
    help='choose the vina directory', default="./bin/vina")
args = parser.parse_args()

m_obj = re.search(r'config_vina_(.*).txt', args.vina_config_file)
if m_obj:
    protein_ligand = m_obj.groups()[0]
    print ("Docking {0} with AutoDock Vina.".format(protein_ligand))

config_dir = os.path.dirname(os.path.abspath(args.vina_config_file))
command1 = args.vina_location + " --config {0} > {1}_vina_out.txt".format(
    args.vina_config_file, os.path.join(config_dir, protein_ligand))
os.system(command1)
