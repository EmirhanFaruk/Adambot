from random import randint

def ruzgar(obje_listesi_listesi, ruzgar_hizi, sayacx, sayacy, hedef_ruzgar_hizi):
	if sayacx > 2:
		sayacx -= 1
	if sayacy > 2:
		sayacy -= 1
	if randint(0, sayacx) == 1:
		hedef_ruzgar_hizi[0] = randint(-3, 3)
		sayacx = 600
	if randint(0, sayacy) == 1:
		hedef_ruzgar_hizi[1] = randint(-3, 3)
		sayacy = 600
	if abs(ruzgar_hizi[0] - hedef_ruzgar_hizi[0]) > 0.1:
		ruzgar_hizi[0] += (hedef_ruzgar_hizi[0] - ruzgar_hizi[0])/10
	else:
		ruzgar_hizi[0] = hedef_ruzgar_hizi[0]
	if abs(ruzgar_hizi[1] - hedef_ruzgar_hizi[1]) > 0.1:
		ruzgar_hizi[1] += (hedef_ruzgar_hizi[1] - ruzgar_hizi[1])/10
	else:
		ruzgar_hizi[1] = hedef_ruzgar_hizi[1]
	for obje_listesi_sayaci in range(len(obje_listesi_listesi)):
		for obje_sayaci in range(len(obje_listesi_listesi[obje_listesi_sayaci])):
			obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].x += ruzgar_hizi[0]
			obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].y += ruzgar_hizi[1]

	return obje_listesi_listesi, ruzgar_hizi, sayacx, sayacy, hedef_ruzgar_hizi