import subprocess, time

for i in range(3):
  subprocess.Popen(['multipass', 'delete', '--all', '-p' ])  
