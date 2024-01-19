
# Modification date: Fri Dec 23 22:12:30 2022

# Production date: Wed Jan 17 22:46:05 2024

from Hareketli_Obje import *
from mesafe import *
import pygame

pygame.init()


pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

patlama_sesi = pygame.mixer.Sound("boom_müzik.mp3")#patlama.wav")
patlama_sesi.set_volume(0.1)

class Patlama(Hareketli_Obje):
	def __init__(self, x, y, genislik, yukseklik, yerden_yukseklik, can, hiz, guc, p1, p2, p3):
		pygame.mixer.find_channel().play(patlama_sesi)
		#Parametrelerden gelen değerleri objeye almak/işlemek
		Hareketli_Obje.__init__(self, x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
		self.yerden_yukseklik = yerden_yukseklik
		self.guc = guc
		self.patlama_suresi = 5

		#patlama büyüklüğümü hesaplayıp oranlama
		self.p1 = pygame.transform.scale(p1, (self.genislik, self.genislik))
		self.p2 = pygame.transform.scale(p2, (self.genislik, self.genislik))
		self.p3 = pygame.transform.scale(p3, (self.genislik, self.genislik))

	def hasar_ver(self, objeler_listesi, adambot):
		for objeler in objeler_listesi:
			for obje in objeler:#bütün objeleri tek tek alttaki testten geçirip gerekirse hasar vereceğiz
				if mesafe((self.x, self.y), (obje.x, obje.y)) < self.genislik * 5/4 and abs(self.yerden_yukseklik - obje.yerden_yukseklik) < self.genislik * 5/4:#patlama alanı patlamanın genişliğinin 125% kadarı olacak
					obje.can -= self.guc * self.genislik/(mesafe((self.x, self.y), (obje.x, obje.y))+1)#objeden oranla can azaltmak
		if mesafe((self.x, self.y), (adambot.x, adambot.y)) < self.genislik * 5/4 and abs(self.yerden_yukseklik - adambot.yerden_yukseklik) < self.genislik * 5/4:#patlama alanı patlamanın genişliğinin 125% kadarı olacak
			adambot.can -= (self.guc * self.genislik/(mesafe((self.x, self.y), (adambot.x, adambot.y))+1))/200#objeden oranla can azaltmak
		self.patlama_suresi -= 1#patlama süresini 1 azaltmak
		return
	def ana_ekrana_ciz(self, pencere):
		if self.patlama_suresi > 3:
			pencere.blit(self.p1, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
		elif self.patlama_suresi > 1:
			pencere.blit(self.p2, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
		else:
			pencere.blit(self.p3, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
		return
