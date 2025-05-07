import os, shutil, time, random
import webbrowser as wb

print("Sie starten Fehleranalyse V4.3.1!")

BPATH = "./programdata/buero"

def fehlerbehebung(Id:str, *arg):
    global versio
    print("Error#"+Id, "Debug:", arg)
    print("Fehler wird behoben...")
    try:
        match Id:
            case "F!!1":
                print("Ihre Ordnerstruktur ist fehlerhaft! Wenden Sie sich an den Kundenservice und installieren Sie ggf. alle Pakete neu.")
                raise SystemError()
            case "Mod!1":
                os.system("-m pip install pycols")
            case "I1":
                os.mkdir("./images")
            case "Mu1!":
                os.mkdir("./music")
            case "U!1":
                print("Ihre Update-Programme sind fehlerhaft! Installieren Sie update.py und systemupdate.py erneut")
                raise SystemError()
            case "BÃ¼!1":
                print("Ihr bueroUtils.py ist fehlerhaft. Installieren Sie die neueste BÃ¼ro-Version manuell.")
                raise SystemError()
            case "BÃ¼!!!2":
                print("Ihre BÃ¼ro-Datei fehlt! Installieren Sie die neueste Version manuell neu.")
                raise SystemError()
            case "Ad1":
                os.mkdir("./programdata/ads")
            case "LKim1":
                os.mkdir("./programdata/lkims")
            case "LKim2!":
                os.mkdir("./programdata/achievements")
            case "Wn!1":
                os.mkdir("./programdata/win")
            case "Rn!1":
                os.mkdir("./programdata/run")
            case "V1":
                for l in installiert+["System"]:
                    with open(BPATH+"/versioninfo_" + l + ".txt", "a") as file:
                        file.write("(zurÃ¼ckgesetzt-installieren Sie ein Update)")
            case "V2":
                with open(BPATH+"/versioninfo.txt", "a") as file:
                    file.write("0.0.0")
            case "V3":
                for i in arg[0]:
                    os.remove(BPATH+"/versioninfo_"+i+".txt")
            case "PIN!1":
                with open(BPATH+"/PIN_opt.txt", "x") as PIN_opt:
                    PIN_opt.write("True")
            case "PIN!2":
                with open(BPATH+"/PIN_l.txt", "x") as PIN_l:
                    PIN_l.write("8")
            case "PIN!3":
                a = input("Authentifizierung erforderlich (abbr = Abbrechen): ")
                if a != "abbr":
                    random.seed(int())
                    with open(BPATH+"/PIN.txt", "r") as f:
                        if str(random.randint(1, 10**30)) == f.read():
                            default = str(random.randint(1, 10**32-1))
                            random.seed(int(input(f"Neuen WiederherstellungsschlÃ¼ssel mit 32 Stellen erstellen [Default: {default}]: ") or default))
                            with open(BPATH+"/restore.txt", "w") as f2:
                                f2.write(str(random.randint(1, 10**40)))
                        else:
                            print("Authentifizierung fehlgeschlagen."); time.sleep(0.5); raise SystemError()
                else:
                    print("Ignorieren Sie die folgende Meldung und fahren Sie weiter wie zuvor."); time.sleep(0.5); raise SystemError()
            case "Lg1":
                with open(BPATH+"/log.txt", "w") as lg:
                    lg.write("False")
            case "Tp1":
                with open(BPATH+"/tipps.txt", "x", encoding="utf-8") as f:
                    f.write("Wussten Sie schon, dass Sie FunktionsvorschlÃ¤ge einsenden kÃ¶nnen?")
            case "AGB1":
                with open(BPATH+"/agb.txt", "x") as f:
                    f.write("False")
            case "COL!1":
                with open(BPATH+"/color.txt", "x") as f:
                    for i in range(5):
                        f.write("WHITE#*#")
            case "MEN!1":
                with open(BPATH+"/menu.txt", "x") as f:
                    f.write("")
            case "ACH!!1":
                with open(BPATH+"/achievements.txt", "x", encoding="utf-8") as f:
                    f.write("0#*#")
            case "UID!!1":
                with open(BPATH+"/username.txt", "x", encoding="utf-8") as f:
                    f.write("RANDOM_NAME_WITH_PROFILE_"+str(random.randint(10**5, 10**6-1)))
            case "DVID!!1":
                with open(BPATH+"/devid.txt", "x", encoding="utf-8") as f:
                    f.write(versio.split(".")[0]+"-"+str(random.randint(10000, 99999))+"-"+versio.split(".")[1]+"."+versio.split(".")[2])
            case "DVID!!2":
                with open(BPATH+"/deviceidstatic.txt", "x", encoding="utf-8") as f:
                    f.write("False")
            case "Db!1":
                os.mkdir(BPATH+"/debug")
            case "UF1":
                shutil.rmtree("./programdata/update")
                os.mkdir("./programdata/update")
            case "MF1":
                os.mkdir("./programdata/mail/sent")
            case "BF1":
                with open("./programdata/bank/konto.txt", "x", encoding="utf-8") as f:
                    f.write("0.00")
            case "LTP!1":
                os.mkdir("./programdata/ltp")
            case "GF!1":
                os.mkdir("./programdata/goodFood")
            case _:
                print("Unbekannte ID")
                raise SystemError()
        print("Fehler erfolgreich behoben...")
    except:
        print("Fehlerbehebung gescheitert...\nSenden Sie die Fehler-ID sowie die Debug-Informationen (s.o. sowie ggf, DebugLogs) an den Kundenservice...")
        print("Eventuell lÃ¶st ein Update all Ihrer Pakete das Problem. Doppelklicken Sie auf bueroUtils.py...")

print("Fehlersuche initiieren...")

installiert = []
files = os.listdir()
if "verschlÃ¼sseln.py" in files:
    installiert.append("VerschlÃ¼sseler")
if "Haustier.py" in files:
    installiert.append("Haustier")
if "Ballonfahrt.py" in files and "Ballonfahrt-M2_1.py" in files and "Ballonfahrt-M2_2.py" in files:
    installiert.append("Ballonfahrt")
if "SchingSchangSchongIntelligent.py" in files:
    installiert.append("SchingSchangSchongIQ")
if "abstrakt.py" in files:
    installiert.append("abstrakte Verzerrung")
if "quest.py" in files and "level-editor.py" in files:
    installiert.append("im Verlies")
if "Passwortgenerator.py" in files:
    installiert.append("Passwortgenerator")
if "Musik.py" in files:
    installiert.append("Musik")
if "Garten-im-GlÃ¼ck.py" in files:
    installiert.append("Garten im GlÃ¼ck")
if "lebensmittel.py" in files:
    installiert.append("Lebensmittel")
if "quiz.py" in files:
    installiert.append("Das groÃŸe Quiz")
if "Rechnung.pyw" in files:
    installiert.append("Rechnungen")
if "mail.py" in files and "mail_agent.pyw" in files:
    installiert.append("BÃ¼roMail")
if "bank.py" in files:
    installiert.append("BÃ¼roBank")
if "ltp_agent.py" in files:
    installiert.append("LTP Agent")
if "bonus.py" in files:
    installiert.append("BÃ¼roBonus")
if "ritter_launcher.py" in files:
    installiert.append("Die Ritter - Launcher")
if "kaffee.py" in files:
    installiert.append("Kaffee Manager")
if "goodFood.py" in files:
    installiert.append("GoodFood")
print(f"Installierte Pakete: {str(installiert)}")

try:
    import pycols
except:
    fehlerbehebung("Mod!1")
try:
    startfile = os.listdir("./")
    prdata = os.listdir("./programdata")
    bdata = os.listdir(BPATH)
    tempfile = os.listdir("./programdata/update")
except:
    print("Error#F!!1 ist aufgetreten! Senden Sie diese Information sofort an den Kundenservice!")
print("Initialisierung abgeschlossen")
if not "images" in startfile:
    fehlerbehebung("I1")
if not "music" in startfile:
    fehlerbehebung("Mu1!")
if not "update.py" in startfile or not "systemupdate.py" in startfile:
    fehlerbehebung("U!1")
if not "bueroUtils.py" in startfile:
    fehlerbehebung("BÃ¼!1")
if not "bÃ¼ro.py" in startfile:
    fehlerbehebung("BÃ¼!!!2")
print("Ausgangsordner untersucht...")
if not "ads" in prdata:
    fehlerbehebung("Ad1")
if not "lkims" in prdata:
    fehlerbehebung("LKim1")
if not "achievements" in prdata:
    fehlerbehebung("LKim2!")
if not "win" in prdata:
    fehlerbehebung("Wn!1")
if not "run" in prdata:
    fehlerbehebung("Rn!1")
print("Direkte Daten Ã¼berprÃ¼ft...")
error = False
for i in installiert+["System"]:
    if not "versioninfo_"+i+".txt" in bdata:
        error = True
if error:
    fehlerbehebung("V1")
y = []
for i in bdata:
    if "versioninfo_" in i:
        x = i[12:]
        x = x[0:len(x)-4]
        if x not in installiert+["System"]:
            y.append(x)
if len(y) != 0:
    fehlerbehebung("V3", y)
if "versioninfo.txt" not in bdata:
    fehlerbehebung("V2")
    versio = "0.0.0"
else:
    with open(BPATH+"/versioninfo.txt", "r", encoding="utf-8") as f:
        versio = f.read()
if "debug" not in bdata:
    fehlerbehebung("Db!1")
if "PIN_opt.txt" not in bdata:
    fehlerbehebung("PIN!1")
if "PIN_l.txt" not in bdata:
    fehlerbehebung("PIN!2")
if "log.txt" not in bdata:
    fehlerbehebung("Lg1")
if "tipps.txt" not in bdata:
    fehlerbehebung("Tp1")
if "agb.txt" not in bdata:
    fehlerbehebung("AGB1")
if "color.txt" not in bdata:
    fehlerbehebung("COL!1")
if "menu.txt" not in bdata:
    fehlerbehebung("MEN!1")
if "achievements.txt" not in bdata:
    fehlerbehebung("ACH!!1")
if "username.txt" not in bdata:
    fehlerbehebung("UID!!1")
if "devid.txt" not in bdata:
    fehlerbehebung("DVID!!1")
if "deviceidstatic.txt" not in bdata:
    fehlerbehebung("DVID!!2")
if "restore.txt" not in bdata:
    fehlerbehebung("PIN!3")
print("BÃ¼rospezifische Daten und gespeicherte Einstellungen Ã¼berprÃ¼ft...")
if not tempfile == []:
    fehlerbehebung("UF1", tempfile)
print("Updateordner und temporÃ¤re Dateien Ã¼berprÃ¼ft...")
if "BÃ¼roMail" in installiert:
    if not "sent" in os.listdir("./programdata/mail"):
        fehlerbehebung("MF1")
print("BÃ¼roMail-Daten Ã¼berprÃ¼ft...")
if "BÃ¼roBank" in installiert:
    if not "konto.txt" in os.listdir("./programdata/bank"):
        fehlerbehebung("BF1")
print("BÃ¼roBank-Daten Ã¼berprÃ¼ft...")
if "LTP Agent" in installiert:
    if not "ltp" in prdata:
        fehlerbehebung("LTP!1")
if "GoodFood" in installiert:
    if not "goodFood" in prdata:
        fehlerbehebung("GF!1")
print("Weitere Daten geprÃ¼ft...")

anl = input("Haben Sie ein weiteres Anliegen? Sie kÃ¶nnnen es hier eingeben (z.B. PIN vergessen, Erfolge fehlen, Debug-Log Ã¼bermitteln, Specials fehlen, WiederherstellungsschlÃ¼ssel Ã¤ndern ...): ")
if anl == "PIN vergessen":
    anl = input("Ihre PIN wird nach einer IdentitÃ¤tsbestÃ¤tigung zurÃ¼ckgesetzt.\nWollen Sie fortfahren (j/n)? ")
    if anl == "j":
        print("Bitte identifizieren Sie sich per Mail und geben Sie die LÃ¤nge Ihrer PIN ein.")
        time.sleep(0.4)
        with open(BPATH+"/PIN_l.txt", "r") as f:
            l = f.read()
        if not l == input("PIN-LÃ¤nge eingeben: "):
            print("Falsche Eingabe!!!")
            time.sleep(3)
            raise ValueError("Falsche Eingabe!")
        print("Identifizierung per Mail lÃ¤uft...")
        time.sleep(3.5)
        wb.open("mailto:leander@kafemann.berlin?subject=PIN vergessen&body=Ich bestÃ¤tige mein Anliegen hiermit und schlieÃŸe jegliche Haftung Ihrerseits aus.")
        time.sleep(2)
        input("Ein WiederherstellungsschlÃ¼ssel ist erforderlich.")
        random.seed(int(input("WiederherstellungsschlÃ¼ssel eingeben: ")))
        with open(BPATH+"/restore.txt", "r") as f:
            if not f.read() == str(random.randint(1, 10**40)):
                print("Dieser WiederherstellungsschlÃ¼ssel ist inkorrekt."); time.sleep(2.5)
                raise ValueError("Inkorrekter Code")
        os.remove("./programdata/buero/PIN.txt")
        print("PIN erfolgreich zurÃ¼ckgesetzt.")
elif anl == "Debug-Log Ã¼bermitteln":
    x = input("Soll das neueste DebugLog Ã¼bermittelt werden oder wollen Sie eines auswÃ¤hlen (neu/Zeit)")
    dblist = list(os.listdir(BPATH+"/debug"))
    dblist.sort()
    if x == "neu":
        path = "./programdata/buero/debug/"+dblist[-1]
    else:
        y = ["Bitte geben Sie", "erst einen Wert an"]
        while len(y) != 1:
            zeit = input("Bitte geben Sie einen Zeitpunkt(so genau wie mÃ¶glich) an (Format: JJJJ-MM-TT-SS-MM-SS). MÃ¶glich:"+str(y))
            y = []
            for i in dblist:
                if zeit in i:
                    y.append(i)
        path = BPATH+"/debug/"+y[0]
    shutil.copy(path, './debugLog.txt')
    wb.open("mailto:leander@kafemann.berlin?subject=DebugLog&body=Ich mÃ¶chte Ihnen hiermit mein DebugLog senden. [Bitte fÃ¼gen Sie eine Beschreibung des Fehlers und das DebugLog (im BÃ¼ro-Ordner) hinzu]")
elif anl == "Erfolge fehlen" or anl == "Specials fehlen" or anl == "Gewinnspiele fehlen":
    print("Sie kÃ¶nnen neue Erfolge/Specials Ã¼ber die Anfordern-Funktion erhalten, indem Sie alle bzw. die fehlenden angeben.")
    x = input("Wollen Sie die neuen Erfolge/Specials/Gewinnspiele jetzt installieren (j/n)?")
    if x == "j":
        input("DrÃ¼cken Sie Enter, wenn Sie alle Erfolge/Specials/Gewinnspiele hier (in diesem Ordner) gespeichert haben.")
        count = 0
        for i in os.listdir("./"):
            if i.endswith(".lkim"):
                if not "Special" in i:
                    try:
                        os.remove("./programdata/achievements/"+i)
                    except:
                        print("einen neuen Erfolg entdeckt")
                    finally:
                        shutil.move("./"+i, "./programdata/achievements/"+i)
                        count += 1
                else:
                    shutil.move("./"+i, "./programdata/lkims/"+i)
                    count += 1
            elif "z!" in i and i.endswith(".txt"):
                shutil.move("./"+i, "./programdata/win/"+i)
        print(count, "Erfolge erfolgreich implementiert.")
elif anl == "WiederherstellungsschlÃ¼ssel Ã¤ndern":
    random.seed(int(input("Authentifizierung erforderlich: "))); time.sleep(0.2)
    with open(BPATH+"/PIN.txt", "r") as f:
        if str(random.randint(1, 10**30)) == f.read():
            default = str(random.randint(1, 10**32-1))
            random.seed(int(input(f"Neuen WiederherstellungsschlÃ¼ssel mit 32 Stellen erstellen [Default: {default}]: ") or default))
            with open(BPATH+"/restore.txt", "w") as f2:
                f2.write(str(random.randint(1, 10**40)))
        else:
            print("Authentifizierung fehlgeschlagen."); time.sleep(1)
print("Falls Ihr Anliegen nicht behoben werden konnte, Ã¼berprÃ¼fen Sie die Installation sowie Ihre Netzwerkverbindung und installieren Sie die Pakete gegebenenfalls neu."); time.sleep(0.5)
print("Wir sind auch Ã¼ber unseren Kundenservice erreichbar."); time.sleep(0.2)
print("Vorgang wird abgeschlossen (drÃ¼cken Sie Strg+c, um das Programm zu beenden)...")
time.sleep(2)
