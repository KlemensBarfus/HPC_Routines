def get_sacct_info():
  import subprocess

  sys_cmd = 'sacct --format="JobID,Jobname%30,state,time,start,end,elapsed"'

  result = subprocess.run([sys_cmd], stdout=subprocess.PIPE, shell='true')
  stdout = result.stdout
  stdout = stdout.decode(encoding='UTF-8')
  stdout = stdout.split("\n")
  keynames = stdout[0].split()
  # second line is '--------------------------------------'                                                                                                                                                 
  all_jobs = []
  for i in range(2, len(stdout)-1):
    vals_str = stdout[i].split()
    all_jobs.append({})
    for j in range(0, len(keynames)):
      all_jobs[i-2].update({keynames[j] : vals_str[j]})
  return all_jobs
