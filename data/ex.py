import subprocess

i = 1
while i < 40:
    subprocess.call("python cleanUp_c.py " + str(i), shell=True)
    print str(i)
    i += 1
