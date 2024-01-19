
# Modification date: Wed Nov  9 20:22:22 2022

# Production date: Wed Jan 17 22:46:05 2024

import pygame
from pygame import Color
from math import sqrt
from random import choice, randint, uniform


pygame.init()

genislik, yukseklik = 800, 800
ana_pencere = pygame.display.set_mode((genislik, yukseklik), pygame.FULLSCREEN)
monitor_buyuklugu = [pygame.display.Info().current_w, pygame.display.Info().current_h]
zeminustu_yuzeyi = pygame.Surface((genislik, yukseklik))


pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

patlama_sesi = pygame.mixer.Sound("patlama.wav")
muzik = pygame.mixer.Sound("müzik.mp3")
muzik.set_volume(0.1)
patlama_sesi.set_volume(0.1)
mermi_sesi = pygame.mixer.Sound("pshot.wav")
mermi_sesi.set_volume(0.1)
pygame.mixer.set_num_channels(999)


class Yazi:
    def __init__(self, x, y, boyut, yazi):
        self.x, self.y, self.boyut, self.yazi = x, y, boyut, yazi
    def ekrana_ciz(self, pencere):
        self.fon = pygame.font.Font("PKMN_RBYGSC.ttf", self.boyut)
        self.yazi_yuzeyi = self.fon.render(self.yazi, False, (0, 0, 0))
        self.yazi_genisligi = self.yazi_yuzeyi.get_width()
        pencere.blit(self.yazi_yuzeyi, (int(self.x - self.yazi_genisligi/2), int(self.y)))

class Dugme:
    def __init__(self, x, y, genislik, yukseklik, renk, yazi):
        self.x, self.y, self.genislik, self.yukseklik, self.renk, self.yazi = x, y, genislik, yukseklik, renk, Yazi(x + genislik/2, y + yukseklik/4, yukseklik//2, yazi)
        
    def ekrana_ciz(self, pencere):
        pygame.draw.rect(pencere, self.renk, pygame.Rect(self.x, self.y, self.genislik, self.yukseklik))
        self.yazi.ekrana_ciz(pencere)
        
    def tiklama_kontrolu(self, tiklama_pozisyonu):
        if tiklama_pozisyonu[0] > self.x and tiklama_pozisyonu[0] < self.x + self.genislik:
            if tiklama_pozisyonu[1] > self.y and tiklama_pozisyonu[1] < self.y + self.yukseklik:
                return True
        return False



def mesafe(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)



class Zemin:
    def __init__(self, x, y, genislik, yukseklik, resim, resmi_fulle):
        self.x, self.y, self.genislik, self.yukseklik = x, y, genislik, yukseklik
        self.yinele_x = 0
        self.yinele_y = 0
        self.resim = resim
        if resmi_fulle:
            self.resim = pygame.transform.scale(resim, (genislik, yukseklik))
        else:
            self.yinele_x = self.genislik // self.resim.get_width()
            self.yinele_y = self.yukseklik // self.resim.get_height()
        self.resmi_fulle = resmi_fulle
    def ana_ekrana_ciz(self, pencere):
        if self.resmi_fulle:
            pencere.blit(self.resim, (self.x, self.y))
        else:
            for x in range(self.yinele_x):
                for y in range(self.yinele_y):
                    pencere.blit(self.resim, (self.x + self.resim.get_width() * x, self.y + self.resim.get_height() * y))

def Mermi(pencere, bx, by, hx, hy, hasar, muhtemel_hedefler):
    pygame.mixer.find_channel().play(mermi_sesi)
    if randint(1, 3) == 2:
        pygame.draw.line(pencere, (200, 200, 100), (bx, by), (hx, hy))
    pygame.draw.circle(pencere, (200, 200, 100), (hx, hy), 2)
    for hedef in muhtemel_hedefler:
        if hx > hedef.x - hedef.genislik/2 and hx < hedef.x + hedef.genislik/2:
            if hy > hedef.y - hedef.yukseklik/2 and hy < hedef.y + hedef.yukseklik/2:
                hedef.can -= hasar

class Cekicadam_Gizli_AntiHava_Savunmasi:
    def __init__(self, x, y, genislik, yukseklik, hasar, ates_hizi, menzil):
        return

class Hareketli_Obje:
    def __init__(self, x, y, genislik, yukseklik, can, hiz):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        self.x, self.y, self.genislik, self.yukseklik, self.can, self.hiz = x, y, genislik, yukseklik, can, hiz

        #Hareket için gerekli olan değişkenleri oluşturmak(sağa bak = sagb, sağa git = sagg gibi)
        self.sagb = True
        self.solb, self.asab, self.yukb = False, False, False
        self.sagg, self.solg, self.asag, self.yukg = False, False, False, False

        self.yerden_yukseklik = self.yukseklik#yer birimleri kendi yükseklik yüksekliğinde olacak
        return

    def hareket_et(self):#objeyi gereken değişkenlere göre hareket ettirecek olan fonksiyon
        if self.sagg:#eğer sağa gidiyorsa x koordinatını hız ile arttır
            self.x += self.hiz
        elif self.solg:
            self.x -= self.hiz
        if self.yukg:
            self.y -= self.hiz
        elif self.asag:
            self.y += self.hiz
        return

    def golge_ciz(self, pencere, sag_resim, sol_resim, asagi_resim, yukari_resim):#gölge çizme fonksiyonu
        if self.sagb:#eğer obje sağa bakıyorsa sağa bakarkenki halini çiz
            sag_resim.set_alpha(220-self.yerden_yukseklik)
            sag_resim = pygame.transform.scale(sag_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(sag_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.solb:
            sol_resim.set_alpha(220-self.yerden_yukseklik)
            sol_resim = pygame.transform.scale(sol_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(sol_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.asab:
            asagi_resim.set_alpha(220-self.yerden_yukseklik)
            asagi_resim = pygame.transform.scale(asagi_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(asagi_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.yukb:
            yukari_resim.set_alpha(220-self.yerden_yukseklik)
            yukari_resim = pygame.transform.scale(yukari_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(yukari_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        #pygame.draw.circle(pencere, ((52/255)*self.yerden_yukseklik, (140/255)*self.yerden_yukseklik, (49/255)*self.yerden_yukseklik), ((self.x), (self.y)), self.genislik/3 + self.yerden_yukseklik/10)#gölgeyi yuvarlak olarak çizmek/(52, 140, 49)
        return


    def ana_ekrana_ciz(self, pencere, sag_resim, sol_resim, asagi_resim, yukari_resim):#obje resmini gerekli şekilde çizdiren fonksiyon
        if self.sagb:#eğer obje sağa bakıyorsa sağa bakarkenki halini çiz
            pencere.blit(sag_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.solb:
            pencere.blit(sol_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.asab:
            pencere.blit(asagi_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.yukb:
            pencere.blit(yukari_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        return




class Adambot(Hareketli_Obje):
    def __init__(self, x, y, genislik, yukseklik, can, hiz, hasar, kamikaze_saldiri_gucu):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        super().__init__(x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
        self.kamikaze_saldiri_gucu = kamikaze_saldiri_gucu
        self.hasar = hasar
        #Yükseklik değişkeni ve kamikaze dolum süresi değişkenleri
        self.kamikaze_dolum_suresi = 60 #1 saniyede bir
        self.kamikaze_saldirisi_yuksekligi = 0
        self.kamikaze_saldirisinda = False

        self.ates_suresi = 2
        

    def kamikaze_saldirisi(self, patlamalar, p1, p2, p3):
        if not(self.kamikaze_saldirisinda) and self.kamikaze_dolum_suresi >= 60:
            if self.yerden_yukseklik > 10:
                self.hiz = 10 * (200//self.yerden_yukseklik + 1)
                self.kamikaze_saldirisinda = True
                self.kamikaze_saldirisi_yuksekligi = self.yerden_yukseklik * self.kamikaze_saldiri_gucu
        if self.kamikaze_saldirisinda:
            if self.yerden_yukseklik <= 5:
                self.yerden_yukseklik = 0
                patlamalar.append(Patlama(self.x, self.y, int(self.kamikaze_saldirisi_yuksekligi), int(self.kamikaze_saldirisi_yuksekligi), 0, 0, self.kamikaze_saldirisi_yuksekligi, p1, p2, p3))
                pygame.mixer.find_channel().play(patlama_sesi)
                self.kamikaze_saldirisinda = False
                self.hiz = 10
                self.kamikaze_dolum_suresi = 0
            else:
                self.yerden_yukseklik *= 0.5

    def ates_et(self, pencere, muhtemel_hedefler):
        if self.ates_suresi < 1:
            self.ates_suresi += 1
        else:
            if self.sagb:#eğer obje sağa bakıyorsa sağa bakarkenki halini çiz
                Mermi(pencere, self.x + self.genislik*0.5, self.y - self.yerden_yukseklik, uniform(self.x + self.yerden_yukseklik + 100, self.x + self.yerden_yukseklik * 2 + 100), uniform(self.y - 10, self.y + 10), self.hasar, muhtemel_hedefler)
            elif self.solb:
                Mermi(pencere, self.x , self.y - self.yerden_yukseklik, uniform(self.x - self.yerden_yukseklik * 2 - 100, self.x - self.yerden_yukseklik - 100), uniform(self.y, self.y + 10), self.hasar, muhtemel_hedefler)
            elif self.asab:
                Mermi(pencere, self.x , self.y - self.yerden_yukseklik, uniform(self.x - 10, self.x + 10), uniform(self.y + self.yerden_yukseklik + 100, self.y + self.yerden_yukseklik * 2 + 100), self.hasar, muhtemel_hedefler)
            elif self.yukb:
                Mermi(pencere, self.x , self.y - self.yerden_yukseklik - self.yukseklik*0.5, uniform(self.x - 10, self.x + 10), uniform(self.y - self.yerden_yukseklik * 2 - 100, self.y - self.yerden_yukseklik - 100), self.hasar, muhtemel_hedefler)
            self.ates_suresi = 0


class Patlama(Hareketli_Obje):
    def __init__(self, x, y, genislik, yukseklik, can, hiz, guc, p1, p2, p3):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        Hareketli_Obje.__init__(self, x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
        self.guc = guc
        self.patlama_suresi = 30

        #patlama büyüklüğümü hesaplayıp oranlama
        self.p1 = pygame.transform.scale(p1, (self.genislik, self.genislik))
        self.p2 = pygame.transform.scale(p2, (self.genislik, self.genislik))
        self.p3 = pygame.transform.scale(p3, (self.genislik, self.genislik))

    def hasar_ver(self, objeler):
        for obje in objeler:#bütün objeleri tek tek alttaki testten geçirip gerekirse hasar vereceğiz
            if mesafe((self.x, self.y), (obje.x, obje.y)) < self.genislik * 5/4:#patlama alanı patlamanın genişliğinin 125% kadarı olacak
                obje.can -= self.guc * self.genislik/(mesafe((self.x, self.y), (obje.x, obje.y))+1)#objeden oranla can azaltmak
        self.patlama_suresi -= 1#patlama süresini 1 azaltmak
        return
    def ana_ekrana_ciz(self, pencere):
        if self.patlama_suresi > 20:
            pencere.blit(self.p1, (self.x - self.genislik/2, self.y - self.yukseklik/2))
        elif self.patlama_suresi > 10:
            pencere.blit(self.p2, (self.x - self.genislik/2, self.y - self.yukseklik/2))
        else:
            pencere.blit(self.p3, (self.x - self.genislik/2, self.y - self.yukseklik/2))
        return

class Tank(Hareketli_Obje):
    def __init__(self, x, y, genislik, yukseklik, can, hiz):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        Hareketli_Obje.__init__(self, x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
        self.dusurdu = False

    def sayi_dusur(self, sayac):
        if not(self.dusurdu) and self.can <= 0:
            sayac -= 1
            self.dusurdu = True
            return sayac
        return sayac

    def ana_ekrana_ciz(self, pencere, r0, r1, r2, r3):
        if self.can > 0:
            pencere.blit(r0, (self.x - self.genislik/2, self.y - self.yukseklik/2))
        else:
            pencere.blit(choice([r1, r2, r3]), (self.x - self.genislik/2, self.y - self.yukseklik/2))
        return






patlamalar = []
askerler = []
tanklar = []
zeminler = []

absol = pygame.image.load("Adambot_Sol.png").convert_alpha()
absag = pygame.image.load("Adambot_Sağ.png").convert_alpha()
abasa = pygame.image.load("Adambot_Aşağı.png").convert_alpha()
abyuk = pygame.image.load("Adambot_Yukarı.png").convert_alpha()

absolg = pygame.image.load("Adambot_Sol_Gölge.png").convert_alpha()
absagg = pygame.image.load("Adambot_Sağ_Gölge.png").convert_alpha()
abasag = pygame.image.load("Adambot_Aşağı_Gölge.png").convert_alpha()
abyukg = pygame.image.load("Adambot_Yukarı_Gölge.png").convert_alpha()

abbuyukluk = 50

absol = pygame.transform.scale(absol, (abbuyukluk, abbuyukluk))
absag = pygame.transform.scale(absag, (abbuyukluk, abbuyukluk))
abasa = pygame.transform.scale(abasa, (abbuyukluk, abbuyukluk))
abyuk = pygame.transform.scale(abyuk, (abbuyukluk, abbuyukluk))
absolg = pygame.transform.scale(absolg, (abbuyukluk, abbuyukluk))
absagg= pygame.transform.scale(absagg, (abbuyukluk, abbuyukluk))
abasag = pygame.transform.scale(abasag, (abbuyukluk, abbuyukluk))
abyukg = pygame.transform.scale(abyukg, (abbuyukluk, abbuyukluk))

adambot = Adambot(400, 400, abbuyukluk, abbuyukluk, 1000, 10, 300, 1)

patlama1 = pygame.image.load("Patlama1.png").convert_alpha()
patlama2 = pygame.image.load("Patlama2.png").convert_alpha()
patlama3 = pygame.image.load("Patlama3.png").convert_alpha()

duran_tank = pygame.image.load("tank.png").convert_alpha()
patlamis_tank1 = pygame.image.load("Tank_patlamış1.png").convert_alpha()
patlamis_tank2 = pygame.image.load("Tank_patlamış2.png").convert_alpha()
patlamis_tank3 = pygame.image.load("Tank_patlamış3.png").convert_alpha()

duran_tank = pygame.transform.scale(duran_tank, (100, 100))
patlamis_tank1 = pygame.transform.scale(patlamis_tank1, (100, 100))
patlamis_tank2 = pygame.transform.scale(patlamis_tank2, (100, 100))
patlamis_tank3 = pygame.transform.scale(patlamis_tank3, (100, 100))

fayans = pygame.image.load("Zemin_Fayansı.png").convert_alpha()
tank_fayansi = pygame.image.load("Tank_Fayansı.png").convert_alpha()


baslama_dugmesi = Dugme(monitor_buyuklugu[0]//4, int(monitor_buyuklugu[1]*0.6875), monitor_buyuklugu[0]//2, int(monitor_buyuklugu[1]*0.1875), (150, 150, 150), "Basla")
gorev_yazisi = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2, int(monitor_buyuklugu[1]*0.0375), "Gorev: Hammerman\'in acikhava tank hangarini yok et.")
gorev_yazisi0 = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2 - int(monitor_buyuklugu[1]*0.0375*2), int(monitor_buyuklugu[1]*0.0375), "Tanklar solda olacak.")
gorev_yazisi1 = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2 - int(monitor_buyuklugu[1]*0.0375*4), int(monitor_buyuklugu[1]*0.0375), "Kamikaze saldirisi icin yuksel ve bosluga bas.")
gorev_yazisi2 = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2 - int(monitor_buyuklugu[1]*0.0375*6), int(monitor_buyuklugu[1]*0.0375), "Ok tuslari ile hareket et, w/s ile yuksel/alcal.")
gorev_yazisi3 = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]//2 - int(monitor_buyuklugu[1]*0.0375*8), int(monitor_buyuklugu[1]*0.0375), "E tusu ile ates et.")

asama = 0#0 menü, 1 savaş, 2 oyun sonu ekranı


clock = pygame.time.Clock()
running = True
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

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if baslama_dugmesi.tiklama_kontrolu((x, y)):
                    asama = 1
                    adambot.yerden_yukseklik = 0
                    adambot_zemini = Zemin(200, 200, 400, 400, fayans, False)
                    zeminler.append(adambot_zemini)
                    zeminler.append(Zemin(-2200, -200, 1400, 3900, tank_fayansi, False))
                    #tank_zemini = Zemin(0, 0, monitor_buyuklugu[0], monitor_buyuklugu[1], fayans, False)
                    for i in range(10):
                        for j in range(5):
                            tanklar.append(Tank(-2000 + i * 100, j * 70, 100, 100, 500, 0))
                    tank_sayisi = len(tanklar)
                    gorev_yazisi = Yazi(monitor_buyuklugu[0]//2, 60, 30, "Kalan tank sayisi: " + str(tank_sayisi))
                    pygame.mixer.find_channel().play(muzik, -1)
        if basilan_tuslar[pygame.K_ESCAPE] or not(running):
            break
        
        
    elif asama == 1:
        basilan_tuslar = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if basilan_tuslar[pygame.K_ESCAPE] or not(running):
            break

        if basilan_tuslar[pygame.K_RIGHT]:
            adambot.sagb = True
            adambot.solb = False
            adambot.sagg = True
            adambot.solg = False
        elif basilan_tuslar[pygame.K_LEFT]:
            adambot.sagb = False
            adambot.solb = True
            adambot.sagg = False
            adambot.solg = True
        else:
            adambot.sagg = False
            adambot.solg = False
            if adambot.yukb or adambot.asab:
                adambot.sagb, adambot.solb = False, False
        if basilan_tuslar[pygame.K_UP]:
            adambot.yukb = True
            adambot.asab = False
            adambot.yukg = True
            adambot.asag = False
        elif basilan_tuslar[pygame.K_DOWN]:
            adambot.yukb = False
            adambot.asab = True
            adambot.yukg = False
            adambot.asag = True
        else:
            adambot.yukg = False
            adambot.asag = False
            if adambot.sagb or adambot.solb:
                adambot.yukb, adambot.asab = False, False
        if basilan_tuslar[pygame.K_SPACE] or adambot.kamikaze_saldirisinda:
            adambot.kamikaze_saldirisi(patlamalar, patlama1, patlama2, patlama3)
        if basilan_tuslar[pygame.K_w] and not(adambot.kamikaze_saldirisinda):
            if adambot.yerden_yukseklik + adambot.hiz <= 200:
                adambot.yerden_yukseklik += adambot.hiz
        if basilan_tuslar[pygame.K_s] and not(adambot.kamikaze_saldirisinda):
            if adambot.yerden_yukseklik - adambot.hiz >= 0:
                adambot.yerden_yukseklik -= adambot.hiz

        

        
        adambot.hareket_et()
        adambot.kamikaze_dolum_suresi += 1
        if not(adambot.x < monitor_buyuklugu[0]*3/4 and adambot.x > monitor_buyuklugu[0]/4):
            if adambot.x > monitor_buyuklugu[0]*3/4:
                adambot.x -= adambot.hiz
                for patlama in patlamalar:
                    patlama.x -= adambot.hiz
                for tank in tanklar:
                    tank.x -= adambot.hiz
                for zemin in zeminler:
                    zemin.x -= adambot.hiz
            if adambot.x < monitor_buyuklugu[0]/4:
                adambot.x += adambot.hiz
                for patlama in patlamalar:
                    patlama.x += adambot.hiz
                for tank in tanklar:
                    tank.x += adambot.hiz
                for zemin in zeminler:
                    zemin.x += adambot.hiz
        if not(adambot.y + adambot.yerden_yukseklik < monitor_buyuklugu[1]*3/4 and adambot.y > monitor_buyuklugu[1]/4):
            if adambot.y > monitor_buyuklugu[1]*3/4:
                adambot.y -= adambot.hiz
                for patlama in patlamalar:
                    patlama.y -= adambot.hiz
                for tank in tanklar:
                    tank.y -= adambot.hiz
                for zemin in zeminler:
                    zemin.y -= adambot.hiz
            if adambot.y - adambot.yerden_yukseklik < monitor_buyuklugu[1]/4:
                adambot.y += adambot.hiz
                for patlama in patlamalar:
                    patlama.y += adambot.hiz
                for tank in tanklar:
                    tank.y += adambot.hiz
                for zemin in zeminler:
                    zemin.y += adambot.hiz

        for zemin in zeminler:
            zemin.ana_ekrana_ciz(ana_pencere)
        for tank in tanklar:
            tank_sayisi = tank.sayi_dusur(tank_sayisi)
            tank.ana_ekrana_ciz(ana_pencere, duran_tank, patlamis_tank1, patlamis_tank2, patlamis_tank3)
        adambot.golge_ciz(ana_pencere, absagg, absolg, abasag, abyukg)
        for patlama in patlamalar:
            if patlama.patlama_suresi <= 0:
                patlamalar.remove(patlama)
                continue
            else:
                patlama.hasar_ver(tanklar)
                patlama.ana_ekrana_ciz(ana_pencere)
                
        if basilan_tuslar[pygame.K_e]:
            adambot.ates_et(ana_pencere, tanklar)
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
