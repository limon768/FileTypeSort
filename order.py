import os

indir = "in/"
outdir="out/"

files=set()
for file in os.listdir(indir): 
    if "." in file: 
        files.add(file)

for e in [e.split(".")[1] for e in files]:
    if not os.path.exists(outdir+"/"+e): os.mkdir(outdir+"/"+e)

for f in files:
    os.rename(indir+f, outdir + str(f.split(".")[1])+ "/" + f)