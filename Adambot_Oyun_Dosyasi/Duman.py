
# Modification date: Sat Dec 24 20:49:14 2022

# Production date: Wed Jan 17 22:46:05 2024

import pygame
from random import uniform, choice



class Duman:
	def __init__(self, x, y, boyut, buyume_hizi, yukselme_hizi, duman_resmi):
		self.x, self.y, self.boyut, self.buyume_hizi, self.yukselme_hizi = x, y, boyut, buyume_hizi, yukselme_hizi, 
		self.saydamlik = 150
		self.resim = duman_resmi
		self.resim = pygame.transform.scale(self.resim, (self.boyut*2, self.boyut*2))
	
	def guncelle(self, dumanlar):
		self.saydamlik -= 100/self.boyut
		if self.saydamlik <= 100/self.boyut:
			dumanlar.remove(self)
		else:
			self.resim.set_alpha(int(self.saydamlik))
			self.boyut += self.buyume_hizi
			self.resim = pygame.transform.scale(self.resim, (self.boyut*2, self.boyut*2))
			self.y += self.yukselme_hizi
			#self.x += uniform(0, 0.5)
			"""
			if choice([True, False, False, False, False]):
				if choice([True, False]):
					self.x += uniform(0, self.boyut * 0.1)
				else:
					self.x -= uniform(0, self.boyut * 0.1)
			"""
			
			
		
	def ekrana_ciz(self, ana_pencere):
		ana_pencere.blit(self.resim, (self.x - self.boyut, self.y - self.boyut))
		#self.yuzey = pygame.Surface((self.boyut, self.boyut), pygame.SRCALPHA)
		#self.yuzey.fill((0, 0, 0))
		#self.yuzey.set_colorkey((0, 0, 0))
		
		#pygame.draw.circle(self.yuzey, (self.renk[0], self.renk[1], self.renk[2], self.saydamlik), (self.yuzey.get_width() // 2, self.yuzey.get_height() // 2), self.boyut)
		
		#self.yuzey.blit(self.resim, (0, 0))
		
		#ana_pencere.blit(self.yuzey, self.yuzey.get_rect(center=(self.x, self.y)))