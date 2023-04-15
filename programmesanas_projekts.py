dat=['19.06.1919','18.11.1918','17.06.1940','14.06.1940','25.03.1949','14.06.1987 - 06.09.1991','04.05.1990','13.01.1991 - 27.01.1991','23.08.1939','23.08.1989','17.03.1944','14.11.1922','08.04.1927','09.04.1930','11.04.1936','07.07.1993','08.07.1999','08.07.2007','08.07.2011','08.07.2015','08.07.2019'']
notik=["Cēsu kaujas",'Latvijas Republikas proklamēšanas diena','Latvijas Republikas okupācijas diena','1941. gada jūnija deportācijas Latvijā','1949. gada 25. marta deportācija Latvijā','Dziesmotā revolūcija','Latvijas Republikas Neatkarības atjaunošanas diena','Barikāžu laiks','Molotova-Ribentropa pakts','Baltijas ceļš','Nacionālās pretošanās kustības piemiņas diena','Jānis Čakste','Gustavs Zemgals','Alberts Kviesis','Kārlis Ulmanis','Guntis Ulmanis','Vaira Vīķe-Freiberga','Valdis Zatlers','Andris Bēŗziņš','Raimonds Vējonis','Egils Levits']
notikaprak=['Cēsu kaujas bija viens no nozīmīgākajiem pavērsiena punktiem Latvijas Neatkarības kara gaitā. Kaujas noslēdzās ar Igaunijas armijas un Ziemeļlatvijas brigādes pārliecinošu uzvaru.','Latvijas Tautas padomes (LTP) formāls solis 1918. gada 18. novembrī, ar kuru suverēnā valsts vara Latvijā pārgāja LTP rokās un tika dibināta neatkarīga valsts','Latvijas valdība bija spiesta pakļauties PSRS ultimātam, un 17.06. rītā padomju karaspēks šķērsoja Latvijas robežu un ieņēma visus stratēģiski svarīgos punktus.','14.06.1941. vairāk nekā 15 400 Latvijas pilsoņu deportēja no Latvijas. Daļu no deportētajiem uzreiz arestēja un nogādāja ieslodzījuma vietās. Pārējos nometināja Sibīrijā un Kazahstānā. Tā bija pirmā masu deportācija no Latvijas.','25.03.1949. Latvijā, Lietuvā un Igaunijā sākās deportācijas akcija “Krasta banga”, kuras laikā 42 125 Latvijas iedzīvotājus izsūtīja mūža nometinājumā uz Sibīriju.','Dziesmotā revolūcija jeb Trešā Atmoda bija laika posms Baltijas valstu (Latvija, Lietuva, Igaunija) vēsturē starp 1986. un 1991. gadu, kas beidzās ar pilnīgu valstiskās neatkarības atjaunošanu visās trijās valstīs.','1990. gada 4. maijā Latvijas PSR Augstākā Padome pieņēma deklarāciju par Latvijas Republikas neatkarības atjaunošanu, kā arī noteica pārejas posmu no Latvijas Republikas Augstākās Padomes līdz Saeimas sasaukšanai.','Barikāžu laiks ir vēsturisks apzīmējums 1990. gada 4. maijā atjaunotās Latvijas Republikas aizsardzības pasākumiem, kas tika organizēti Rīgā un citās Latvijas pilsētās no 1991. gada 13. līdz 27. janvārim.','Molotova-Ribentropa pakts bija neuzbrukšanas līgums starp Vāciju un Padomju Sociālistisko Republiku Savienību (PSRS), kas radīja priekšnoteikumus padomju un vācu agresijai kaimiņvalstīs.','Akcijas mērķis bija pievērst vietējās un starptautiskās sabiedrības uzmanību nelikumīgajiem apstākļiem, kādos Baltijas valstis tika pievienotas PSRS, akcentējot 23.08.1939. noslēgtā Molotova–Ribentropa pakta izšķirošo nozīmi turpmākajā Baltijas okupācijā. Cauri visām trim Baltijas valstīm dzīvā ķēdē sastājās miljoniem cilvēku.','1944. gada 17. martā Konstantīna Čakstes vadītā Latvijas Centrālā padome pabeidza parakstu vākšanu memorandam, kurā pieprasīta Latvijas valsts neatkarības faktiska atjaunošana.','Jānis Čakste tiek ievēlēts par pirmo Latvijas Valsts prezidentu.','Gustavs Zemgals tiek ievēlēts par otro Latvijas Valsts prezidentu.','Alberts Kviesis tiek ievēlēts par trešo Latvijas Valsts prezidentu.','Kārlis Ulmanis tiek ievēlēts par ceturto Latvijas Valsts preizdentu, bet vēsturnieki Ulmani vairs neuzskata kā prezidentu, bet gan kā prezidenta aizvietotāju.','Guntis Ulmanis tiek ievēlēts par Latvijas Valsts prezidentu.','Vaira Vīķe-Freiberga tiek ievēlēta par Latvijas Valsts prezidenti.','Valdis Zatlers tiek ievēlēts par Latvijas Valsts prezidentu.','Andris Bērziņš tiek ievēlēts par Latvijas Valsts prezidentu.','Raimonds Vējonis tiek ievēlēts par Latvijas Valsts prezidentu.','Egils Levits tiek ievēlēts par Latvijas Valsts prezidentu.']
a=(input("Ievadi datumu(dd.mm.gggg) vai notikumu(piem. Cēsu kaujas) par kuru vēlies uzzināt! - "))
if a in dat:
    print(notik[dat.index(a)])
    while True:
        jane=(input("Vai vēlies uzzināt vairāk par šo notikumu? Ievaid 'Jā' vai 'Nē'!"))
        if jane == 'Jā':
            print(notikaprak[dat.index(a)])
            break
        if jane == 'Nē':
            break
elif a in notik:
    print(dat[notik.index(a)])
    while True:
        jane=(input("Vai vēlies uzzināt vairāk par šo notikumu? Ievaid 'Jā' vai 'Nē'!"))
        if jane == 'Jā':
            print(notikaprak[notik.index(a)])
            break
        if jane == 'Nē':
            break        
else:
    print("Datums nav atbilstošs, mēģini to ievadīt vēlreiz.")
