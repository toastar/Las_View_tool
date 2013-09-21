def plotlas(Laslocation,Logname)

	import numpy as np
	from las import LASReader
	sample3 = LASReader(Laslocation, null_subs=np.nan)
	fig = pyplot.figure()
	ax = fig.add_subplot(1,1,1)
	line, ax.plot(sample3.data[Logname], sample3.data['DEPT'])
	"""ax.set_xscale('log')"""
	ax.invert_yaxis()
	show()

