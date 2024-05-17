Python script for preparing surface plots for dual-color reporter-gene experiments
----------------------------------------------------------------------------------

by A.M. 2024 (andreas.moeglich@uni-bayreuth.de)

1. System requirements
- Python 3, tested on several versions from 3.6 - 3.12
- Python library fcsparser (ver. 0.2.8), can be obtained from https://pypi.org/project/fcsparser/

2. Installation instructions
- copy to target directory
- place input data (.fcs files) in the same directory

3. Demo
- run the script (as is): fcs2txt.py
- opens input data files as specified by comma-separated list in Python script
- outputs tab-delimited text file collating all input data in one table

4. Instructions for use
- provide input .fcs files in the same structure as the example file
- specify .fcs filenames within script
- specify name of .txt output file
- optionally, set cutoff values for forward and side scatter signals (fsc and ssc)
- run script from command line or out of IDE

5. Notes
- depending on yor flow cytometer, the data columns in the .fsc file may have different names and may need to be adjusted