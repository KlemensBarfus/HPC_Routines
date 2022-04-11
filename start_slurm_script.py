def get_job_id_from_sbatch_output(direct_output):
  temp_str = direct_output.decode('UTF-8')
  temp_str = temp_str.rsplit()
  job_id = int(temp_str[3])
  return job_id

def start_slurm_script(scriptname):
  # starts slurm script with scriptname
  # returns the job_id
  # input:
  # scriptname: scriptname [string], remember to be in the correct path before starting !
  # output:
  # job_id [integer]
  # written by K. Barfus, 2/2022
  import subprocess
  sys_cmd = "sbatch "+scriptname
  direct_output = subprocess.check_output(sys_cmd, shell=True)
  # b'Submitted batch job 23005933\n'                                                                                                                                                                       
  job_id = get_job_id_from_sbatch_output(direct_output)
  return job_id
