# Omori Law Calculator

k=20
p=1
c = 30.0/3600/24

#print (c)

t = 0 
while t <= 40:
	n = k / (c + t) ** p
	print(t,n)
	t = t + .5

#Transfer this file to make a plot "python3 omori.py >! omori.xy"
#Check number of lines cat omori.xy | wc -l
#plot the file using GMT psxy omori.xy -R0/40/0/40 -JX5 -Ba10f1 >! omori.ps
#view the graphical output gv omori.ps &
# conclusion from graph : The rate of earthquakes decays very rapidly over the first few days and then much more gradually after a week.
#to view a specific line python3 omori.py | sed -n 'line #'p
