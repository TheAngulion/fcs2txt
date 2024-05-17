#!/usr/bin/python

'''
- reads FACS data in FCS format and exports to text
- written by the incredible A.M.
'''


#

import fcsparser as facs
import numpy as np

# provide comma-separated list of fcs filenames
filenames= '06162023_pAurora2_60_dark_1.fcs,06162023_pAurora2_60_light_1.fcs,06162023_pCDF_dark_1.fcs'.split(',')

# name of output file
txtfname = '06162023_pAurora2_60_1.txt'

# cutoff values for FACS data
ssc_cutoff = 10
fsc_cutoff = 2

# normalize FACS data?
normed = 1

#
export = np.array([])
# read FCS source file
for index, currfile in enumerate(filenames):
  meta, data = facs.parse(currfile, reformat_meta=True)

  # now filter the data for fsc and ssc cutoffs
  monster = data.loc[data['FSC-AREA'] >= fsc_cutoff]
  monster1 = monster.loc[monster['FL2-AREA'] > 0]
  monster2 = monster1.loc[monster1['SSC-AREA'] >= ssc_cutoff]

  # retrieve the data columns we want to evaluate
  fsc_a = monster2['FSC-AREA']
  ssc_a = monster2['SSC-AREA']
  fl2_a = monster2['FL2-AREA']

  # prepare the current data set
  log_tex = np.log10(fl2_a.tolist())
  log_tex = [i for i in log_tex if not np.isnan(i)]
  bins = np.linspace(0, 6, 121)
  use_n,use_bins = np.histogram(log_tex, bins, normed=normed)
  bincenter=[(use_bins[i] + use_bins[i + 1]) / 2 for i in range(len(bins) - 1)]

  # store data for export
  if(len(export)):
    export = np.vstack((export, bincenter))
    export = np.vstack((export, use_n))
  else:
    export = np.array(bincenter)
    export = np.vstack((export, use_n))

# export data
np.savetxt(txtfname, export.transpose(), header='data sets\n' + ' % '.join(filenames) + ' %', comments='')