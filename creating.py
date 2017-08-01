import io
def omar () :
			
			matrix=["rice","green beans rice","sea food rice","maxican rice","chicken","veal","italian chicken","italian beaf","maxican beaf","green salad","pure caeser","italian salad","crispy chicken salad","sea food salad","hot dog pizza","cheese pizza","anchoive pizza","hawaian pizza","veggie pizza","classic onion soup","sweet corn soup","mashrom soup","cream chicken soup","beaf soup","mashed potato","special fries","corn on the cob","bread","water","strawberry","chocolate milkshake","red bean","grean bean","mango","coffee","tea","ice tea","kiwi","ice coffee","express coffee","apple tea","mango tea","strawperry tea","turky coffee","french coffee","chocolate cake","ice cream","cream caramel","cheese cake","brownie cake"]
			price = [10,52,21,12,66,55,5,5,2,2]

			b = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]


			f = io.StringIO()
			print f
			f = open("6.xml", "w+")
			print f
			
			
			v=input("sdasdasdasd")
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
