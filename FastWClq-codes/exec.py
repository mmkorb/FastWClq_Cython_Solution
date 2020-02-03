from subprocess import Popen, PIPE
import os
'''
Sample to help developing. Need to save the graph in a file.
'''
#setting paths
path=os.path.abspath(__file__);
path2= os.path.dirname(path);
alg_path=path2+"/fast-wclq"
filepath=path2+"/bio/bio-celegans.dimw"

#executing and geting the output
command01 = alg_path+" "+filepath+" 50 100 1 1000"
p = Popen(command01, shell=True, stdout=PIPE)
p.wait()
print(p.communicate())