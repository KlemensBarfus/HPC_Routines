def set_rsl_output_error_links(home_directory, scratch_directory, n_threads):
  import os
  # sets links from the home directory to the scratch directory to write output and error files there for MPI jobs 
  for i_threads in range(0, n_threads):
    temp_str = "rsl.out."+str(i_threads).zfill(4)
    sys_cmd = "ln -sf "+scratch_directory+temp_str+" "+home_directory
    os.system(sys_cmd)
    temp_str = "rsl.error."+str(i_threads).zfill(4)
    sys_cmd = "ln -sf "+scratch_directory+temp_str+" "+home_directory
    os.system(sys_cmd)
