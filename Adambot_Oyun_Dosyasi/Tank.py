from Hareketli_Obje import *
from Duman import *
import pygame
from random import choice, randint

pygame.init()

class Tank(Hareketli_Obje):
	def __init__(self, x, y, genislik, yukseklik, can, hiz):
		#Parametrelerden gelen değerleri objeye almak/işlemek
		Hareketli_Obje.__init__(self, x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
		self.dusurdu = False
		self.goruntu_sayaci = 0;
		self.yerden_yukseklik = 0

	def sayi_dusur(self, sayac):
		if not(self.dusurdu) and self.can <= 0:
			sayac -= 1
			self.dusurdu = True
			return sayac
		return sayac

	def ana_ekrana_ciz(self, pencere, r0, r1, r2, r3, dumanlar, duman_resmi):
		if self.can > 0:
			pencere.blit(r0, (self.x - self.genislik/2, self.y - self.yukseklik/2))
		else:
			if 2 == randint(1, 15):
				dumanlar.append(Duman(self.x - self.genislik/2 + uniform(0, self.genislik), self.y - self.yukseklik/2 + uniform(0, self.yukseklik), self.genislik//2, 1, -1, duman_resmi))
			self.goruntu_sayaci += 0.1
			pencere.blit([r1, r2, r3][int(self.goruntu_sayaci//3)], (self.x - self.genislik/2, self.y - self.yukseklik/2))
			if self.goruntu_sayaci >= 8:
				self.goruntu_sayaci = 0
		return
