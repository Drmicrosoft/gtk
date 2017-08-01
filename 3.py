import io
port=11119
ppp=10
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



class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
        system.exit();

    def onButtonPressed(self, b2):
		Gtk.main_quit(*args)
		print ("Omar is hacker")
		system.exit()



import socket
s=socket.socket()


s.connect(("",port))
 


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
	

x = Gtk.Builder()

mat  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

x.add_from_file("restaurant8.glade")
print ("Hacked")
p= x.get_objects()
yy=0

x1 = x.get_object("x1")
x2 = x.get_object("x2")
x3 = x.get_object("x3")
x4 = x.get_object("x4")
x5 = x.get_object("x5")
x6 = x.get_object("x6")
x7 = x.get_object("x7")
x8 = x.get_object("x8")
x9 = x.get_object("x9")
b1 = x.get_object("Check Out1")
Show = x.get_object("Show")
Show1 = x.get_object("Show1")
Show2 = x.get_object("Show2")
Show3 = x.get_object("Show3")
Show4 = x.get_object("Show4")
Show5 = x.get_object("Show5")
Show6 = x.get_object("Show6")
Show7 = x.get_object("Show7")
Show8 = x.get_object("Show8")
Show9 = x.get_object("Show9")

ch = x.get_object("Check Out")
ch2 = x.get_object("Check Out2")
ch3 = x.get_object("Check Out3")
ch4 = x.get_object("Check Out4")
ch5 = x.get_object("Check Out5")
ch6 = x.get_object("Check Out6")
ch7 = x.get_object("Check Out7")
ch8 = x.get_object("Check Out8")
ch9 = x.get_object("Check Out9")

window1 = x.get_object("window1")
window10 = x.get_object("window10")
window11 = x.get_object("window11")
window3 = x.get_object("window3")
window4 = x.get_object("window4")
window5 = x.get_object("window5")
window6 = x.get_object("window6")
window7 = x.get_object("window7")
window8 = x.get_object("window8")
window9 = x.get_object("window9")

def price_func () :
	global yy
	Show.set_text(str(yy))
	Show1.set_text(str(yy))
	Show2.set_text(str(yy))
	Show3.set_text(str(yy))
	Show4.set_text(str(yy))
	Show5.set_text(str(yy))
	Show6.set_text(str(yy))
	Show7.set_text(str(yy))
	Show8.set_text(str(yy))
	Show9.set_text(str(yy))




def z1 (z) :
		global yy
		yy=yy+10
		global mat
		mat[0]=mat[0] + 1;
		if mat[0]<0 :
			mat[0]=0
			
		if yy<0 :
			yy=0
		price_func()
		show2.set_text(str(mat[0]))

		
def z2 (z) :
		global yy
		yy=yy-10
		global mat
		mat[0]=mat[0] - 1;
		if mat[0]<0 :
			mat[0]=0
			
		if yy<0 :
			yy=0
		price_func()
		show2.set_text(str(mat[0]))




def z3 (z) :
		global yy
		yy=yy+15
		global mat
		mat[1]=mat[1] + 1;
		if mat[1]<0 :
			mat[1]=0
			
		if yy<0 :
			yy=0
		price_func()
		show7.set_text(str(mat[1]))

		
def z4 (z) :
		global yy
		yy=yy-15
		global mat
		mat[1]=mat[1] - 1;
		if mat[1]<0 :
			mat[1]=0
			
		if yy<0 :
			yy=0
		price_func()
		show7.set_text(str(mat[1]))




def z5 (z) :
		global yy
		yy=yy+15
		global mat
		mat[2]=mat[2] + 1;
		if mat[2]<0 :
			mat[2]=0
			
		if yy<0 :
			yy=0
		price_func()
		show1.set_text(str(mat[2]))

		
def z6 (z) :
		global yy
		yy=yy-15
		global mat
		mat[2]=mat[2] - 1;
		if mat[2]<0 :
			mat[2]=0
			
		if yy<0 :
			yy=0
		price_func()
		show1.set_text(str(mat[2]))




def z7 (z) :
		global yy
		yy=yy+17
		global mat
		mat[3]=mat[3] + 1;
		if mat[3]<0 :
			mat[3]=0
			
		if yy<0 :
			yy=0
		price_func()
		show6.set_text(str(mat[3]))

		
def z8 (z) :
		global yy
		yy=yy-17
		global mat
		mat[3]=mat[3] - 1;
		if mat[3]<0 :
			mat[3]=0
			
		if yy<0 :
			yy=0
		price_func()
		show6.set_text(str(mat[3]))




def z9 (z) :
		global yy
		yy=yy+15
		global mat
		mat[4]=mat[4] + 1;
		if mat[4]<0 :
			mat[4]=0
			
		if yy<0 :
			yy=0
		price_func()
		show5.set_text(str(mat[4]))
		show40.set_text(str(mat[4]))

		
def z10 (z) :
		global yy
		yy=yy-15
		global mat
		mat[4]=mat[4] - 1;
		if mat[4]<0 :
			mat[4]=0
			
		if yy<0 :
			yy=0
		price_func()
		show5.set_text(str(mat[4]))
		show40.set_text(str(mat[4]))




def z11 (z) :
		global yy
		yy=yy+18
		global mat
		mat[5]=mat[5] + 1;
		if mat[5]<0 :
			mat[5]=0
			
		if yy<0 :
			yy=0
		price_func()
		show4.set_text(str(mat[5]))
		show45.set_text(str(mat[5]))

		
def z12 (z) :
		global yy
		yy=yy-18
		global mat
		mat[5]=mat[5] - 1;
		if mat[5]<0 :
			mat[5]=0
			
		if yy<0 :
			yy=0
		price_func()
		show4.set_text(str(mat[5]))
		show45.set_text(str(mat[5]))




def z13 (z) :
		global yy
		yy=yy+35
		global mat
		mat[6]=mat[6] + 1;
		if mat[6]<0 :
			mat[6]=0
			
		if yy<0 :
			yy=0
		price_func()
		show8.set_text(str(mat[6]))

		
def z14 (z) :
		global yy
		yy=yy-35
		global mat
		mat[6]=mat[6] - 1;
		if mat[6]<0 :
			mat[6]=0
			
		if yy<0 :
			yy=0
		price_func()
		show8.set_text(str(mat[6]))




def z15 (z) :
		global yy
		yy=yy+25
		global mat
		mat[7]=mat[7] + 1;
		if mat[7]<0 :
			mat[7]=0
			
		if yy<0 :
			yy=0
		price_func()
		show3.set_text(str(mat[7]))
		show50.set_text(str(mat[7]))

		
def z16 (z) :
		global yy
		yy=yy-25
		global mat
		mat[7]=mat[7] - 1;
		if mat[7]<0 :
			mat[7]=0
			
		if yy<0 :
			yy=0
		price_func()
		show3.set_text(str(mat[7]))
		show50.set_text(str(mat[7]))




def z17 (z) :
		global yy
		yy=yy+25
		global mat
		mat[8]=mat[8] + 1;
		if mat[8]<0 :
			mat[8]=0
			
		if yy<0 :
			yy=0
		price_func()
		show11.set_text(str(mat[8]))

		
def z18 (z) :
		global yy
		yy=yy-25
		global mat
		mat[8]=mat[8] - 1;
		if mat[8]<0 :
			mat[8]=0
			
		if yy<0 :
			yy=0
		price_func()
		show11.set_text(str(mat[8]))




def z19 (z) :
		global yy
		yy=yy+28
		global mat
		mat[9]=mat[9] + 1;
		if mat[9]<0 :
			mat[9]=0
			
		if yy<0 :
			yy=0
		price_func()
		show10.set_text(str(mat[9]))
		show41.set_text(str(mat[9]))

		
def z20 (z) :
		global yy
		yy=yy-28
		global mat
		mat[9]=mat[9] - 1;
		if mat[9]<0 :
			mat[9]=0
			
		if yy<0 :
			yy=0
		price_func()
		show10.set_text(str(mat[9]))
		show41.set_text(str(mat[9]))




def z21 (z) :
		global yy
		yy=yy+30
		global mat
		mat[10]=mat[10] + 1;
		if mat[10]<0 :
			mat[10]=0
			
		if yy<0 :
			yy=0
		price_func()
		show12.set_text(str(mat[10]))

		
def z22 (z) :
		global yy
		yy=yy-30
		global mat
		mat[10]=mat[10] - 1;
		if mat[10]<0 :
			mat[10]=0
			
		if yy<0 :
			yy=0
		price_func()
		show12.set_text(str(mat[10]))




def z23 (z) :
		global yy
		yy=yy+27
		global mat
		mat[11]=mat[11] + 1;
		if mat[11]<0 :
			mat[11]=0
			
		if yy<0 :
			yy=0
		price_func()
		show9.set_text(str(mat[11]))

		
def z24 (z) :
		global yy
		yy=yy-27
		global mat
		mat[11]=mat[11] - 1;
		if mat[11]<0 :
			mat[11]=0
			
		if yy<0 :
			yy=0
		price_func()
		show9.set_text(str(mat[11]))




def z25 (z) :
		global yy
		yy=yy+30
		global mat
		mat[12]=mat[12] + 1;
		if mat[12]<0 :
			mat[12]=0
			
		if yy<0 :
			yy=0
		price_func()
		show15.set_text(str(mat[12]))
		show41.set_text(str(mat[12]))

		
def z26 (z) :
		global yy
		yy=yy-30
		global mat
		mat[12]=mat[12] - 1;
		if mat[12]<0 :
			mat[12]=0
			
		if yy<0 :
			yy=0
		price_func()
		show15.set_text(str(mat[12]))
		show41.set_text(str(mat[12]))




def z27 (z) :
		global yy
		yy=yy+28
		global mat
		mat[13]=mat[13] + 1;
		if mat[13]<0 :
			mat[13]=0
			
		if yy<0 :
			yy=0
		price_func()
		show14.set_text(str(mat[13]))
		show46.set_text(str(mat[13]))

		
def z28 (z) :
		global yy
		yy=yy-28
		global mat
		mat[13]=mat[13] - 1;
		if mat[13]<0 :
			mat[13]=0
			
		if yy<0 :
			yy=0
		price_func()
		show14.set_text(str(mat[13]))
		show46.set_text(str(mat[13]))




def z29 (z) :
		global yy
		yy=yy+25
		global mat
		mat[14]=mat[14] + 1;
		if mat[14]<0 :
			mat[14]=0
			
		if yy<0 :
			yy=0
		price_func()
		show16.set_text(str(mat[14]))
		show51.set_text(str(mat[14]))

		
def z30 (z) :
		global yy
		yy=yy-25
		global mat
		mat[14]=mat[14] - 1;
		if mat[14]<0 :
			mat[14]=0
			
		if yy<0 :
			yy=0
		price_func()
		show16.set_text(str(mat[14]))
		show51.set_text(str(mat[14]))




def z31 (z) :
		global yy
		yy=yy+23
		global mat
		mat[15]=mat[15] + 1;
		if mat[15]<0 :
			mat[15]=0
			
		if yy<0 :
			yy=0
		price_func()
		show13.set_text(str(mat[15]))
		show61.set_text(str(mat[15]))

		
def z32 (z) :
		global yy
		yy=yy-23
		global mat
		mat[15]=mat[15] - 1;
		if mat[15]<0 :
			mat[15]=0
			
		if yy<0 :
			yy=0
		price_func()
		show13.set_text(str(mat[15]))
		show61.set_text(str(mat[15]))




def z33 (z) :
		global yy
		yy=yy+18
		global mat
		mat[16]=mat[16] + 1;
		if mat[16]<0 :
			mat[16]=0
			
		if yy<0 :
			yy=0
		price_func()
		show19.set_text(str(mat[16]))
		show37.set_text(str(mat[16]))

		
def z34 (z) :
		global yy
		yy=yy-18
		global mat
		mat[16]=mat[16] - 1;
		if mat[16]<0 :
			mat[16]=0
			
		if yy<0 :
			yy=0
		price_func()
		show19.set_text(str(mat[16]))
		show37.set_text(str(mat[16]))




def z35 (z) :
		global yy
		yy=yy+20
		global mat
		mat[17]=mat[17] + 1;
		if mat[17]<0 :
			mat[17]=0
			
		if yy<0 :
			yy=0
		price_func()
		show18.set_text(str(mat[17]))
		show42.set_text(str(mat[17]))

		
def z36 (z) :
		global yy
		yy=yy-20
		global mat
		mat[17]=mat[17] - 1;
		if mat[17]<0 :
			mat[17]=0
			
		if yy<0 :
			yy=0
		price_func()
		show18.set_text(str(mat[17]))
		show42.set_text(str(mat[17]))




def z37 (z) :
		global yy
		yy=yy+37
		global mat
		mat[18]=mat[18] + 1;
		if mat[18]<0 :
			mat[18]=0
			
		if yy<0 :
			yy=0
		price_func()
		show20.set_text(str(mat[18]))
		show47.set_text(str(mat[18]))

		
def z38 (z) :
		global yy
		yy=yy-37
		global mat
		mat[18]=mat[18] - 1;
		if mat[18]<0 :
			mat[18]=0
			
		if yy<0 :
			yy=0
		price_func()
		show20.set_text(str(mat[18]))
		show47.set_text(str(mat[18]))




def z39 (z) :
		global yy
		yy=yy+22
		global mat
		mat[19]=mat[19] + 1;
		if mat[19]<0 :
			mat[19]=0
			
		if yy<0 :
			yy=0
		price_func()
		show17.set_text(str(mat[19]))
		show58.set_text(str(mat[19]))

		
def z40 (z) :
		global yy
		yy=yy-22
		global mat
		mat[19]=mat[19] - 1;
		if mat[19]<0 :
			mat[19]=0
			
		if yy<0 :
			yy=0
		price_func()
		show17.set_text(str(mat[19]))
		show58.set_text(str(mat[19]))




def z41 (z) :
		global yy
		yy=yy+25
		global mat
		mat[20]=mat[20] + 1;
		if mat[20]<0 :
			mat[20]=0
			
		if yy<0 :
			yy=0
		price_func()
		show23.set_text(str(mat[20]))
		show38.set_text(str(mat[20]))

		
def z42 (z) :
		global yy
		yy=yy-25
		global mat
		mat[20]=mat[20] - 1;
		if mat[20]<0 :
			mat[20]=0
			
		if yy<0 :
			yy=0
		price_func()
		show23.set_text(str(mat[20]))
		show38.set_text(str(mat[20]))




def z43 (z) :
		global yy
		yy=yy+28
		global mat
		mat[21]=mat[21] + 1;
		if mat[21]<0 :
			mat[21]=0
			
		if yy<0 :
			yy=0
		price_func()
		show22.set_text(str(mat[21]))
		show48.set_text(str(mat[21]))

		
def z44 (z) :
		global yy
		yy=yy-28
		global mat
		mat[21]=mat[21] - 1;
		if mat[21]<0 :
			mat[21]=0
			
		if yy<0 :
			yy=0
		price_func()
		show22.set_text(str(mat[21]))
		show48.set_text(str(mat[21]))




def z45 (z) :
		global yy
		yy=yy+26
		global mat
		mat[22]=mat[22] + 1;
		if mat[22]<0 :
			mat[22]=0
			
		if yy<0 :
			yy=0
		price_func()
		show24.set_text(str(mat[22]))
		show53.set_text(str(mat[22]))

		
def z46 (z) :
		global yy
		yy=yy-26
		global mat
		mat[22]=mat[22] - 1;
		if mat[22]<0 :
			mat[22]=0
			
		if yy<0 :
			yy=0
		price_func()
		
		show24.set_text(str(mat[22]))
		show53.set_text(str(mat[22]))




def z47 (z) :
		global yy
		yy=yy+30
		global mat
		mat[23]=mat[23] + 1;
		if mat[23]<0 :
			mat[23]=0
			
		if yy<0 :
			yy=0
		price_func()
		show21.set_text(str(mat[23]))
		show52.set_text(str(mat[23]))

		
def z48 (z) :
		global yy
		yy=yy-30
		global mat
		mat[23]=mat[23] - 1;
		if mat[23]<0 :
			mat[23]=0
			
		if yy<0 :
			yy=0
		price_func()
		show21.set_text(str(mat[23]))
		show52.set_text(str(mat[23]))




def z49 (z) :
		global yy
		yy=yy+25
		global mat
		mat[24]=mat[24] + 1;
		if mat[24]<0 :
			mat[24]=0
			
		if yy<0 :
			yy=0
		price_func()
		show27.set_text(str(mat[24]))

		
def z50 (z) :
		global yy
		yy=yy-25
		global mat
		mat[24]=mat[24] - 1;
		if mat[24]<0 :
			mat[24]=0
			
		if yy<0 :
			yy=0
		price_func()
		show27.set_text(str(mat[24]))




def z51 (z) :
		global yy
		yy=yy+13
		global mat
		mat[25]=mat[25] + 1;
		if mat[25]<0 :
			mat[25]=0
			
		if yy<0 :
			yy=0
		price_func()
		show26.set_text(str(mat[25]))

		
def z52 (z) :
		global yy
		yy=yy-13
		global mat
		mat[25]=mat[25] - 1;
		if mat[25]<0 :
			mat[25]=0
			
		if yy<0 :
			yy=0
		price_func()
		show26.set_text(str(mat[25]))




def z53 (z) :
		global yy
		yy=yy+12
		global mat
		mat[26]=mat[26] + 1;
		if mat[26]<0 :
			mat[26]=0
			
		if yy<0 :
			yy=0
		price_func()
		show28.set_text(str(mat[26]))

		
def z54 (z) :
		global yy
		yy=yy-12
		global mat
		mat[26]=mat[26] - 1;
		if mat[26]<0 :
			mat[26]=0
			
		if yy<0 :
			yy=0
		price_func()
		show28.set_text(str(mat[26]))




def z55 (z) :
		global yy
		yy=yy+22
		global mat
		mat[27]=mat[27] + 1;
		if mat[27]<0 :
			mat[27]=0
			
		if yy<0 :
			yy=0
		price_func()
		show25.set_text(str(mat[27]))

		
def z56 (z) :
		global yy
		yy=yy-22
		global mat
		mat[27]=mat[27] - 1;
		if mat[27]<0 :
			mat[27]=0
			
		if yy<0 :
			yy=0
		price_func()
		show25.set_text(str(mat[27]))




def z57 (z) :
		global yy
		yy=yy+8
		global mat
		mat[28]=mat[28] + 1;
		if mat[28]<0 :
			mat[28]=0
			
		if yy<0 :
			yy=0
		price_func()
		show31.set_text(str(mat[28]))

		
def z58 (z) :
		global yy
		yy=yy-8
		global mat
		mat[28]=mat[28] - 1;
		if mat[28]<0 :
			mat[28]=0
			
		if yy<0 :
			yy=0
		price_func()
		show31.set_text(str(mat[28]))




def z59 (z) :
		global yy
		yy=yy+6
		global mat
		mat[29]=mat[29] + 1;
		if mat[29]<0 :
			mat[29]=0
			
		if yy<0 :
			yy=0
		price_func()
		show30.set_text(str(mat[29]))

		
def z60 (z) :
		global yy
		yy=yy-6
		global mat
		mat[29]=mat[29] - 1;
		if mat[29]<0 :
			mat[29]=0
			
		if yy<0 :
			yy=0
		price_func()
		show30.set_text(str(mat[29]))




def z61 (z) :
		global yy
		yy=yy+12
		global mat
		mat[30]=mat[30] + 1;
		if mat[30]<0 :
			mat[30]=0
			
		if yy<0 :
			yy=0
		price_func()
		show32.set_text(str(mat[30]))

		
def z62 (z) :
		global yy
		yy=yy-12
		global mat
		mat[30]=mat[30] - 1;
		if mat[30]<0 :
			mat[30]=0
			
		if yy<0 :
			yy=0
		price_func()
		show32.set_text(str(mat[30]))




def z63 (z) :
		global yy
		yy=yy+15
		global mat
		mat[31]=mat[31] + 1;
		if mat[31]<0 :
			mat[31]=0
			
		if yy<0 :
			yy=0
		price_func()
		show29.set_text(str(mat[31]))

		
def z64 (z) :
		global yy
		yy=yy-15
		global mat
		mat[31]=mat[31] - 1;
		if mat[31]<0 :
			mat[31]=0
			
		if yy<0 :
			yy=0
		price_func()
		show29.set_text(str(mat[31]))




def z65 (z) :
		global yy
		yy=yy+7
		global mat
		mat[32]=mat[32] + 1;
		if mat[32]<0 :
			mat[32]=0
			
		if yy<0 :
			yy=0
		price_func()
		show35.set_text(str(mat[32]))

		
def z66 (z) :
		global yy
		yy=yy-7
		global mat
		mat[32]=mat[32] - 1;
		if mat[32]<0 :
			mat[32]=0
			
		if yy<0 :
			yy=0
		price_func()
		show35.set_text(str(mat[32]))




def z67 (z) :
		global yy
		yy=yy+5
		global mat
		mat[33]=mat[33] + 1;
		if mat[33]<0 :
			mat[33]=0
			
		if yy<0 :
			yy=0
		price_func()
		show34.set_text(str(mat[33]))

		
def z68 (z) :
		global yy
		yy=yy-5
		global mat
		mat[33]=mat[33] - 1;
		if mat[33]<0 :
			mat[33]=0
			
		if yy<0 :
			yy=0
		price_func()
		show34.set_text(str(mat[33]))




def z69 (z) :
		global yy
		yy=yy+15
		global mat
		mat[34]=mat[34] + 1;
		if mat[34]<0 :
			mat[34]=0
			
		if yy<0 :
			yy=0
		price_func()
		show36.set_text(str(mat[34]))
		show49.set_text(str(mat[34]))

		
def z70 (z) :
		global yy
		yy=yy-15
		global mat
		mat[34]=mat[34] - 1;
		if mat[34]<0 :
			mat[34]=0
			
		if yy<0 :
			yy=0
		price_func()
		show36.set_text(str(mat[34]))
		show49.set_text(str(mat[34]))




def z71 (z) :
		global yy
		yy=yy+17
		global mat
		mat[35]=mat[35] + 1;
		if mat[35]<0 :
			mat[35]=0
			
		if yy<0 :
			yy=0
		price_func()
		show33.set_text(str(mat[35]))
		show54.set_text(str(mat[35]))

		
def z72 (z) :
		global yy
		yy=yy-17
		global mat
		mat[35]=mat[35] - 1;
		if mat[35]<0 :
			mat[35]=0
			
		if yy<0 :
			yy=0
		price_func()
		show33.set_text(str(mat[35]))
		show54.set_text(str(mat[35]))




def z73 (z) :
		global yy
		yy=yy+11
		global mat
		mat[36]=mat[36] + 1;
		if mat[36]<0 :
			mat[36]=0
			
		if yy<0 :
			yy=0
		price_func()
		show39.set_text(str(mat[36]))

		
def z74 (z) :
		global yy
		yy=yy-11
		global mat
		mat[36]=mat[36] - 1;
		if mat[36]<0 :
			mat[36]=0
			
		if yy<0 :
			yy=0
		price_func()
		show39.set_text(str(mat[36]))




def z75 (z) :
		global yy
		yy=yy+15
		global mat
		mat[37]=mat[37] + 1;
		if mat[37]<0 :
			mat[37]=0
			
		if yy<0 :
			yy=0
		price_func()
		show43.set_text(str(mat[37]))

		
def z76 (z) :
		global yy
		yy=yy-15
		global mat
		mat[37]=mat[37] - 1;
		if mat[37]<0 :
			mat[37]=0
			
		if yy<0 :
			yy=0
		price_func()
		show43.set_text(str(mat[37]))




def z77 (z) :
		global yy
		yy=yy+16
		global mat
		mat[38]=mat[38] + 1;
		if mat[38]<0 :
			mat[38]=0
			
		if yy<0 :
			yy=0
		price_func()
		show44.set_text(str(mat[38]))

		
def z78 (z) :
		global yy
		yy=yy-16
		global mat
		mat[38]=mat[38] - 1;
		if mat[38]<0 :
			mat[38]=0
			
		if yy<0 :
			yy=0
		price_func()
		show44.set_text(str(mat[38]))




def z79 (z) :
		global yy
		yy=yy+12
		global mat
		mat[39]=mat[39] + 1;
		if mat[39]<0 :
			mat[39]=0
			
		if yy<0 :
			yy=0
		price_func()
		show55.set_text(str(mat[39]))

		
def z80 (z) :
		global yy
		yy=yy-12
		global mat
		mat[39]=mat[39] - 1;
		if mat[39]<0 :
			mat[39]=0
			
		if yy<0 :
			yy=0
		price_func()
		show55.set_text(str(mat[39]))




def z81 (z) :
		global yy
		yy=yy+10
		global mat
		mat[40]=mat[40] + 1;
		if mat[40]<0 :
			mat[40]=0
			
		if yy<0 :
			yy=0
		price_func()
		show56.set_text(str(mat[40]))

		
def z82 (z) :
		global yy
		yy=yy-10
		global mat
		mat[40]=mat[40] - 1;
		if mat[40]<0 :
			mat[40]=0
			
		if yy<0 :
			yy=0
		price_func()
		show56.set_text(str(mat[40]))




def z83 (z) :
		global yy
		yy=yy+99
		global mat
		mat[41]=mat[41] + 1;
		if mat[41]<0 :
			mat[41]=0
			
		if yy<0 :
			yy=0
		price_func()
		show57.set_text(str(mat[41]))

		
def z84 (z) :
		global yy
		yy=yy-99
		global mat
		mat[41]=mat[41] - 1;
		if mat[41]<0 :
			mat[41]=0
			
		if yy<0 :
			yy=0
		price_func()
		show57.set_text(str(mat[41]))




def z85 (z) :
		global yy
		yy=yy+100
		global mat
		mat[42]=mat[42] + 1;
		if mat[42]<0 :
			mat[42]=0
			
		if yy<0 :
			yy=0
		price_func()
		show59.set_text(str(mat[42]))

		
def z86 (z) :
		global yy
		yy=yy-100
		global mat
		mat[42]=mat[42] - 1;
		if mat[42]<0 :
			mat[42]=0
			
		if yy<0 :
			yy=0
		price_func()
		show59.set_text(str(mat[42]))




def z87 (z) :
		print "omar"
		global yy
		yy=yy+60
		global mat
		mat[43]=mat[43] + 1;
		if mat[43]<0 :
			mat[43]=0
			
		if yy<0 :
			yy=0
		price_func()
		show60.set_text(str(mat[43]))

		
def z88 (z) :
		print "omar"
		global yy
		yy=yy-60
		global mat
		mat[43]=mat[43] - 1;
		if mat[43]<0 :
			mat[43]=0
			
		if yy<0 :
			yy=0
		price_func()
		show60.set_text(str(mat[43]))

def omar2 (z) :
	global ppp
	print "startx"
	print ppp
	if ppp == 1 :
		com = x1.get_active_text()
		print com
		omar3(com)
	elif ( ppp == 2) :
		com = x2.get_active_text()
		print com
		omar3(com)
	elif ppp == 3 :
		com = x3.get_active_text()
		print com
		omar3(com)
	elif ppp == 4 :
		com = x4.get_active_text()
		print com
		omar3(com)
	elif ppp == 5 :
		com = x5.get_active_text()
		print com
		omar3(com)
	elif ppp == 6 :
		com = x6.get_active_text()
		print com
		omar3(com)
	elif ppp == 7 :
		com = x7.get_active_text()
		print com
		omar3(com)
	elif ppp == 8 :
		com = x8.get_active_text()
		print com
		omar3(com)
	elif ppp == 9 :
		com = x9.get_active_text()
		print com
		omar3(com)
	elif ppp == 10 :
		print "omar"
		omar3("salad")

def omar3 (com) :
	global ppp
	if(com == "salad") :
		b8(1)
		ppp=1
	elif(com == "others") :
		b125(1)
		ppp=9
	elif(com == "recommended") :
		b126(1)
		ppp=10
	elif(com == "soup") :
		b127(1)
		ppp=2
	elif(com == "pasta") :
		b128(1)
		ppp=3
	elif(com == "pizza") :
		b129(1)
		ppp=4
	elif(com == "rice") :
		b130(1)
		ppp=5
	elif(com == "meat") :
		b131(1)
		ppp=6
	elif(com == "dessert") :
		b132(1)
		ppp=7
	elif(com == "drinks") :
		b133(1)
		ppp=8


def b8 (z) :
		
			window1.show_all()
			window10.hide()
			window11.hide()
			window3.hide()
			window4.hide()
			window5.hide()
			window6.hide()
			window7.hide()
			window8.hide()
			window9.hide()

		



def b125 (z) :
		
			window10.show_all()
			window11.hide()
			window3.hide()
			window4.hide()
			window5.hide()
			window6.hide()
			window7.hide()
			window8.hide()
			window9.hide()
			window1.hide()

		



def b126 (z) :
		
			window11.show_all()
			window3.hide()
			window4.hide()
			window5.hide()
			window6.hide()
			window7.hide()
			window8.hide()
			window9.hide()
			window1.hide()
			window10.hide()

		



def b127 (z) :
		
			window3.show_all()
			window4.hide()
			window5.hide()
			window6.hide()
			window7.hide()
			window8.hide()
			window9.hide()
			window1.hide()
			window10.hide()
			window11.hide()

		



def b128 (z) :
		
			window4.show_all()
			window5.hide()
			window6.hide()
			window7.hide()
			window8.hide()
			window9.hide()
			window1.hide()
			window10.hide()
			window11.hide()
			window3.hide()

		



def b129 (z) :
		
			window5.show_all()
			window6.hide()
			window7.hide()
			window8.hide()
			window9.hide()
			window1.hide()
			window10.hide()
			window11.hide()
			window3.hide()
			window4.hide()

		



def b130 (z) :
		
			window6.show_all()
			window7.hide()
			window8.hide()
			window9.hide()
			window1.hide()
			window10.hide()
			window11.hide()
			window3.hide()
			window4.hide()
			window5.hide()

		



def b131 (z) :
		
			window7.show_all()
			window8.hide()
			window9.hide()
			window1.hide()
			window10.hide()
			window11.hide()
			window3.hide()
			window4.hide()
			window5.hide()
			window6.hide()

		



def b132 (z) :
		
			window8.show_all()
			window9.hide()
			window1.hide()
			window10.hide()
			window11.hide()
			window3.hide()
			window4.hide()
			window5.hide()
			window6.hide()
			window7.hide()

		



def b133 (z) :
		
			window9.show_all()
			window1.hide()
			window10.hide()
			window11.hide()
			window3.hide()
			window4.hide()
			window5.hide()
			window6.hide()
			window7.hide()
			window8.hide()

		




button8 = x.get_object("button8")
button125 = x.get_object("button125")
button126 = x.get_object("button126")
button127 = x.get_object("button127")
button128 = x.get_object("button128")
button129 = x.get_object("button129")
button130 = x.get_object("button130")
button131 = x.get_object("button131")
button132 = x.get_object("button132")
button133 = x.get_object("button133")

button8.connect("clicked", omar2)
button125.connect("clicked", omar2)
button126.connect("clicked", omar2)
button127.connect("clicked", omar2)
button128.connect("clicked", omar2)
button129.connect("clicked", omar2)
button130.connect("clicked", omar2)
button131.connect("clicked", omar2)
button132.connect("clicked", omar2)
button133.connect("clicked", omar2)


button1 = x.get_object("button1")
button2 = x.get_object("button2")
button3 = x.get_object("button3")
button4 = x.get_object("button4")
button5 = x.get_object("button5")
button6 = x.get_object("button6")
button7 = x.get_object("button7")
button8 = x.get_object("button8")
button9 = x.get_object("button9")
button10 = x.get_object("button10")
button11 = x.get_object("button11")
button12 = x.get_object("button12")
button13 = x.get_object("button13")
button14 = x.get_object("button14")
button15 = x.get_object("button15")
button16 = x.get_object("button16")
button17 = x.get_object("button17")
button18 = x.get_object("button18")
button19 = x.get_object("button19")
button20 = x.get_object("button20")
button21 = x.get_object("button21")
button22 = x.get_object("button22")
button23 = x.get_object("button23")
button24 = x.get_object("button24")
button25 = x.get_object("button25")
button26 = x.get_object("button26")
button27 = x.get_object("button27")
button28 = x.get_object("button28")
button29 = x.get_object("button29")
button30 = x.get_object("button30")
button31 = x.get_object("button31")
button32 = x.get_object("button32")
button33 = x.get_object("button33")
button34 = x.get_object("button34")
button35 = x.get_object("button35")
button36 = x.get_object("button36")
button37 = x.get_object("button37")
button38 = x.get_object("button38")
button39 = x.get_object("button39")
button40 = x.get_object("button40")
button41 = x.get_object("button41")
button42 = x.get_object("button42")
button43 = x.get_object("button43")
button44 = x.get_object("button44")
button45 = x.get_object("button45")
button46 = x.get_object("button46")
button47 = x.get_object("button47")
button48 = x.get_object("button48")
button49 = x.get_object("button49")
button50 = x.get_object("button50")
button51 = x.get_object("button51")
button52 = x.get_object("button52")
button53 = x.get_object("button53")
button54 = x.get_object("button54")
button55 = x.get_object("button55")
button56 = x.get_object("button56")
button57 = x.get_object("button57")
button58 = x.get_object("button58")
button59 = x.get_object("button59")
button60 = x.get_object("button60")
button61 = x.get_object("button61")
button62 = x.get_object("button62")
button63 = x.get_object("button63")
button64 = x.get_object("button64")
button65 = x.get_object("button65")
button66 = x.get_object("button66")
button67 = x.get_object("button67")
button68 = x.get_object("button68")
button69 = x.get_object("button69")
button70 = x.get_object("button70")
button71 = x.get_object("button71")
button72 = x.get_object("button72")
button73 = x.get_object("button73")
button74 = x.get_object("button74")
button75 = x.get_object("button75")
button76 = x.get_object("button76")
button77 = x.get_object("button77")
button78 = x.get_object("button78")
button79 = x.get_object("button79")
button80 = x.get_object("button80")
button81 = x.get_object("button81")
button82 = x.get_object("button82")
button83 = x.get_object("button83")
button84 = x.get_object("button84")
button85 = x.get_object("button85")
button86 = x.get_object("button86")
button87 = x.get_object("button87")
button88 = x.get_object("button88")
button89 = x.get_object("button89")
button90 = x.get_object("button90")
button91 = x.get_object("button91")
button92 = x.get_object("button92")
button93 = x.get_object("button93")
button94 = x.get_object("button94")
button95 = x.get_object("button95")
button96 = x.get_object("button96")
button97 = x.get_object("button97")
button98 = x.get_object("button98")
button99 = x.get_object("button99")
button100 = x.get_object("button100")
button101 = x.get_object("button101")
button102 = x.get_object("button102")
button103 = x.get_object("button103")
button104 = x.get_object("button104")
button105 = x.get_object("button105")
button106 = x.get_object("button106")
button107 = x.get_object("button107")
button108 = x.get_object("button108")
button109 = x.get_object("button109")
button110 = x.get_object("button110")
button111 = x.get_object("button111")
button112 = x.get_object("button112")
button113 = x.get_object("button113")
button114 = x.get_object("button114")
button115 = x.get_object("button115")
button116 = x.get_object("button116")
button117 = x.get_object("button117")
button118 = x.get_object("button118")
button119 = x.get_object("button119")
button120 = x.get_object("button120")
button121 = x.get_object("button121")
button122 = x.get_object("button122")
button123 = x.get_object("button123")
button124 = x.get_object("button124")




show1 = x.get_object("show1")
show2 = x.get_object("show2")
show3 = x.get_object("show3")
show4 = x.get_object("show4")
show5 = x.get_object("show5")
show6 = x.get_object("show6")
show7 = x.get_object("show7")
show8 = x.get_object("show8")
show9 = x.get_object("show9")
show10 = x.get_object("show10")
show11 = x.get_object("show11")
show12 = x.get_object("show12")
show13 = x.get_object("show13")
show14 = x.get_object("show14")
show15 = x.get_object("show15")
show16 = x.get_object("show16")
show17 = x.get_object("show17")
show18 = x.get_object("show18")
show19 = x.get_object("show19")
show20 = x.get_object("show20")
show21 = x.get_object("show21")
show22 = x.get_object("show22")
show23 = x.get_object("show23")
show24 = x.get_object("show24")
show25 = x.get_object("show25")
show26 = x.get_object("show26")
show27 = x.get_object("show27")
show28 = x.get_object("show28")
show29 = x.get_object("show29")
show30 = x.get_object("show30")
show31 = x.get_object("show31")
show32 = x.get_object("show32")
show33 = x.get_object("show33")
show34 = x.get_object("show34")
show35 = x.get_object("show35")
show36 = x.get_object("show36")
show37 = x.get_object("show37")
show38 = x.get_object("show38")
show39 = x.get_object("show39")
show40 = x.get_object("show40")
show41 = x.get_object("show41")
show42 = x.get_object("show42")
show43 = x.get_object("show43")
show44 = x.get_object("show44")
show45 = x.get_object("show45")
show46 = x.get_object("show46")
show47 = x.get_object("show47")
show48 = x.get_object("show48")
show49 = x.get_object("show49")
show50 = x.get_object("show50")
show51 = x.get_object("show51")
show52 = x.get_object("show52")
show53 = x.get_object("show53")
show54 = x.get_object("show54")
show55 = x.get_object("show55")
show56 = x.get_object("show56")
show57 = x.get_object("show57")
show58 = x.get_object("show58")
show59 = x.get_object("show59")
show60 = x.get_object("show60")
show61 = x.get_object("show61")



x.connect_signals(Handler())

k = ['salad','soup','pasta','pizza','rice','meat','dessert','drinks','others','recommended']
	
def initiaal_combo(z) :
		
	i=0
	while 1 :
		if i <=9 :
			x1.append_text("{}".format(k[i]))
			x2.append_text("{}".format(k[i]))
			x3.append_text("{}".format(k[i]))
			x4.append_text("{}".format(k[i]))
			x5.append_text("{}".format(k[i]))
			x6.append_text("{}".format(k[i]))
			x7.append_text("{}".format(k[i]))
			x8.append_text("{}".format(k[i]))
			x9.append_text("{}".format(k[i]))
			print "{}".format(k[i])			
			i=i+1

		else : 
			break
	
	
def get_combo (z):
	print (z)
	#x1.append_text("Omar is hacker")
	#remove(position)
	com = x2.get_active_text()
	
	
	#e1.set_editable(0)
	#e1.set_activates_default(1)
	#e1.set_overwrite_mode(1)
	
	
	print com ;
	return com


initiaal_combo(1)

button3.connect("clicked", z1)
button4.connect("clicked", z2)
button13.connect("clicked", z3)
button14.connect("clicked", z4)
button1.connect("clicked", z5)
button2.connect("clicked", z6)
button11.connect("clicked", z7)
button12.connect("clicked", z8)
button17.connect("clicked", z9)
button18.connect("clicked", z10)
button15.connect("clicked", z11)
button16.connect("clicked", z12)
button19.connect("clicked", z13)
button20.connect("clicked", z14)
button9.connect("clicked", z15)
button10.connect("clicked", z16)
button27.connect("clicked", z17)
button28.connect("clicked", z18)
button25.connect("clicked", z19)
button26.connect("clicked", z20)
button29.connect("clicked", z21)
button30.connect("clicked", z22)
button23.connect("clicked", z23)
button24.connect("clicked", z24)
button37.connect("clicked", z25)
button38.connect("clicked", z26)
button35.connect("clicked", z27)
button36.connect("clicked", z28)
button39.connect("clicked", z29)
button40.connect("clicked", z30)
button33.connect("clicked", z31)
button34.connect("clicked", z32)
button47.connect("clicked", z33)
button48.connect("clicked", z34)
button45.connect("clicked", z35)
button46.connect("clicked", z36)
button49.connect("clicked", z37)
button50.connect("clicked", z38)
button43.connect("clicked", z39)
button44.connect("clicked", z40)
button57.connect("clicked", z41)
button58.connect("clicked", z42)
button55.connect("clicked", z43)
button56.connect("clicked", z44)
button59.connect("clicked", z45)
button60.connect("clicked", z46)
button53.connect("clicked", z47)
button54.connect("clicked", z48)
button67.connect("clicked", z49)
button68.connect("clicked", z50)
button65.connect("clicked", z51)
button66.connect("clicked", z52)
button69.connect("clicked", z53)
button70.connect("clicked", z54)
button63.connect("clicked", z55)
button64.connect("clicked", z56)
button77.connect("clicked", z57)
button78.connect("clicked", z58)
button75.connect("clicked", z59)
button76.connect("clicked", z60)
button79.connect("clicked", z61)
button80.connect("clicked", z62)
button73.connect("clicked", z63)
button74.connect("clicked", z64)
button87.connect("clicked", z65)
button88.connect("clicked", z66)
button85.connect("clicked", z67)
button86.connect("clicked", z68)
button89.connect("clicked", z69)
button90.connect("clicked", z70)
button83.connect("clicked", z71)
button84.connect("clicked", z72)

button5.connect("clicked", z33)
button6.connect("clicked", z34)
button7.connect("clicked", z41)
button21.connect("clicked", z42)
button32.connect("clicked", z9)
button41.connect("clicked", z10)
button42.connect("clicked", z25)
button51.connect("clicked", z26)
button52.connect("clicked", z35)
button61.connect("clicked", z36)
button91.connect("clicked", z11)
button92.connect("clicked", z12)
button93.connect("clicked", z27)
button94.connect("clicked", z28)
button95.connect("clicked", z37)
button96.connect("clicked", z38)
button97.connect("clicked", z43)
button98.connect("clicked", z44)
button99.connect("clicked", z69)
button100.connect("clicked", z70)

button101.connect("clicked", z15)
button102.connect("clicked", z16)

button103.connect("clicked", z29)
button104.connect("clicked", z30)
button105.connect("clicked", z47)
button106.connect("clicked", z48)
button107.connect("clicked", z45)
button108.connect("clicked", z46)
button109.connect("clicked", z71)
button110.connect("clicked", z72)
button117.connect("clicked", z39)
button118.connect("clicked", z40)
button123.connect("clicked", z31)
button124.connect("clicked", z32)


button22.connect("clicked", z73)
button31.connect("clicked", z74)
button62.connect("clicked", z75)
button71.connect("clicked", z76)
button72.connect("clicked", z77)
button81.connect("clicked", z78)
button111.connect("clicked", z79)
button112.connect("clicked", z80)
button113.connect("clicked", z81)
button114.connect("clicked", z82)
button115.connect("clicked", z83)
button116.connect("clicked", z84)
button119.connect("clicked", z85)
button120.connect("clicked", z86)
button121.connect("clicked", z87)
button122.connect("clicked", z88)

def checkout (z):
		omar1()
	
		print "first"
		mat[50]=yy
		print mat[50]
		s.send (str(mat))
		print "end"
ch.connect("clicked", checkout)
b1.connect("clicked", checkout)
ch2.connect("clicked", checkout)
ch3.connect("clicked", checkout)
ch4.connect("clicked", checkout)
ch5.connect("clicked", checkout)
ch6.connect("clicked", checkout)
ch7.connect("clicked", checkout)
ch8.connect("clicked", checkout)
ch9.connect("clicked", checkout)
		
window11.show_all()
Gtk.main()

