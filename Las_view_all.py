import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from las import LASReader

def plotAllLas(Laslocation,Logname):
	
	
    sample = LASReader(Laslocation, null_subs=np.nan)
    #ax.set_xscale('log') A log scale will be used only for resistivity.
    lognames = sample.curves.names
    totalname = len(lognames)
    plt.subplots(nrows=1, ncols=totalname-1, sharey=True);
    log = 1
    #ax = fig.add_subplot(1,1,1)
    #ax.plot(sample.data[Logname], sample.data['DEPT'])
    
    sample.curves.display()
    name = 0
    for name in range(totalname):
		if(lognames[name] != 'DEPT'):
			if(log == 1):
				print lognames[name]
				print log
				ax = plt.subplot(1,totalname-1,log)
				plt.plot(sample.data[lognames[name]], sample.data['DEPT'])
			else:
				print log
				print lognames[name]
                #ax = fig.add_subplot(totalname, 1, log, sharex = ax)
				plt.subplot(1, totalname-1, log)
		        plt.plot(sample.data[lognames[name]], sample.data['DEPT'])
		        
			log += 1
			#ax.invert_yaxis()
    		#ax.set_title(lognames[name])
			#plt.title(logname[name])
    		#ax.set_ylabel('Depth (feet)')
    pyplot.show()
