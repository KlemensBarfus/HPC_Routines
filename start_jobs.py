# if you need to start numerous jobs on Taurus again and you can identifiy the slurm script by a search string                                                                                              
# like "run_job_2001*" this script will help you                                                                                                                                                            
# to make use of placeholders like "*" put the search string in "" in the terminal call                                                                                                                     
# call is: python3 start_jobs.py "search_string" 
# written by Klemens Barfus 03/11/2020                                                                                                                                                                      

import os
import glob
import sys

search_string = sys.argv[1]

slurm_scripts = glob.glob(search_string)
for script in  slurm_scripts:
  sys_cmd = "sbatch "+script
  #print(sys_cmd)                                                                                                                                                                                           
  os.system(sys_cmd)
