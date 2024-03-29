
# Modification date: Wed Dec  7 08:14:52 2022

# Production date: Wed Jan 17 22:46:05 2024

import pygame
from pygame import Color
from math import sqrt
from random import choice, randint, uniform

from Adambot import *
from Bomba import *
#from Cekicadam_Gizli_AntiHava_Savunmasi import *
from Dugme import *
from herseyi_kaydir import *
from Mermi import *
from mesafe import *
from Patlama import *
from Tank import *
from Yazi import *
from Zemin import *



pygame.init()

genislik, yukseklik = 600, 400
bayraklar = pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME
ana_pencere = pygame.display.set_mode((genislik, yukseklik), bayraklar)#, 0, 32)#, pygame.FULLSCREEN)
monitor_buyuklugu = [pygame.display.Info().current_w, pygame.display.Info().current_h]#[genislik, yukseklik]
#zeminustu_yuzeyi = pygame.Surface((genislik, yukseklik))
#ana_pencere = pygame.display.set_mode((monitor_buyuklugu[0], monitor_buyuklugu[1]), pygame.RESIZABLE)

#pygame.display.set_caption("Adambot")


pygame.mixer.pre_init(44100, -16, 2, 512) #frequency, size, channels, buffersize

patlama_sesi = pygame.mixer.Sound("boom_müzik.mp3")#patlama.wav")
patlama_sesi.set_volume(0.1)
muzik = pygame.mixer.Sound("müzik.mp3")
muzik.set_volume(0.1)
bzz = pygame.mixer.Sound("BrrrrrrrrKısık.wav")
bzz.set_volume(0.2)

#Team Fortress 2 Resupply Cabinet sound effect.mp3
cephane_yenileme_sesi = pygame.mixer.Sound("Team Fortress 2 Resupply Cabinet sound effect.mp3")
cephane_yenileme_sesi.set_volume(0.1)
pygame.mixer.set_num_channels(999)







patlamalar = []
askerler = []
tanklar = []
zeminler = []
bombalar = []

absol = pygame.image.load("Adambot_Sol.png").convert_alpha()
absag = pygame.image.load("Adambot_Sağ.png").convert_alpha()
abasa = pygame.image.load("Adambot_Aşağı.png").convert_alpha()
abyuk = pygame.image.load("Adambot_Yukarı.png").convert_alpha()

absolg = pygame.image.load("Adambot_Sol_Gölge.png").convert_alpha()
absagg = pygame.image.load("Adambot_Sağ_Gölge.png").convert_alpha()
abasag = pygame.image.load("Adambot_Aşağı_Gölge.png").convert_alpha()
abyukg = pygame.image.load("Adambot_Yukarı_Gölge.png").convert_alpha()

abbuyukluk = 16

absol = pygame.transform.scale(absol, (abbuyukluk, abbuyukluk))
absag = pygame.transform.scale(absag, (abbuyukluk, abbuyukluk))
abasa = pygame.transform.scale(abasa, (abbuyukluk, abbuyukluk))
abyuk = pygame.transform.scale(abyuk, (abbuyukluk, abbuyukluk))
absolg = pygame.transform.scale(absolg, (abbuyukluk, abbuyukluk))
absagg= pygame.transform.scale(absagg, (abbuyukluk, abbuyukluk))
abasag = pygame.transform.scale(abasag, (abbuyukluk, abbuyukluk))
abyukg = pygame.transform.scale(abyukg, (abbuyukluk, abbuyukluk))

adambot = Adambot(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2, abbuyukluk, abbuyukluk, 1000, 1.5, 15, 300, 1, monitor_buyuklugu)

patlama1 = pygame.image.load("Patlama1.png").convert_alpha()
patlama2 = pygame.image.load("Patlama2.png").convert_alpha()
patlama3 = pygame.image.load("Patlama3.png").convert_alpha()

bomba_sol = pygame.image.load("Bomba_Sol.png").convert_alpha()
bomba_sag = pygame.image.load("Bomba_Sağ.png").convert_alpha()
bomba_asa = pygame.image.load("Bomba_Aşağı.png").convert_alpha()
bomba_yuk = pygame.image.load("Bomba_Yukarı.png").convert_alpha()



duran_tank = pygame.image.load("tank.png").convert_alpha()
patlamis_tank1 = pygame.image.load("Tank_patlamış1.png").convert_alpha()
patlamis_tank2 = pygame.image.load("Tank_patlamış2.png").convert_alpha()
patlamis_tank3 = pygame.image.load("Tank_patlamış3.png").convert_alpha()

duran_tank = pygame.transform.scale(duran_tank, (abbuyukluk*2, abbuyukluk*2))
patlamis_tank1 = pygame.transform.scale(patlamis_tank1, (abbuyukluk*2, abbuyukluk*2))
patlamis_tank2 = pygame.transform.scale(patlamis_tank2, (abbuyukluk*2, abbuyukluk*2))
patlamis_tank3 = pygame.transform.scale(patlamis_tank3, (abbuyukluk*2, abbuyukluk*2))

fayans = pygame.image.load("Zemin_Fayansı.png").convert_alpha()
tank_fayansi = pygame.image.load("Tank_Fayansı.png").convert_alpha()


baslama_dugmesi = Dugme(monitor_buyuklugu[0]//4, int(monitor_buyuklugu[1]*0.6875), monitor_buyuklugu[0]//2, int(monitor_buyuklugu[1]*0.1875), (150, 150, 150), "Basla")
sol_dugme = Dugme(int(monitor_buyuklugu[0]*0.05), int(monitor_buyuklugu[1]*0.6), int(monitor_buyuklugu[0]*0.05), int(monitor_buyuklugu[1]*0.3), (150, 150, 150), " ")
sag_dugme = Dugme(int(monitor_buyuklugu[0]*0.20), int(monitor_buyuklugu[1]*0.6), int(monitor_buyuklugu[0]*0.05), int(monitor_buyuklugu[1]*0.3), (150, 150, 150), " ")
yuk_dugme = Dugme(int(monitor_buyuklugu[0]*0.05), int(monitor_buyuklugu[1]*0.6), int(monitor_buyuklugu[0]*0.2), int(monitor_buyuklugu[1]*0.1), (150, 150, 150), "^")
asa_dugme = Dugme(int(monitor_buyuklugu[0]*0.05), int(monitor_buyuklugu[1]*0.8), int(monitor_buyuklugu[0]*0.2), int(monitor_buyuklugu[1]*0.1), (150, 150, 150), "v")
yuksel_dugme = Dugme(monitor_buyuklugu[0]*16//20, int(monitor_buyuklugu[1]*0.7), monitor_buyuklugu[0]//10, int(monitor_buyuklugu[1]*0.1), (150, 150, 150), "^^")
alcal_dugme = Dugme(monitor_buyuklugu[0]*16//20, int(monitor_buyuklugu[1]*0.8), monitor_buyuklugu[0]//10, int(monitor_buyuklugu[1]*0.1), (150, 150, 150), "vv")
kamikaze_dugme = Dugme(monitor_buyuklugu[0]*18//20, int(monitor_buyuklugu[1]*0.6), monitor_buyuklugu[0]//10, int(monitor_buyuklugu[1]*0.1), (150, 150, 150), "O")
bomba_dugme = Dugme(monitor_buyuklugu[0]*18//20, int(monitor_buyuklugu[1]*0.7), monitor_buyuklugu[0]//10, int(monitor_buyuklugu[1]*0.1), (150, 150, 150), "o")
ates_dugme = Dugme(monitor_buyuklugu[0]*18//20, int(monitor_buyuklugu[1]*0.8), monitor_buyuklugu[0]//10, int(monitor_buyuklugu[1]*0.1), (150, 150, 150), "i")






gorev_yazisi = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2, int(monitor_buyuklugu[1]*0.0375), "Gorev: Hammerman\'in acikhava tank hangarini yok et.")
gorev_yazisi0 = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2 - int(monitor_buyuklugu[1]*0.0375*2), int(monitor_buyuklugu[1]*0.0375), "Tanklar solda olacak.")
gorev_yazisi1 = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2 - int(monitor_buyuklugu[1]*0.0375*4), int(monitor_buyuklugu[1]*0.0375), "Kamikaze saldirisi icin yuksel ve bosluga bas.")
gorev_yazisi2 = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2 - int(monitor_buyuklugu[1]*0.0375*6), int(monitor_buyuklugu[1]*0.0375), "Ok tuslari ile hareket et, w/s ile yuksel/alcal.")
gorev_yazisi3 = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2 - int(monitor_buyuklugu[1]*0.0375*8), int(monitor_buyuklugu[1]*0.0375), "E tusu ile ates et.")

asama = 0#0 menü, 1 savaş, 2 oyun sonu ekranı


parmaklar = {}

clock = pygame.time.Clock()
running = True
basili = False
while running:
	clock.tick(30)
	ana_pencere.fill((52, 140, 49))
	if asama == 0:
		baslama_dugmesi.ekrana_ciz(ana_pencere)
		gorev_yazisi0.ekrana_ciz(ana_pencere)
		gorev_yazisi1.ekrana_ciz(ana_pencere)
		gorev_yazisi2.ekrana_ciz(ana_pencere)
		gorev_yazisi3.ekrana_ciz(ana_pencere)
		gorev_yazisi.ekrana_ciz(ana_pencere)
		basilan_tuslar = pygame.key.get_pressed()


		if basili:
			parmaklar["fare"] = pygame.mouse.get_pos()
			for parmak in parmaklar:
				pygame.draw.circle(ana_pencere, (100, 200, 70), parmaklar[parmak], 50)
		else:
			parmaklar["fare"] = (-1, -1)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.FINGERUP:
				parmaklar.pop(event.finger_id, None)
			if event.type == pygame.FINGERDOWN:
				basili = True
				x = event.x * monitor_buyuklugu[0]
				y = event.y * monitor_buyuklugu[1]
				parmaklar[event.finger_id] = x, y
			if event.type == pygame.FINGERMOTION:
				basili = True
				x = event.x * monitor_buyuklugu[0]
				y = event.y * monitor_buyuklugu[1]
				parmaklar[event.finger_id] = x, y
			if event.type == pygame.MOUSEBUTTONUP:
				basili = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				basili = True
				
		if baslama_dugmesi.tiklama_kontrolu(parmaklar):
			asama = 1
			adambot.yerden_yukseklik = 0
			adambot_zemini = Zemin(200, 200, 400, 400, fayans, True)
			zeminler.append(adambot_zemini)
			zeminler.append(Zemin(-2064, -64, 2024, 2024, tank_fayansi, False))#tank_fayansi
			#tank_zemini = Zemin(0, 0, monitor_buyuklugu[0], monitor_buyuklugu[1], fayans, False)
			for i in range(12):
				for j in range(5):
					if True:#choice([True, False]):
						tanklar.append(Tank(-2000 + i * abbuyukluk*2, j * 70, 100, 100, 500, 0))
			tank_sayisi = len(tanklar)
			gorev_yazisi = Yazi(monitor_buyuklugu[0]//2, 60, 30, "Kalan tank sayisi: " + str(tank_sayisi))
			pygame.mixer.find_channel().play(muzik, -1)
			pygame.mixer.find_channel().play(bzz, -1)
		if basilan_tuslar[pygame.K_ESCAPE] or not(running):
			break
		
		
	elif asama == 1:
		basilan_tuslar = pygame.key.get_pressed()
		
		
		if basili:
			parmaklar["fare"] = pygame.mouse.get_pos()
			for parmak in parmaklar:
				pygame.draw.circle(ana_pencere, (250, 30, 30), parmaklar[parmak], 50)
		else:
			parmaklar["fare"] = (-1, -1)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.FINGERUP:
				parmaklar.pop(event.finger_id, None)
			if event.type == pygame.FINGERDOWN:
				basili = True
				x = event.x * monitor_buyuklugu[0]
				y = event.y * monitor_buyuklugu[1]
				parmaklar[event.finger_id] = x, y
			if event.type == pygame.FINGERMOTION:
				basili = True
				x = event.x * monitor_buyuklugu[0]
				y = event.y * monitor_buyuklugu[1]
				parmaklar[event.finger_id] = x, y
			if event.type == pygame.MOUSEBUTTONUP:
				basili = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				basili = True


		if basilan_tuslar[pygame.K_ESCAPE] or not(running):
			break
		if basilan_tuslar[pygame.K_RIGHT] or basilan_tuslar[pygame.K_LEFT] or basilan_tuslar[pygame.K_UP] or basilan_tuslar[pygame.K_DOWN] or (basilan_tuslar[pygame.K_w] and not(adambot.kamikaze_saldirisinda)) or (basilan_tuslar[pygame.K_s] and not(adambot.kamikaze_saldirisinda)):
			bzz.set_volume(0.5)
		else:
			bzz.set_volume(0.2)
		
		if basilan_tuslar[pygame.K_RIGHT] or sag_dugme.tiklama_kontrolu(parmaklar):
			adambot.sagb = True
			adambot.solb = False
			adambot.sagg = True
			adambot.solg = False
		elif basilan_tuslar[pygame.K_LEFT] or sol_dugme.tiklama_kontrolu(parmaklar):
			adambot.sagb = False
			adambot.solb = True
			adambot.sagg = False
			adambot.solg = True
		else:
			adambot.sagg = False
			adambot.solg = False
			if adambot.yukb or adambot.asab:
				adambot.sagb, adambot.solb = False, False
		if basilan_tuslar[pygame.K_UP] or yuk_dugme.tiklama_kontrolu(parmaklar):
			adambot.yukb = True
			adambot.asab = False
			adambot.yukg = True
			adambot.asag = False
		elif basilan_tuslar[pygame.K_DOWN] or asa_dugme.tiklama_kontrolu(parmaklar):
			adambot.yukb = False
			adambot.asab = True
			adambot.yukg = False
			adambot.asag = True
		else:
			adambot.yukg = False
			adambot.asag = False
			if adambot.sagb or adambot.solb:
				adambot.yukb, adambot.asab = False, False
		if kamikaze_dugme.tiklama_kontrolu(parmaklar) or basilan_tuslar[pygame.K_SPACE] or adambot.kamikaze_saldirisinda:
			adambot.kamikaze_saldirisi(patlamalar, patlama1, patlama2, patlama3)
		if (basilan_tuslar[pygame.K_w] or yuksel_dugme.tiklama_kontrolu(parmaklar)) and not(adambot.kamikaze_saldirisinda):
			if adambot.yerden_yukseklik + adambot.hiz <= 200:
				adambot.yerden_yukseklik += adambot.hiz * 2
		if (basilan_tuslar[pygame.K_s] or alcal_dugme.tiklama_kontrolu(parmaklar)) and not(adambot.kamikaze_saldirisinda):
			if adambot.yerden_yukseklik - adambot.hiz >= 0:
				adambot.yerden_yukseklik -= adambot.hiz

		
		
		adambot.akiskan_hareket_sistemi()
		adambot.hareket_et_ivmeli()
		adambot.sayac_arttir()
		
		adambot, patlamalar, tanklar, zeminler, bombalar = herseyi_kaydir(adambot, monitor_buyuklugu, patlamalar, tanklar, zeminler, bombalar)

		for zemin in zeminler:
			zemin.ana_ekrana_ciz(ana_pencere)
		for tank in tanklar:
			tank_sayisi = tank.sayi_dusur(tank_sayisi)
			tank.ana_ekrana_ciz(ana_pencere, duran_tank, patlamis_tank1, patlamis_tank2, patlamis_tank3)
		adambot.golge_ciz(ana_pencere, absagg, absolg, abasag, abyukg, abbuyukluk)
		for bomba in bombalar:
			bomba.akiskan_hareket_sistemi()
			bomba.hareket_et_ivmeli()
			bomba.ana_ekrana_ciz(ana_pencere, bomba_sag, bomba_sol, bomba_asa, bomba_yuk)
			bruh  = bomba.dus(patlamalar, patlama1, patlama2, patlama3)
			if bruh:
				bombalar.remove(bomba)
		for patlama in patlamalar:
			if patlama.patlama_suresi <= 0:
				patlamalar.remove(patlama)
				continue
			else:
				patlama.hasar_ver(tanklar)
				patlama.ana_ekrana_ciz(ana_pencere)
				
		if basilan_tuslar[pygame.K_e] or ates_dugme.tiklama_kontrolu(parmaklar):
			adambot.ates_et(ana_pencere, tanklar)
		if basilan_tuslar[pygame.K_q] or bomba_dugme.tiklama_kontrolu(parmaklar):
			bombalar = adambot.bomba_birak(bombalar)
			
		if adambot.yerden_yukseklik == 0:
			if adambot.x >= zeminler[0].x and adambot.x <= zeminler[0].x + zeminler[0].genislik:
				if adambot.y >= zeminler[0].y and adambot.y <= zeminler[0].y + zeminler[0].yukseklik:
					adambot.cephane_doldur()
					
		
			
		if tank_sayisi > 0:
			gorev_yazisi.yazi = "Kalan tank sayisi: " + str(tank_sayisi)
		else:
			gorev_yazisi.yazi = "Ussune geri don ve inis yap."
			if adambot.yerden_yukseklik == 0:
				if adambot.x >= zeminler[0].x and adambot.x <= zeminler[0].x + zeminler[0].genislik:
					if adambot.y >= zeminler[0].y and adambot.y <= zeminler[0].y + zeminler[0].yukseklik:
						asama = 2
						gorev_yazisi.yazi = "Adam."
						gorev_yazisi.x = monitor_buyuklugu[0]/2
						gorev_yazisi.y = monitor_buyuklugu[1]/2
		adambot.ana_ekrana_ciz(ana_pencere, absag, absol, abasa, abyuk)
		sol_dugme.ekrana_ciz(ana_pencere)
		sag_dugme.ekrana_ciz(ana_pencere)
		asa_dugme.ekrana_ciz(ana_pencere)
		yuk_dugme.ekrana_ciz(ana_pencere)
		yuksel_dugme.ekrana_ciz(ana_pencere)
		alcal_dugme.ekrana_ciz(ana_pencere)
		kamikaze_dugme.ekrana_ciz(ana_pencere)
		bomba_dugme.ekrana_ciz(ana_pencere)
		ates_dugme.ekrana_ciz(ana_pencere)
		
		adambot.cephane_goster(ana_pencere)
		gorev_yazisi.ekrana_ciz(ana_pencere)







	elif asama == 2:
		basilan_tuslar = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		if basilan_tuslar[pygame.K_ESCAPE] or not(running):
			break
		gorev_yazisi.ekrana_ciz(ana_pencere)
		
	pygame.display.flip()
pygame.quit()
