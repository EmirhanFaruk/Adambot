
# Modification date: Fri Dec 23 15:21:54 2022

# Production date: Sun Sep  3 15:42:45 2023

import pygame
pygame.init()

def adambot_tuş_hareket(adambot, basilan_tuslar, parmaklar, sag_dugme, sol_dugme, yuk_dugme, asa_dugme, kamikaze_dugme, yuksel_dugme, alcal_dugme, patlamalar, patlama1, patlama2, patlama3):
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
		if adambot.yerden_yukseklik + adambot.hiz <= 100:
			adambot.yerden_yukseklik += adambot.hiz * 2
	if (basilan_tuslar[pygame.K_s] or alcal_dugme.tiklama_kontrolu(parmaklar)) and not(adambot.kamikaze_saldirisinda):
		if adambot.yerden_yukseklik - adambot.hiz >= 0:
			adambot.yerden_yukseklik -= adambot.hiz
	return adambot