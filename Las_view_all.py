import numpy as np
import matplotlib.pyplot as plt
from las import LASReader

def plotAllLas(Laslocation):
    sample = LASReader(Laslocation, null_subs=np.nan)
    #ax.set_xscale('log') A log scale will be used only for resistivity.
    lognames = sample.curves.names
    totalname = len(lognames)
    log = 1
    name = 0
    for name in range(totalname):
		if(lognames[name] != 'DEPT'):
			if(log == 1):
				ax1 = plt.subplot(1,totalname-1,log)
				plt.plot(sample.data[lognames[name]], sample.data['DEPT'])
				plt.gca().invert_yaxis()
				ax1.set_title(lognames[name])
			else:
				 ax=plt.subplot(1, totalname-1, log, sharey = ax1)
				 plt.plot(sample.data[lognames[name]], sample.data['DEPT'])
				 plt.gca().invert_yaxis()
				 ax.set_title(lognames[name])

			log += 1
    plt.show()

if __name__ == "__main__":
    #Laslocation="/home/karl/open_data/rmotc/DataSets/Well Log/CD Files/LAS_log_files/Deeper_LAS_files/49025228330000_281742.LAS"
     
	plotAllLas("49025108700000_283715.LAS")

