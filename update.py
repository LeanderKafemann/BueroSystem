"""
Skript zum Installieren von Updates/-grades fÃ¼r BÃ¼ro.
"""
def update(alter="Update", pStart=False):
    """
    Update: vorhandenes Paket wird upgedatet
    Upgrade: Paket wird neu installiert
    pStart: update wurde manuell (nicht Ã¼ber BÃ¼ro) gestartet
    """
    import os, shutil, zipfile
    from tkinter.filedialog import askopenfilename
    import bueroUtils as b

    bÃ¼ = b.bueroUtils(packageName="Update")
    py = bÃ¼.importPyautoguiCatched()

    dLg = bÃ¼.dLg
    C_, C, T = bÃ¼.get_colors()
    s = bÃ¼.status("Updatevorgang", 48, 8, parts=6, colors=C, tcolors=T)
    s.send_message(" #initialisieren")
    #Initialisierung
    s.send_message(" #Pakete prÃ¼fen")
    addlist, installiert, werkzeuge, unterhaltung, lernen, medien, plugin = bÃ¼.get_installed()
    installiert.append("BÃ¼ro")

    dLg.entrys(installiert, addlist, s, C_, C, T, alter, pStart, werkzeuge, lernen, medien, plugin, unterhaltung)

    pfad = askopenfilename(title="Zip-Datei mit Update auswÃ¤hlen", filetypes=[("ZIP comprimized folder", "*.zip")])
    tempfile = "./programdata/update"
    versiotest_ = list(pfad.split("/")[-1].rstrip(".zip").split("."))
    versiotest = versiotest_[0][-1]+"."+versiotest_[1]+"."+versiotest_[2]
    versionneu = py.prompt("Geben Sie die neu installierte Version an:", "Version angeben", versiotest)
    s.send_message(" #Update-Dateien lesen") #4.te Nachricht von 7

    dLg.entrys(pfad, versiotest_, versiotest, versionneu)

    with zipfile.ZipFile(pfad, 'r') as zip_ref:
        zip_ref.extractall(tempfile)
    print("Vorbereitung abgeschlossen.")
    if alter == "Update":
        antwort2 = py.prompt("Welches Ihrer Pakete wollen Sie updaten?\nBitte geben Sie den korrekten Paketnamen an.",\
                             "Paket auswÃ¤hlen", pfad.split("/")[-1].rstrip(".zip").rstrip(versionneu).capitalize())
        s.send_message(" #Update beginnen")
        match antwort2:
            case "VerschlÃ¼sseler":
                os.remove("./verschlÃ¼sseln.py")
                shutil.rmtree("./shopping")
                filelist = os.listdir("./programdata/verschlÃ¼sseln")
                filelist.remove("userlist.txt")
                for i in filelist:
                    os.remove("./programdata/verschlÃ¼sseln/" + i)
                shutil.move(tempfile + "/verschlÃ¼sseln.py", "./verschlÃ¼sseln.py")
                shutil.move(tempfile + "/shopping", "./shopping")
                filelist = os.listdir(tempfile + "/programdata/verschlÃ¼sseln")
                filelist.remove("userlist.txt")
                for i in filelist:
                    shutil.move(tempfile + "/programdata/verschlÃ¼sseln/" + i, "./programdata/verschlÃ¼sseln/" + i)
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_VerschlÃ¼sseler.txt", "w") as newV:
                    newV.write(versionneu)
            case "Haustier":
                os.remove("./Haustier.py")
                shutil.move(tempfile + "/Haustier.py", "./Haustier.py")
                filelist = os.listdir(tempfile + "/programdata/haustier")
                filelist.remove("saved")
                filelist.remove("aktien")
                for i in filelist:
                    shutil.rmtree("./programdata/haustier/" + i)
                    shutil.move(tempfile + "/programdata/haustier/" + i, "./programdata/haustier/" + i)
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_Haustier.txt", "w") as newV:
                    newV.write(versionneu)
            case "Ballonfahrt":
                filelist = os.listdir(tempfile + "/")
                filelist.remove("images"); filelist.remove("programdata")
                for i in filelist:
                    try:
                        os.remove("./" + i)
                    except:
                        pass
                    shutil.move(tempfile + "/" + i, "./" + i)
                filelist = os.listdir(tempfile + "/images")
                for i in filelist:
                    shutil.move(tempfile + "/images/" + i, "./images/" + i)
                shutil.rmtree(tempfile + "/images")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_Ballonfahrt.txt", "w") as newV:
                    newV.write(versionneu)
            case "SchingSchangSchongIQ":
                os.remove("./SchingSchangSchongIntelligent.py")
                shutil.move(tempfile + "/SchingSchangSchongIntelligent.py", "./SchingSchangSchongIntelligent.py")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_SchingSchangSchongIntelligent.txt", "w") as newV:
                    newV.write(versionneu)
            case "abstrakte Verzerrung":
                os.remove("./abstrakt.py")
                shutil.move(tempfile + "/abstrakt.py", "./abstrakt.py")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_abstrakte Verzerrung.txt", "w") as newV:
                    newV.write(versionneu)
            case "im Verlies":
                os.remove("./quest.py")
                os.remove("./level-editor.py")
                shutil.move(tempfile + "/quest.py", "./quest.py")
                shutil.move(tempfile + "/level_editor.py", "./level-editor.py")
                shutil.rmtree(tempfile + "/programdata")
                filelist = os.listdir(tempfile + "/images")
                for i in filelist:
                    shutil.move(tempfile + "/images/" + i, "./images/" + i)
                shutil.rmtree(tempfile + "/images")
                with open("./programdata/buero/versioninfo_im Verlies.txt", "w") as newV:
                    newV.write(versionneu)
            case "Passwortgenerator":
                os.remove("./Passwortgenerator.py")
                shutil.move(tempfile + "/Passwortgenerator.py", "./Passwortgenerator.py")
                shutil.rmtree("./programdata/password")
                shutil.move(tempfile + "/programdata/password", "./programdata/password")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_Passwortgenerator.txt", "w") as newV:
                    newV.write(versionneu)
            case "Musik":
                os.remove("./Musik.py")
                shutil.move(tempfile+"/Musik.py", "./Musik.py")
                shutil.rmtree(tempfile+"/programdata")
                with open("./programdata/buero/versioninfo_Musik.txt", "w") as newV:
                    newV.write(versionneu)
            case "Garten im GlÃ¼ck":
                os.remove("./Garten-im-GlÃ¼ck.py")
                shutil.move(tempfile+"/Garten-im-GlÃ¼ck.py", "./Garten-im-GlÃ¼ck.py")
                filelist = os.listdir(tempfile + "/images")
                for i in filelist:
                    shutil.move(tempfile + "/images/" + i, "./images/" + i)
                shutil.rmtree(tempfile + "/images")
                with open("./programdata/buero/versioninfo_Garten im GlÃ¼ck.txt", "w") as newV:
                    newV.write(versionneu)
            case "Lebensmittel":
                os.remove("./lebensmittel.py")
                shutil.move(tempfile+"/lebensmittel.py", "./lebensmittel.py")
                with open("./programdata/buero/versioninfo_Lebensmittel.txt", "w") as newV:
                    newV.write(versionneu)
            case "Das groÃŸe Quiz":
                os.remove("./quiz.py")
                shutil.move(tempfile+"/quiz.py", "./quiz.py")
                for i in os.listdir(tempfile+"/music"):
                    shutil.move(tempfile+"/music/"+i, "./music/"+i)
                shutil.rmtree(tempfile+"/music")
                with open("./programdata/buero/versioninfo_Das groÃŸe Quiz.txt", "w") as newV:
                    newV.write(versionneu)
            case "Rechnungen":
                os.remove("./Rechnung.pyw")
                shutil.move(tempfile+"/Rechnung.pyw", "./Rechnung.pyw")
                shutil.move(tempfile+"/programdata/rechnungen/rechnung.ico", "./programdata/rechnungen/rechnung.ico")
                shutil.rmtree(tempfile+"/programdata")
                with open("./programdata/buero/versioninfo_Rechnungen.txt", "w") as newV:
                    newV.write(versionneu)
            case "BÃ¼roMail":
                os.remove("./mail.py")
                os.remove("./mail_agent.py")
                shutil.move(tempfile + "/mail.py", "./mail.py")
                shutil.move(tempfile + "/mail_agent.pyw", "./mail_agent.pyw")
                for i in os.listdir(tempfile + "/programdata/mail"):
                    if "." in i:
                        shutil.move(tempfile + "/programdata/mail/"+i, "./programdata/mail/"+i)
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_BÃ¼roMail.txt", "w") as newV:
                    newV.write(versionneu)
            case "BÃ¼roBank":
                os.remove("./bank.py")
                shutil.move(tempfile + "/bank.py", "./bank.py")
                shutil.rmtree("./programdata/bank")
                shutil.move(tempfile + "/programdata/bank", "./programdata/bank")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_BÃ¼roBank.txt", "w") as newV:
                    newV.write(versionneu)
            case "LTP Agent":
                os.remove("./ltp_agent.py")
                shutil.move(tempfile + "/ltp_agent.py", "./ltp_agent.py")
                with open("./programdata/buero/versioninfo_LTP Agent.txt", "w") as newV:
                    newV.write(versionneu)
            case "BÃ¼roBonus":
                os.remove("bonus.py")
                shutil.move(tempfile + "/bonus.py", "./bonus.py")
                with open("./programdata/buero/versioninfo_BÃ¼roBonus.txt", "w") as newV:
                    newV.write(versionneu)
            case "Kaffee Manager":
                os.remove("kaffee.py")
                shutil.move(tempfile + "/kaffee.py", "./kaffee.py")
                with open("./programdata/buero/versioninfo_Kaffee Manager.txt", "w") as newV:
                    newV.write(versionneu)
            case "GoodFood":
                os.remove("goodFood.py")
                shutil.move(tempfile + "/goodFood.py", "./goodFood.py")
                with open("./programdata/buero/versioninfo_GoodFood.txt", "w") as newV:
                    newV.write(versionneu)
            case "BÃ¼ro":
                os.remove("./bÃ¼ro.py")
                os.remove("./bueroUtils.py")
                shutil.move(tempfile + "/bÃ¼ro.py", "./bÃ¼ro.py")
                shutil.move(tempfile + "/bueroUtils.py", "./bueroUtils.py")
                for i in os.listdir(tempfile):
                    if "tipps.txt" == i:
                        os.remove("./programdata/buero/tipps.txt")
                        shutil.move(tempfile+"/"+i, "./programdata/buero/tipps.txt")
                    elif ".lkim" in i:
                        if "Special" in i:
                            shutil.move(tempfile+"/"+i, "./programdata/lkims/"+i)
                        else:
                            if i in os.listdir("./programdata/achievements"):
                                os.remove("./programdata/achievements/"+i)
                            shutil.move(tempfile+"/"+i, "./programdata/achievements/"+i)
                    elif "z!" in i:
                        shutil.move(tempfile+"/"+i, "./programdata/win/"+i)
                    else:
                        shutil.move(tempfile+"/" + i, "./programdata/ads/" + i)
                with open("./programdata/buero/versioninfo.txt", "w") as newV:
                    newV.write(versionneu)
                py.alert("Bitte beachten Sie, dass Sie nach dem Updaten von BÃ¼ro ggf. zunÃ¤chst die Fehleranalyse starten sollten, um Fehler beim Bootvorgang zu vermeiden.", "Fehleranalyse")
            case _:
                py.alert("Fehlerhafter Paketname!")
                quit(code="ERROR")
        s.send_message(" #Update installieren")
        print("Installation abgeschlossen")
    elif alter == "Upgrade":
        antwort2 = py.prompt("Welches unserer Pakete mÃ¶chten Sie neu hinzufÃ¼gen?\nBitte geben Sie den korrekten Namen an.",\
                             "Upgrade", pfad.split("/")[-1].rstrip(".zip").rstrip(versionneu).capitalize())
        s.send_message(" #Upgrade beginnen")
        match antwort2:
            case "VerschlÃ¼sseler":
                shutil.move(tempfile + "/verschlÃ¼sseln.py", "./verschlÃ¼sseln.py")
                shutil.move(tempfile + "/shopping", "./shopping")
                os.mkdir("./programdata/verschlÃ¼sseln")
                filelist = os.listdir(tempfile + "/programdata/verschlÃ¼sseln")
                for i in filelist:
                    shutil.move(tempfile + "/programdata/verschlÃ¼sseln/" + i, "./programdata/verschlÃ¼sseln/" + i)
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_VerschlÃ¼sseler.txt", "w") as newV:
                    newV.write(versionneu)
            case "Haustier":
                shutil.move(tempfile + "/Haustier.py", "./Haustier.py")
                with open("./programdata/buero/versioninfo_Haustier.txt", "w") as newV:
                    newV.write(versionneu)
                shutil.move(tempfile + "/programdata/haustier", "./programdata/haustier")
                shutil.rmtree(tempfile + "/programdata")
            case "Ballonfahrt":
                filelist = os.listdir(tempfile + "/")
                filelist.remove("images"); filelist.remove("programdata")
                for i in filelist:
                    shutil.move(tempfile + "/" + i, "./" + i)
                shutil.move(tempfile + "/programdata/ballonfahrt", "./programdata/ballonfahrt")
                shutil.rmtree(tempfile + "/programdata")
                filelist = os.listdir(tempfile + "/images")
                for i in filelist:
                    shutil.move(tempfile + "/images/" + i, "./images/" + i)
                shutil.rmtree(tempfile + "/images")
                with open("./programdata/buero/versioninfo_Ballonfahrt.txt", "w") as newV:
                    newV.write(versionneu)
            case "SchingSchangSchongIQ":
                shutil.move(tempfile + "/SchingSchangSchongIntelligent.py", "./SchingSchangSchongIntelligent.py")
                shutil.move(tempfile + "/programdata/schingschangschongiq", "./programdata/schingschangschongiq")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_SchingSchangSchongIQ.txt", "w") as newV:
                    newV.write(versionneu)
            case "abstrakte Verzerrung":
                shutil.move(tempfile + "/abstrakt.py", "./abstrakt.py")
                shutil.move(tempfile + "/programdata/abstrakt", "./programdata/abstrakt")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_abstrakte Verzerrung.txt", "w") as newV:
                    newV.write(versionneu)
            case "im Verlies":
                shutil.move(tempfile + "/quest.py", "./quest.py")
                shutil.move(tempfile + "/level_editor.py", "./level-editor.py")
                shutil.move(tempfile + "/programdata/verlies", "./programdata/verlies")
                shutil.rmtree(tempfile + "/programdata")
                filelist = os.listdir(tempfile + "/images")
                for i in filelist:
                    shutil.move(tempfile + "/images/" + i, "./images/" + i)
                shutil.rmtree(tempfile + "/images")
                with open("./programdata/buero/versioninfo_im Verlies.txt", "w") as newV:
                    newV.write(versionneu)
            case "Passwortgenerator":
                shutil.move(tempfile + "/Passwortgenerator.py", "./Passwortgenerator.py")
                shutil.move(tempfile + "/programdata/password", "./programdata/password")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_Passwortgenerator.txt", "w") as newV:
                    newV.write(versionneu)
            case "Musik":
                shutil.move(tempfile + "/Musik.py", "./Musik.py")
                shutil.move(tempfile + "/programdata/music", "./programdata/music")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_Musik.txt", "w") as newV:
                    newV.write(versionneu)
            case "Garten im GlÃ¼ck":
                shutil.move(tempfile+"/Garten-im-GlÃ¼ck.py", "./Garten-im-GlÃ¼ck.py")
                filelist = os.listdir(tempfile + "/images")
                for i in filelist:
                    shutil.move(tempfile + "/images/" + i, "./images/" + i)
                shutil.rmtree(tempfile + "/images")
                with open("./programdata/buero/versioninfo_Garten im GlÃ¼ck.txt", "w") as newV:
                    newV.write(versionneu)
            case "Lebensmittel":
                shutil.move(tempfile + "/lebensmittel.py", "./lebensmittel.py")
                shutil.move(tempfile + "/programdata/lebensmittel", "./programdata/lebensmittel")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_Lebensmittel.txt", "w") as newV:
                    newV.write(versionneu)
            case "Das groÃŸe Quiz":
                shutil.move(tempfile+"/quiz.py", "./quiz.py")
                for i in os.listdir(tempfile+"/music"):
                    shutil.move(tempfile+"/music/"+i, "./music/"+i)
                shutil.rmtree(tempfile+"/music")
                with open("./programdata/buero/versioninfo_Das groÃŸe Quiz.txt", "w") as newV:
                    newV.write(versionneu)
            case "Rechnungen":
                shutil.move(tempfile+"/Rechnung.pyw", "./Rechnung.pyw")
                shutil.move(tempfile + "/programdata/rechnungen", "./programdata/rechnungen")
                with open("./programdata/buero/versioninfo_Rechnungen.txt", "w") as newV:
                    newV.write(versionneu)
            case "BÃ¼roMail":
                shutil.move(tempfile + "/mail.py", "./mail.py")
                shutil.move(tempfile + "/mail_agent.pyw", "./mail_agent.pyw")
                shutil.move(tempfile + "/programdata/mail", "./programdata/mail")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_BÃ¼roMail.txt", "w") as newV:
                    newV.write(versionneu)
            case "BÃ¼roBank":
                shutil.move(tempfile + "/bank.py", "./bank.py")
                shutil.move(tempfile + "/programdata/bank", "./programdata/bank")
                shutil.rmtree(tempfile + "/programdata")
                with open("./programdata/buero/versioninfo_BÃ¼roBank.txt", "w") as newV:
                    newV.write(versionneu)
            case "LTP Agent":
                shutil.move(tempfile + "/ltp_agent.py", "./ltp_agent.py")
                os.mkdir("./programdata/ltp")
                with open("./programdata/buero/versioninfo_LTP Agent.txt", "w") as newV:
                    newV.write(versionneu)
            case "BÃ¼roBonus":
                shutil.move(tempfile + "/bonus.py", "./bonus.py")
                shutil.move(tempfile+"/programdata/bonus", "./programdata/bonus")
                with open("./programdata/buero/versioninfo_LTP Agent.txt", "w") as newV:
                    newV.write(versionneu)
            case "Kaffee Manager":
                shutil.move(tempfile + "/kaffee.py", "./kaffee.py")
                os.mkdir("./programdata/kaffee")
                with open("./programdata/buero/versioninfo_Kaffee Manager.txt", "w") as newV:
                    newV.write(versionneu)
            case "GoodFood":
                shutil.move(tempfile + "/goodFood.py", "./goodFood.py")
                os.mkdir("./programdata/goodFood")
                with open("./programdata/buero/versioninfo_goodFood.txt", "w") as newV:
                    newV.write(versionneu)
            case _:
                py.alert("Fehlerhafter Paketname!")
                quit(code="ERROR")
        s.send_message(" #Upgrade installieren")
        print("Installation abgeschlossen.")
    else:
        quit(code="ERROR")
    s.send_message(" #Vorgang abschlieÃŸen")
    dLg.finalsave_log()
    py.alert("Die Operation war erfolgreich.", "Ende")
    if not pStart:
        try:
            bÃ¼.restart()
        except:
            py.alert("Fehler beim Neustarten.\nStarten Sie BÃ¼ro manuell neu.", "Fehler")
    else:
        if bÃ¼.buttonLog("Jetzt ausprobieren?", "BÃ¼ro starten", buttons=("JA", "NEIN")) == "JA":
            py.alert("Warnung: Falls Sie BÃ¼ro jetzt starten, kann es zu Fehlern kommen.")
            os.system("python ./bÃ¼ro.py")
    
if __name__ == "__main__":
    import bueroUtils as b
    bu = b.bueroUtils(True, "Update")
    py = bu.importPyautoguiCatched()
    update(alter=("Update" if py.confirm("Art des Vorgangs wÃ¤hlen:", "Update", buttons=("Update", "Upgrade")) == "Update" else "Upgrade"), pStart=True)
