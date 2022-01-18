def get_job_numbers(state='all'):
  import subprocess
  if(state == "all"):
    sys_cmd = "sacct"
  else:
    sys_cmd = "sacct --state="+state
  direct_output = subprocess.check_output(sys_cmd, shell=True)
  temp_str = direct_output.decode('UTF-8')
  temp_str2 = temp_str.split("\n")
  job_numbers = []
  for i in range(0, len(temp_str2)):
    if(i >= 2):
      if(len(temp_str2[i].strip()) > 0): # there is an empty line at the end!
        t2 = temp_str2[i].split()
        if("." not in t2[0]):
          job_numbers.append(int(t2[0]))
  return job_numbers

def get_job_names(job_numbers):
  import subprocess
  job_names = []
  for job_number in job_numbers:
    sys_cmd = "sacct -j "+str(job_number)+" --format=Jobname%30"
    direct_output = subprocess.check_output(sys_cmd, shell=True)
    temp_str = direct_output.decode('UTF-8')
    temp_str2 = temp_str.split("\n")
    job_name = temp_str2[2].strip()
    job_names.append(job_name)
  return(job_names)
  # sacct -j jobid --format=User,JobID,Jobname%30,partition,state,time,start,end,elapsed,MaxRss,MaxVMSize,nnodes,ncpus,nodelist

def get_job_start_times(job_numbers):
  import subprocess
  import datetime
  job_start_times = []
  for job_number in job_numbers:
    sys_cmd = "sacct -j "+str(job_number)+" --format=start"
    direct_output = subprocess.check_output(sys_cmd, shell=True)
    temp_str = direct_output.decode('UTF-8')
    temp_str2 = temp_str.split("\n")
    temp_str3 = temp_str2[2].strip()
    job_start_times.append(temp_str3)
  return(job_start_times)
  # sacct -j jobid --format=User,JobID,Jobname%30,partition,state,time,start,end,elapsed,MaxRss,MaxVMSize,nnodes,ncpus,nodelist

job_numbers = get_job_numbers(state="running")
job_names = get_job_names(job_numbers)
start_times = get_job_start_times(job_numbers) 
for i in range(0, len(job_numbers)):
  print(str(job_numbers[i])+" "+job_names[i]+" "+start_times[i])

