import os 

proc_files = os.listdir("/proc")

with open("output.txt", "w+") as of:
    for file in proc_files:
        if "info" not in file:
            continue
            
        with open(f"/proc/{file}", "r") as f:
            of.write(f.read())
        