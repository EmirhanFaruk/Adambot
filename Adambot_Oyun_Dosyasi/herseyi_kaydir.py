def herseyi_kaydir(adambot, monitor_buyuklugu, obje_listesi_listesi, hedef = "bruh"):
	if hedef == "bruh":
		hedef = (adambot.x, adambot.y)
	if adambot.x != monitor_buyuklugu[0]/2 or adambot.y - adambot.yerden_yukseklik/2 != monitor_buyuklugu[1]/2:
		x_farki = -(hedef[0] - monitor_buyuklugu[0]/2)
		y_farki = -(hedef[1] - adambot.yerden_yukseklik/2 - monitor_buyuklugu[1]/2)
		
		adambot.x += x_farki*0.1
		adambot.y += y_farki*0.1
		for obje_listesi_sayaci in range(len(obje_listesi_listesi)):
			for obje_sayaci in range(len(obje_listesi_listesi[obje_listesi_sayaci])):
				obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].x += x_farki*0.1
				obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].y += y_farki*0.1

	return adambot, obje_listesi_listesi