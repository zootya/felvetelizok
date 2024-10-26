# felvetelizok
Beadandó 2025.01.05 -ig

# Feladatmeghatározás
Backend 1. beadandó feladat
Felvételizők
Készíts Django alkalmazást, amelyben felvételizők adatai tárolhatók!
    1. Hozd létre a virtuális környezetet, majd aktiváld, és telepítsd a Django-t!
    2. Hozz létre új django projektet „config” néven!
    3. Hozz lére új appot a projekten belül „felviadmin” néven! Add hozzá a projektet a settings-hez!
    4. A migrate segítségével hozd létre az alap adatbázisokat, majd hozd létre a superusert „admin” felhasználónévvel és jelszóval!
    5. Hozz létre két adatmodellt:
        a. Felvetelizo(név: szöveg, szul_ev:szám,pontszám: egész szám, szak: idegen kulcs a másik táblára)
        b. Szak(szakNev: szöveg) Nem kötelező, plusz feladat: Egészítsd ki a Szak modellt még egy mezővel, amely logikai típusú, és azt jelzi, hogy államilag támogatott-e vagy nem! Ha ezt megoldod, akkor később jelenjen meg ez is a táblázatban!
    6. A modelleket regisztráld az admin felületén!
    7. Az adatmodelleket a makemigrations és a migrate segítségével hozd létre ténylegesen az adatbázisban! Vigyél fel legalább 2 szakot és legalább 2 felvételiző adatát az admin felület segítségével!
    8. Készíts view-t az app-on belül index néven, amely az index.html szerver oldali renderélést oldja meg! Paraméterként kapja meg mindkét modell összes adatát!
    9. Készíts URL-t, amely az előbbi view függévnyét hívja meg! Az url elérési útvonala legyen pl. 127.0.0.1:8000/felviadmin/	(Tehát a projekt url-jében a felviadmin importálja be az app összes url-jét, a felviadmin app pedig az üres ’’ url-hez rendelje hozzá, mint ahogy órán is megoldottuk)
    10. Készítsd el a template-et, amely megjeleníti táblázatban a felvételiző nevét, születési évét, pontszámát, a szak nevét) A template-hez készíts statikus CSS-t is, amelyben néhány alap formázás található a táblázattal és az oldallal!
A feladat további részét már önállóan, az órai minták alapján kell elkészítened, amelyek a következőt tegyék (az URL-eket, view nevét saját magad meghatározhatod):
    11. Lehessen új felvételiző adatát felvinni! A felvitelnél a szak nevét legördülő listából lehessen választani! A bevitel után frissüljön a megjelenített táblázat is!
    12. Lehessen felvételiző adatát törölni! A törlés megoldása rád van bízva, lehet URL segítségével vagy űrlap POST segítségével is!
Feladat beadása: Az include, lib és scripts mappák nem kellenek, csak a django állományai, mint ahogy órán is feltettem a feladatokat. A teljes projektet tömörítsd be zip-be és úgy töltsd fel!