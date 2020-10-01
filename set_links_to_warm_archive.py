# sets soft links from scratch to warm_archive
# written by K.Barfus, IHM TU Dresden, 11/2019
import os 
from os import listdir
from os.path import isfile
import re
import sys

def function1(path, path_to_link, path_linking):
  path_here = path.replace(path_to_link, path_linking) 
  cmd_str = "mkdir "+path_here
  print(cmd_str)
  os.system(cmd_str)
  list_temp = listdir(path)
  n_list_temp = len(list_temp)
  for i in range(0, n_list_temp):
    if(isfile(path+list_temp[i]) == True):
      cmd_str = "ln -sf "+path+list_temp[i]+" "+path_here+list_temp[i]
      print(cmd_str)
      os.system(cmd_str)
    else:
      path = path + list_temp[i]+"/"
      print("going into "+path)
      path = function1(path, path_to_link, path_linking)
  index_temp = [m.start() for m in re.finditer('/', path)]    
  path_return = path[0:index_temp[len(index_temp)-2]+1]    
  return path_return    
 

path_to_link = sys.argv[1] # e.g. "/warm_archive/ws/barfus-WRF3.8.1/"
path_linking = sys.argv[2] # e.g. "/scratch/ws/barfus-WRF3.8.1/" 

path = path_to_link
path_here = path_linking
list_temp = listdir(path)
n_list_temp = len(list_temp)
for i in range(0, n_list_temp):
  if(isfile(path+list_temp[i]) == True):
    cmd_str = "ln -sf "+path+list_temp[i]+" "+path_here+list_temp[i]
    print(cmd_str)
    os.system(cmd_str) 
  else:
    path = path + list_temp[i]+"/"
    print("going into "+path)
    path = function1(path, path_to_link, path_linking)
    
    

  
