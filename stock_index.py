import matplotlib.pyplot as plt
import csv
import matplotlib.animation as animation

plt.switch_backend("Qt4Agg")

def reading_csv(data):
	with open(data) as csv_file:
		index=csv.reader(csv_file,delimiter=",")
		l=0
		dates=[]
		index_open=[]
		for values in index:
			if l!=0:
				dates.append(values[0])
				if values[1]!="null":
					index_open.append(values[1])
			l=l+1
		print(len(index_open))
	return(dates,index_open)

def init():
	ax1.set_xlim(0,5500)
	ax1.set_ylim(0,10000)
	ax1.set_xlabel("From 2000 to 2020")
	ax1.set_ylabel("Index Levels of NASDAQ")
	ax1.legend()
	ax2.set_xlim(0,5500)
	ax2.set_ylim(0,45000)
	ax2.set_xlabel("From 2000 to 2020 ")
	ax2.set_ylabel("Index Levels of SENSEX")
	ax2.legend()
	ax3.set_xlim(0,5500)
	ax3.set_ylim(0,5000)
	ax3.set_xlabel("From 2000 to 2020")
	ax3.set_ylabel("Index Levels of KOSPI")
	ax3.legend()
	ax4.set_xlim(0,5500)
	ax4.set_ylim(0,7500)
	ax4.set_xlabel("From 2000 to 2020")
	ax4.set_ylabel("Index Levels of SHCOMP")
	ax4.legend()
	line=[line1,line2,line3,line4]
	return line

def animate(i):
	xdata.append(i)
	ydata.append(float(america[i]))
	#print(xdata,ydata)
	line1.set_data(xdata,ydata)
	ind_xdata.append(i)
	ind_ydata.append(float(india[i]))
	line2.set_data(ind_xdata,ind_ydata)
	kor_xdata.append(i)
	kor_ydata.append(float(korea[i]))
	line3.set_data(kor_xdata,kor_ydata)
	chi_xdata.append(i)
	chi_ydata.append(float(china[i]))
	line4.set_data(chi_xdata,chi_ydata)
	line=[line1,line2,line3,line4]
	return line

fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
xdata=[]
ydata=[]
line1, =ax1.plot([],[],"y")
ind_xdata=[]
ind_ydata=[]
line2, =ax2.plot([],[],"b")
line2.set_label("India")
line1.set_label("America")
kor_xdata=[]
kor_ydata=[]
line3, =ax3.plot([],[],"r")
line3.set_label("South Korea")
chi_xdata=[]
chi_ydata=[]
line4, =ax4.plot([],[],"g")
line4.set_label("China")
	
date,america=reading_csv("america.csv")
date,india=reading_csv("india.csv")
date,korea=reading_csv("korea.csv")
date,china=reading_csv("china.csv")
ani=animation.FuncAnimation(fig,animate,frames=4990,init_func=init,interval=1,blit=True)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=100, metadata=dict(artist='Shisui1729'))
figM = plt.get_current_fig_manager()
figM.window.showMaximized()
ani.save("stock2.mp4",writer=writer)
plt.legend()
plt.show()

	
