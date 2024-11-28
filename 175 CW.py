from matplotlib import pyplot as plt
import psutil as p

names= []
cp= []
count= 0

for prname in p.process_iter():
    count= count+1 
    if count <= 10:
        outputname= prname.name()
        outputpercentage= p.cpu_percent()
        print("Application Name  :- " + str(outputname) + "\n CPU Usage :- " +str(outputpercentage))
        
        names.append(outputname)
        cp.append(outputpercentage)
        
plt.figure(figsize=(13,8))
plt.xlabel("Application Names")
plt.ylabel("CPU Usage")
plt.bar(names,cp,width=0.6,color=("orange", "grey", "green"))
plt.show()