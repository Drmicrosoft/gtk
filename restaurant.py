
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





class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
        system.exit();

    def onButtonPressed(self, b1):
		Gtk.main_quit(*args)
		print ("Omar is hacker")
		system.exit()


x = Gtk.Builder()
x.add_from_file("restaurant.glade")
print ("Hacked")
p= x.get_objects()



rice = x.get_object("Rice")
chicken = x.get_object("Chicken")
salad = x.get_object("Salad")
classicOnionSoup = x.get_object("ClassicOnionSoup")
hotDogPizza = x.get_object("HotDogPizza")
greenBeansRice = x.get_object("GreenBeansRice")
veal = x.get_object("Veal")
nachosVeal  = x.get_object("NachosVeal")
sweetCornSoup = x.get_object("SweetCornSoup")
cheesePizza = x.get_object("CheesePizza")
seaFoodRice = x.get_object("SeaFoodRice")
italIanChicken = x.get_object("ItalIanChicken")
cornOnTheCob = x.get_object("CornOnTheCob")
mushroomSoup = x.get_object("MushroomSoup")
anchoviePizza = x.get_object("AnchoviePizza")
mexicanRice = x.get_object("MexicanRice")
italianBeef = x.get_object("ItalianBeef")
specialFries = x.get_object("SpecialFries")
creamChickenSoup = x.get_object("CreamChickenSoup")
hawaiianPizza = x.get_object("HawaiianPizza")
seaFoodPasta = x.get_object("SeaFoodPasta")
mexicanBeef = x.get_object("MexicanBeef")
mashedPotato = x.get_object("MashedPotato")
beefSoup = x.get_object("BeefSoup")
veggiePizza = x.get_object("VeggiePizza")
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

mat  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
	

def Rice (z) :
	
	global yy
	yy=yy+8
	global mat
	mat[0]=mat[0] + 1;
	


	tv1.set_text(str(yy))

def Chicken (z) :
	global yy
	yy=yy+53
	global mat
	mat[1]=mat[1] + 1;
	


	tv1.set_text(str(yy))
def Salad (z) :
	global yy
	yy=yy+10
	global mat
	mat[2]=mat[2] + 1;
	


	tv1.set_text(str(yy))

def ClassicOnionSoup (z) :
	global yy
	yy=yy+16
	global mat
	mat[3]=mat[3] + 1;
	


	tv1.set_text(str(yy))

def HotDogPizza (z) :
	global yy
	yy=yy+45
	global mat
	mat[4]=mat[4] + 1;
	


	tv1.set_text(str(yy))

def GreenBeansRice (z) :
	global yy
	yy=yy+13
	global mat
	mat[5]=mat[5] + 1;
	


	tv1.set_text(str(yy))	
def Veal (z) :
	global yy
	yy=yy+60
	global mat
	mat[6]=mat[6] + 1;
	


	tv1.set_text(str(yy))

def NachosVeal (z) :
	global yy
	yy=yy+55
	global mat
	mat[7]=mat[7] + 1;
	


	tv1.set_text(str(yy))

def CheesePizza (z) :
	global yy
	yy=yy+55
	global mat
	mat[8]=mat[8] + 1;
	


	tv1.set_text(str(yy))

def SeaFoodRice (z) :
	global yy
	yy=yy+15
	global mat
	mat[9]=mat[9] + 1;
	


	tv1.set_text(str(yy))

def SweetCornSoup (z) :
	global yy
	yy=yy+19
	global mat
	mat[10]=mat[10] + 1;
	


	tv1.set_text(str(yy))

def ItalIanChicken (z) :
	global yy
	yy=yy+45
	global mat
	mat[11]=mat[11] + 1;
	


	tv1.set_text(str(yy))

def CornOnTheCob (z) :
	global yy
	yy=yy+15
	global mat
	mat[12]=mat[12] + 1;
	


	tv1.set_text(str(yy))

def MushroomSoup (z) :
	global yy
	yy=yy+16
	global mat
	mat[13]=mat[13] + 1;
	


	tv1.set_text(str(yy))

def AnchoviePizza (z) :
	global yy
	yy=yy+55
	global mat
	mat[14]=mat[14] + 1;
	


	tv1.set_text(str(yy))

def MexicanRice (z) :
	global yy
	yy=yy+10
	global mat
	mat[15]=mat[15] + 1;
	


	tv1.set_text(str(yy))

def ItalianBeef (z) :
	global yy
	yy=yy+83
	global mat
	mat[16]=mat[16] + 1;
	


	tv1.set_text(str(yy))

def SpecialFries (z) :
	global yy
	yy=yy+15
	global mat
	mat[17]=mat[17] + 1;
	


	tv1.set_text(str(yy))

def CreamChickenSoup (z) :
	global yy
	yy=yy+18
	global mat
	mat[18]=mat[18] + 1;
	


	tv1.set_text(str(yy))

def HawaiianPizza (z) :
	global yy
	yy=yy+55
	global mat
	mat[19]=mat[19] + 1;
	


	tv1.set_text(str(yy))

def SeaFoodPasta (z) :
	global yy
	yy=yy+50
	global mat
	mat[20]=mat[20] + 1;
	


	tv1.set_text(str(yy))

def MexicanBeef (z) :
	global yy
	yy=yy+83
	global mat
	mat[21]=mat[21] + 1;
	


	tv1.set_text(str(yy))

def MashedPotato (z) :
	global yy
	yy=yy+10
	global mat
	mat[22]=mat[22] + 1;
	


	tv1.set_text(str(yy))

def BeefSoup (z) :
	global yy
	yy=yy+22
	global mat
	mat[23]=mat[23] + 1;
	


	tv1.set_text(str(yy))

def VeggiePizza (z) :
	global yy
	yy=yy+40
	global mat
	mat[24]=mat[24] + 1;
	


	tv1.set_text(str(yy))


#rise.connect("clicked", Gtk.main_quit)
c()
rice.connect("clicked", Rice)
chicken.connect("clicked", Chicken)
salad.connect("clicked", Salad)
classicOnionSoup.connect("clicked", ClassicOnionSoup)
hotDogPizza.connect("clicked", HotDogPizza)
greenBeansRice.connect("clicked", GreenBeansRice)
veal.connect("clicked", Veal)
nachosVeal.connect("clicked", NachosVeal)
cheesePizza.connect("clicked", CheesePizza)
seaFoodRice.connect("clicked", SeaFoodRice)
sweetCornSoup.connect("clicked", SweetCornSoup)
italIanChicken.connect("clicked", ItalIanChicken)
cornOnTheCob.connect("clicked", CornOnTheCob)
mushroomSoup.connect("clicked", MushroomSoup)
anchoviePizza.connect("clicked", AnchoviePizza)
mexicanRice.connect("clicked", MexicanRice)
italianBeef.connect("clicked", ItalianBeef)
specialFries.connect("clicked", SpecialFries)
creamChickenSoup.connect("clicked", CreamChickenSoup)
hawaiianPizza.connect("clicked", HawaiianPizza)
seaFoodPasta.connect("clicked", SeaFoodPasta)
mexicanBeef.connect("clicked", MexicanBeef)
mashedPotato.connect("clicked", MashedPotato)
beefSoup.connect("clicked", BeefSoup)
veggiePizza.connect("clicked", VeggiePizza)

def checkout (z):
	omar1()
	
	s=socket.socket()
	port=11111

	s.connect(("",port))
	s.send (str(mat))
	y =s.recv(1024);
	if(y=='1'):
		s.send(str(yy))
	
	
	


check_out.connect("clicked", checkout)

omar1()
omar()
omar1()


Gtk.main()
