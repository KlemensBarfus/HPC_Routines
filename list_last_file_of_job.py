# lists the last file that was written by each running job
import os
import sys

n_jobs_running = 0
with os.popen('sacct --format="JobID,JobName%30,State"') as pse:
  for line in pse:
    #print(line)
    temp1 = line.split()
    jobname = temp1[1]
    if "wrf_" in jobname:
      if(temp1[2] == "RUNNING"):
        n_jobs_running = n_jobs_running + 1
        date_str = jobname.split("_")[1]                                                    # the date is part of the jobname
        print(temp1[0])
        scratch_dir = "/scratch/ws/0/barfus-WRF3.8.1/WRF3.8.1/WRFV3/test/em_real/"+date_str # this is the directory to check for the last written file
        os.system("ls -Artls "+scratch_dir+"/wrf_d* | tail -n 1")                           # files to check start with "wrf_d"
        #print(line)
print(n_jobs_running, " jobs running")

#os.system("sacct | ./list_last_file_of_job.py")
#data = sys.stdin.read()
#print("testtest")
#print(data)
