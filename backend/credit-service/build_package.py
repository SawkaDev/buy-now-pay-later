import os
import shutil
import subprocess

# Run the sdist command
subprocess.run(["python", "setup.py", "sdist", "--formats=gztar", "--dist-dir=../shared"])

# Remove the .egg-info directory
egg_info_dirs = [d for d in os.listdir() if d.endswith('.egg-info')]
for dir in egg_info_dirs:
    shutil.rmtree(dir)
