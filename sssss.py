import io
port1 = 11114	



import socket

matrix=["rice","green beans rice","sea food rice","maxican rice","chicken","veal","italian chicken","italian beaf","maxican beaf","green salad","pure caeser","italian salad","crispy chicken salad","sea food salad","hot dog pizza","cheese pizza","anchoive pizza","hawaian pizza","veggie pizza","classic onion soup","sweet corn soup","mashrom soup","cream chicken soup","beaf soup","mashed potato","special fries","corn on the cob","bread","water","strawberry","chocolate milkshake","red bean","grean bean","mango","coffee","tea","ice tea","kiwi","ice coffee","express coffee","apple tea","mango tea","strawperry tea","turky coffee","french coffee","chocolate cake","ice cream","cream caramel","cheese cake","brownie cake"]
price = [10,52,21,12,66,55,5,5,2,2]

b = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]



def omar () :
	
	f = io.StringIO()
	print f
	f = open("6.xml", "w+")
	print f

		
	matrix=["rice","green beans rice","sea food rice","maxican rice","chicken","veal","italian chicken","italian beaf","maxican beaf","green salad","pure caeser","italian salad","crispy chicken salad","sea food salad","hot dog pizza","cheese pizza","anchoive pizza","hawaian pizza","veggie pizza","classic onion soup","sweet corn soup","mashrom soup","cream chicken soup","beaf soup","mashed potato","special fries","corn on the cob","bread","water","strawberry","chocolate milkshake","red bean","grean bean","mango","coffee","tea","ice tea","kiwi","ice coffee","express coffee","apple tea","mango tea","strawperry tea","turky coffee","french coffee","chocolate cake","ice cream","cream caramel","cheese cake","brownie cake"]
	price = [10,52,21,12,66,55,5,5,2,2]


	print b[0][1]
	print b[0][0]
	print len(matrix)

	f.write('<data>\n')
	f.write('\t<ip>\n')
	i=0
	while 1 :
		if i <=9 :
			print "{}{}".format("192.168.1.", i)
			f.write('\t\t<x number = "{}" ip = "{}{}" ></x>\n'.format(i+1,"192.168.1.", i))
			print '\t\t<x number = "{}" ip = "{}{}" ></x>\n'.format(i+1,"192.168.1.", i)
			i=i+1;
		else :
			break 
	f.write('\t</ip>\n')
	f.write('\t<table>\n')
	i=1
	while 1 :
		if i <=10 :
			print "{}{}".format(i+2,2)
			f.write('\t\t<y number = "{}" price = "{}"></y>\n'.format(i,price[i-1]))
			i=i+1;
		else :
			break 
	f.write('\t</table>\n')

	f.write('\t<menu>\n')
	i=0
	while 1 :
		if i <=len(matrix)-1 :
			print "{}{}{}{}".format(i+2, i*2,i*3,i+1)
			print "i = " ,i
			
			f.write('\t\t<z order = "{}" t1 = "{}" t2 = "{}" t3 = "{}" t4 = "{}" t5 = "{}" t6 = "{}" t7 = "{}" t8 = "{}" t9 = "{}" t10 = "{}" ></z>\n'.format(matrix[i],b[i][0],b[i][1],b[i][2],b[i][3],b[i][4],b[i][5],b[i][6],b[i][7],b[i][8],b[i][9]))
			print '\t\t<z order = "{}" t1 = "{}" t2 = "{}" t3 = "{}" t4 = "{}" t5 = "{}" t6 = "{}" t7 = "{}" t8 = "{}" t9 = "{}" t10 = "{}" ></z>\n'.format(matrix[i],b[i][0],b[i][1],b[i][2],b[i][3],b[i][4],b[i][5],b[i][6],b[i][7],b[i][8],b[i][9])
			i=i+1;
			
		else :
			break 
	f.write('\t</menu>\n')
	f.write('</data>\n')

	f.close()

	
omar()
print "jjkj"
s=socket.socket()
print "jjkj"
#host = socket.gethostname()

y=[0,0,0,0,0,0,0,0,0,0]

s.bind(("" , port1))
print "jjkj"
s.listen(5)
print "hhhhhhhh"
i=0
y=[0,0,0,0,0,0,0,0,0,0]
y1=1
y2=0
y3=""
y4=0
mat  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print "omar = " ,len(mat)
y5=0

while i < 6 :
	c,addr = s.accept()     # Establish connection with client.
	
	y =c.recv(1024);
	print addr
	print y
	x=input("omar")
	print y
	try :
		while (y2<=300):
			print " y2 = " , y2 , " y[y2] = " , y[y2]
			if y[y2]==',' :
				while y1<y2 :
					print " start "
					y3=y3+(y[y1])
					print " start 2", y[y1]
					y1=y1+1
					print "\n\n omaaar " , y3
					y4=int(y3)
					print "omar " , y4
					

				mat[y5]=y4
				y5=y5+1
				y1=y2+2
				y2=y1
				
					
				
			else:
				y2=y2+1
				print y2
				y3=""

	except :
		print " done "
	
	print mat
	print y5
	x = input("omar")
	print "omar 1"
	print b[0][0]
	print "omar 2"
	print b[1][0]
	print "omar 3"
	print b[0][1]
	i=0
	while i < 50 :
		b[i][0] = mat[i]
		print " b[",i,"][0] = ",b[i][0]
		print " mat[",i,"] = ",mat[i]
		i=i+1
	
	

	
	omar()
	print "hacked"
	
	x=input("omar12")
	
	x=input("sdasd1233")
	print " price = " , mat[50] 
	
	print " Rice  number = ",mat[0]," price = " , mat[0]*8
	x = input("omar")

	x=int(x) 
	print "end"
	if x==1 :
		print "jjkj"
                print "recieve 1"
		y=input("the bill is ")
		c.send(str(y))
	elif x==2 :
		print "hhhhhhh"
                print "recieve 2 "
		y=input("the bill is ")
		c.send(str(y))
		
	elif x==3 :
        	
                print "recieve 3"
		y=input("the bill is ")
		c.send(str(y))
		
        i=i+1
