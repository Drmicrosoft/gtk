
from gi.repository import Gtk

import sys


import pyaudio
import wave
import time
import pygst
pygst.require("0.10")
import gst
import os
import fcntl
import struct
from xml.dom import minidom
import select



import socket
s=socket.socket()
port=11118

#s.connect(("",port))





class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
        system.exit();

    def onButtonPressed(self, b1):
		Gtk.main_quit(*args)
		print ("Omar is hacker")
		system.exit()


x = Gtk.Builder()
x.add_from_file("restaurant1.glade")
print ("Hacked")
p= x.get_objects()



x1 = x.get_object("button1")
x2 = x.get_object("button2")
x3 = x.get_object("show1")

x4 = x.get_object("button3")
x5 = x.get_object("button4")
x6 = x.get_object("show2")

x7 = x.get_object("button5")
x8 = x.get_object("button6")
x9 = x.get_object("show3")

x10 = x.get_object("button7")
x11 = x.get_object("button8")
x12 = x.get_object("show4")

x13 = x.get_object("button9")
x14 = x.get_object("button10")
x15 = x.get_object("show5")

x16 = x.get_object("button11")
x17 = x.get_object("button12")
x18 = x.get_object("show6")

x19 = x.get_object("button13")
x20 = x.get_object("button14")
x21 = x.get_object("show7")

x22 = x.get_object("button15")
x23 = x.get_object("button16")
x24 = x.get_object("show8")

x25 = x.get_object("button17")
x26 = x.get_object("button18")
x27 = x.get_object("show9")

x28 = x.get_object("button19")
x29 = x.get_object("button20")
x30 = x.get_object("show10")

x31 = x.get_object("button21")
x32 = x.get_object("button22")
x33 = x.get_object("show11")

x34 = x.get_object("button23")
x35 = x.get_object("button24")
x36 = x.get_object("show12")

x37 = x.get_object("button25")
x38 = x.get_object("button26")
x39 = x.get_object("show13")

x40 = x.get_object("button27")
x41 = x.get_object("button28")
x42 = x.get_object("show14")

x43 = x.get_object("button29")
x44 = x.get_object("button30")
x45 = x.get_object("show15")

x46 = x.get_object("button31")
x47 = x.get_object("button32")
x48 = x.get_object("show16")

x49 = x.get_object("button33")
x50 = x.get_object("button34")
x51 = x.get_object("show17")

x52 = x.get_object("button35")
x53 = x.get_object("button36")
x54 = x.get_object("show18")

x55 = x.get_object("button37")
x56 = x.get_object("button38")
x57 = x.get_object("show19")

x58 = x.get_object("button39")
x59 = x.get_object("button40")
x60 = x.get_object("show20")

x61 = x.get_object("button41")
x62 = x.get_object("button42")
x63 = x.get_object("show21")

x64 = x.get_object("button43")
x65 = x.get_object("button44")
x66 = x.get_object("show22")

x67 = x.get_object("button45")
x68 = x.get_object("button46")
x69 = x.get_object("show23")

x70 = x.get_object("button47")
x71 = x.get_object("button48")
x72 = x.get_object("show24")

x73 = x.get_object("button49")
x74 = x.get_object("button50")
x75 = x.get_object("show25")


check_out = x.get_object("Check Out")

tv1 = x.get_object("Show")
x.connect_signals(Handler())
print ("Hacked")

window = x.get_object("window1")
print ("Hacked")

window.show_all()
print ("Hacked")

yy=0
def c():
    global yy    # Needed to modify global copy of globvar
    print " yy = " , yy
    yy = 1
    print " yy = " , yy

mat  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print len(mat)

def omar ():
	global mat
	i=0
	while (i<25):
		mat[i]=0
		i=i+1
		
def omar1():
	
	i=0
	while (i<25):
		print "mat [",i,"] = ",mat[i]
		i=i+1
	

def y1 (z) :
	
	global yy
	yy=yy+8
	global mat
	mat[0]=mat[0] + 1;
	

	if mat[0]<0 :
		mat[0]=0
		
	if yy<0 :
		yy=0
	tv1.set_text(str(yy))
	x3.set_text(str(mat[0]))

def y2 (z) :
	
	global yy
	yy=yy-8
	global mat
	mat[0]=mat[0] - 1;
	if mat[0]<0 :
		mat[0]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x3.set_text(str(mat[0]))
	
	
def y3 (z) :
	global yy
	yy=yy+53
	global mat
	mat[1]=mat[1] + 1;
	if mat[1]<0 :
		mat[1]=0
		
	if yy<0 :
		yy=0
	
	tv1.set_text(str(yy))
	x6.set_text(str(mat[1]))
	
		


	
	
def y4 (z) :
	global yy
	yy=yy-53
	global mat
	mat[1]=mat[1] - 1;
	if mat[1]<0 :
		mat[1]=0
		
	if yy<0 :
		yy=0
	
	tv1.set_text(str(yy))
	x6.set_text(str(mat[1]))
	
		


	

	
def y5 (z) :
	global yy
	yy=yy+10
	global mat
	mat[2]=mat[2] + 1;
	
	if mat[2]<0 :
		mat[2]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x9.set_text(str(mat[2]))

def y6 (z) :
	global yy
	yy=yy-10
	global mat
	mat[2]=mat[2] - 1;
	if mat[2]<0 :
		mat[2]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x9.set_text(str(mat[2]))

def y7 (z) :
	global yy
	yy=yy+16
	global mat
	mat[3]=mat[3] + 1;
	if mat[3]<0 :
		mat[3]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x12.set_text(str(mat[3]))

def y8 (z) :
	global yy
	yy=yy-16
	global mat
	mat[3]=mat[3] - 1;
	if mat[3]<0 :
		mat[3]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x12.set_text(str(mat[3]))

def y9 (z) :
	global yy
	yy=yy+45
	global mat
	mat[4]=mat[4] + 1;
	if mat[4]<0 :
		mat[4]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x15.set_text(str(mat[4]))
	


def y10 (z) :
	global yy
	yy=yy-45
	global mat
	mat[4]=mat[4] - 1;
	if mat[4]<0 :
		mat[4]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x15.set_text(str(mat[4]))
	

def y11 (z) :
	global yy
	yy=yy+13
	global mat
	mat[5]=mat[5] + 1;
	if mat[5]<0 :
		mat[5]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))	
	x18.set_text(str(mat[5]))

def y12 (z) :
	global yy
	yy=yy-13
	global mat
	mat[5]=mat[5] - 1;
	if mat[5]<0 :
		mat[5]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))	
	x18.set_text(str(mat[5]))

def y13 (z) :
	global yy
	yy=yy+60
	global mat
	mat[6]=mat[6] + 1;
	if mat[6]<0 :
		mat[6]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x21.set_text(str(mat[6]))

def y14 (z) :
	global yy
	yy=yy-60
	global mat
	mat[6]=mat[6] - 1;
	if mat[6]<0 :
		mat[6]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x21.set_text(str(mat[6]))

def y15 (z) :
	global yy
	yy=yy+55
	global mat
	mat[7]=mat[7] + 1;
	if mat[7]<0 :
		mat[7]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x24.set_text(str(mat[7]))

def y16 (z) :
	global yy
	yy=yy-55
	global mat
	mat[7]=mat[7] - 1;
	if mat[7]<0 :
		mat[7]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x24.set_text(str(mat[7]))

def y17 (z) :
	global yy
	yy=yy+55
	global mat
	mat[8]=mat[8] + 1;
	if mat[8]<0 :
		mat[8]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x27.set_text(str(mat[8]))
	
def y18 (z) :
	global yy
	yy=yy-55
	global mat
	mat[8]=mat[8] - 1;
	if mat[8]<0 :
		mat[8]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x27.set_text(str(mat[8]))

def y19 (z) :
	global yy
	yy=yy+15
	global mat
	mat[9]=mat[9] + 1;
	if mat[9]<0 :
		mat[9]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x30.set_text(str(mat[9]))


def y20 (z) :
	global yy
	yy=yy-15
	global mat
	mat[9]=mat[9] - 1;
	if mat[9]<0 :
		mat[9]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x30.set_text(str(mat[9]))

def y21 (z) :
	global yy
	yy=yy+19
	global mat
	mat[10]=mat[10] + 1;
	if mat[10]<0 :
		mat[10]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x33.set_text(str(mat[10]))

def y22 (z) :
	global yy
	yy=yy-19
	global mat
	mat[10]=mat[10] - 1;
	if mat[10]<0 :
		mat[10]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x33.set_text(str(mat[10]))

def y23 (z) :
	global yy
	yy=yy+45
	global mat
	mat[11]=mat[11] + 1;
	if mat[11]<0 :
		mat[11]=0
		
	if yy<0 :
		yy=0
	
	


	tv1.set_text(str(yy))
	x36.set_text(str(mat[11]))

def y24 (z) :
	global yy
	yy=yy-45
	global mat
	mat[11]=mat[11] - 1;
	if mat[11]<0 :
		mat[11]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x36.set_text(str(mat[11]))

def y25 (z) :
	global yy
	yy=yy+15
	global mat
	mat[12]=mat[12] + 1;
	if mat[12]<0 :
		mat[12]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x39.set_text(str(mat[12]))


def y26 (z) :
	global yy
	yy=yy-15
	global mat
	mat[12]=mat[12] - 1;
	if mat[12]<0 :
		mat[12]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x39.set_text(str(mat[12]))

def y27 (z) :
	global yy
	yy=yy+16
	global mat
	mat[13]=mat[13] + 1;
	if mat[13]<0 :
		mat[13]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x42.set_text(str(mat[13]))


def y28 (z) :
	global yy
	yy=yy-16
	global mat
	mat[13]=mat[13] - 1;
	if mat[13]<0 :
		mat[13]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x42.set_text(str(mat[13]))

def y29 (z) :
	global yy
	yy=yy+55
	global mat
	mat[14]=mat[14] + 1;
	if mat[14]<0 :
		mat[14]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x45.set_text(str(mat[14]))


def y30 (z) :
	global yy
	yy=yy-55
	global mat
	mat[14]=mat[14] - 1;
	if mat[14]<0 :
		mat[14]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x45.set_text(str(mat[14]))

def y31 (z) :
	global yy
	yy=yy+10
	global mat
	mat[15]=mat[15] + 1;
	if mat[15]<0 :
		mat[15]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x48.set_text(str(mat[15]))



def y32 (z) :
	global yy
	yy=yy-10
	global mat
	mat[15]=mat[15] - 1;
	if mat[15]<0 :
		mat[15]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x48.set_text(str(mat[15]))


def y33 (z) :
	global yy
	yy=yy+83
	global mat
	mat[16]=mat[16] + 1;
	if mat[16]<0 :
		mat[16]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x51.set_text(str(mat[16]))



def y34 (z) :
	global yy
	yy=yy-83
	global mat
	mat[16]=mat[16] - 1;
	if mat[16]<0 :
		mat[16]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x51.set_text(str(mat[16]))


def y35 (z) :
	global yy
	
	yy=yy+15
	global mat
	mat[17]=mat[17] + 1;
	if mat[17]<0 :
		mat[17]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x54.set_text(str(mat[17]))



def y36 (z) :
	global yy
	yy=yy-15
	global mat
	mat[17]=mat[17] - 1;
	if mat[17]<0 :
		mat[17]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x54.set_text(str(mat[17]))


def y37 (z) :
	global yy
	yy=yy+18
	global mat
	mat[18]=mat[18] + 1;
	if mat[18]<0 :
		mat[18]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x57.set_text(str(mat[18]))



def y38 (z) :
	global yy
	yy=yy-18
	global mat
	mat[18]=mat[18] - 1;
	if mat[18]<0 :
		mat[18]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x57.set_text(str(mat[18]))

def y39 (z) :
	global yy
	yy=yy+55
	global mat
	mat[19]=mat[19] + 1;
	if mat[19]<0 :
		mat[19]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x60.set_text(str(mat[19]))



def y40 (z) :
	global yy
	yy=yy-55
	global mat
	mat[19]=mat[19] - 1;
	if mat[19]<0 :
		mat[19]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x60.set_text(str(mat[19]))


def y41 (z) :
	global yy
	yy=yy+50
	global mat
	mat[20]=mat[20] + 1;
	if mat[20]<0 :
		mat[20]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x63.set_text(str(mat[20]))


def y42 (z) :
	global yy
	yy=yy-50
	global mat
	mat[20]=mat[20] - 1;
	if mat[20]<0 :
		mat[20]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x63.set_text(str(mat[20]))

def y43 (z) :
	global yy
	yy=yy+83
	global mat
	mat[21]=mat[21] + 1;
	if mat[21]<0 :
		mat[21]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x66.set_text(str(mat[21]))



def y44 (z) :
	global yy
	yy=yy-83
	global mat
	mat[21]=mat[21] - 1;
	if mat[21]<0 :
		mat[21]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x66.set_text(str(mat[21]))


def y45 (z) :
	global yy
	yy=yy+10
	global mat
	mat[22]=mat[22] + 1;
	if mat[22]<0 :
		mat[22]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	
	x69.set_text(str(mat[22]))


def y46 (z) :
	global yy
	yy=yy-10
	global mat
	
	mat[22]=mat[22] - 1;
	if mat[22]<0 :
		mat[22]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	
	x69.set_text(str(mat[22]))

def y47 (z) :
	global yy
	yy=yy+22
	global mat
	mat[23]=mat[23] + 1;
	if mat[23]<0 :
		mat[23]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x72.set_text(str(mat[23]))


def y48 (z) :
	global yy
	yy=yy-22
	global mat
	mat[23]=mat[23] - 1;
	if mat[23]<0 :
		mat[23]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x72.set_text(str(mat[23]))


def y49 (z) :
	global yy
	yy=yy+40
	global mat
	mat[24]=mat[24] + 1;
	if mat[24]<0 :
		mat[24]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x75.set_text(str(mat[24]))



def y50 (z) :
	global yy
	yy=yy-40
	global mat
	mat[24]=mat[24] - 1;
	if mat[24]<0 :
		mat[24]=0
		
	if yy<0 :
		yy=0
	


	tv1.set_text(str(yy))
	x75.set_text(str(mat[24]))



#rise.connect("clicked", Gtk.main_quit)
c()
x1.connect("clicked", y1)
x2.connect("clicked", y2)

x4.connect("clicked", y3)
x5.connect("clicked", y4)

x7.connect("clicked", y5)
x8.connect("clicked", y6)

x10.connect("clicked", y7)
x11.connect("clicked", y8)

x13.connect("clicked", y9)
x14.connect("clicked", y10)

x16.connect("clicked", y11)
x17.connect("clicked", y12)

x19.connect("clicked", y13)
x20.connect("clicked", y14)

x22.connect("clicked", y15)
x23.connect("clicked", y16)

x25.connect("clicked", y17)
x26.connect("clicked", y18)

x28.connect("clicked", y19)
x29.connect("clicked", y20)

x31.connect("clicked", y21)
x32.connect("clicked", y22)

x34.connect("clicked", y23)
x35.connect("clicked", y24)

x37.connect("clicked", y25)
x38.connect("clicked", y26)

x40.connect("clicked", y27)
x41.connect("clicked", y28)

x43.connect("clicked", y29)
x44.connect("clicked", y30)

x46.connect("clicked", y31)
x47.connect("clicked", y32)

x49.connect("clicked", y33)
x50.connect("clicked", y34)

x52.connect("clicked", y35)
x53.connect("clicked", y36)

x55.connect("clicked", y37)
x56.connect("clicked", y38)

x58.connect("clicked", y39)
x59.connect("clicked", y40)

x61.connect("clicked", y41)
x62.connect("clicked", y42)

x64.connect("clicked", y43)
x65.connect("clicked", y44)

x67.connect("clicked", y45)
x68.connect("clicked", y46)

x70.connect("clicked", y47)
x71.connect("clicked", y48)

x73.connect("clicked", y49)
x74.connect("clicked", y50)


def checkout (z):
		omar1()
	
		print "first"
		mat[50]=yy
		#s.send (str(mat))
		
		
		
	
	


check_out.connect("clicked", checkout)

omar1()
omar()
omar1()


Gtk.main()

