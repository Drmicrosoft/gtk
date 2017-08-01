
from xml.dom import minidom
xmldoc = minidom.parse('6.xml')
itemlist = xmldoc.getElementsByTagName('x')
itemlist1 = xmldoc.getElementsByTagName('y')
itemlist2 = xmldoc.getElementsByTagName('z')
print(len(itemlist))
print(len(itemlist1))
print(len(itemlist2))
vv=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
while i<10:
	print "Your table number " , itemlist[i].attributes['number'].value  ,"Your table IP " , itemlist[i].attributes['ip'].value  
	i=i+1
i=0
while i<10:
	print "Your table number " , itemlist1[i].attributes['number'].value  ,"Your table Price " , itemlist1[i].attributes['price'].value  
	i=i+1
i=0
while i<50:
	print "number 1 ",i , itemlist2[i].attributes['order'].value  ,"Your table 1 " , itemlist2[i].attributes['t1'].value  
	vv[i]=itemlist2[i].attributes['t1'].value
	i=i+1


print vv
