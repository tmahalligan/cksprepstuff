import subprocess, time

for i in range(2):
  subprocess.run(['multipass', 'launch', '-c' '2', '-m' '4G', '-d' '10G', '-n', f"server{i}" ])  