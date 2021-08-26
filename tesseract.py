# -*- coding: UTF-8 -*-


from PIL import Image
import pytesseract
import os
import time
import csv


startzeit = time.strftime("%d.%m.%Y_%H-%M-%S %Z")  # für Logfile
start = time.time()  # für Berechnung der Dauer des Skripts
counter_processed = 0  # wie viele Dateien wurden verarbeitet
counter_skipped = 0  # wie viele Dateien wurden ausgelassen
counter_all = 1  # Gesamtzahl der Dateien


cwd = os.getcwd()
data_path = cwd + os.sep + "data"


logfile = open("logfile_" + startzeit + ".txt", "w")
print("Start des Skripts: {}\n\n".format(startzeit), file=logfile)

gesamt = open("gesamtübersicht_" + startzeit + ".csv", "w")
heading = ["Lfd. Nr.", "Pfad und Dateiname", "Status", "Text"]  # Überschriftenzeile schreiben
mywriter = csv.writer(gesamt, dialect='excel', delimiter=';')
mywriter.writerow(heading)


for root, dirs, files in os.walk(data_path):
    for file in files:
        print("Datei {} wird verarbeitet".format(file))
        try:
            fullfile = os.path.join(root, file)
            data = pytesseract.image_to_string(Image.open(fullfile), lang="eng+deu")
            if len(data) > 0:
                outputfile = file + ".txt"
                with open(outputfile, "w") as target:
                    target.write(data)
                    print("Datei {} erfolgreich abgearbeitet".format(fullfile), file=logfile)
                    counter_processed += 1
                    row = (counter_all, fullfile, "Es wurde Text erkannt", data)
                    mywriter.writerow(row)
                    counter_all += 1
            else:
                print("Datei {} erfolgreich abgearbeitet, es wurde kein Text gefunden".format(fullfile), file=logfile)
                row = (counter_all, fullfile, "Es wurde kein Text erkannt",)
                mywriter.writerow(row)
                counter_all += 1
        except:
            print("Datei {} ist kein Bild, die Datei wurde übersprungen".format(fullfile), file=logfile)
            counter_skipped += 1
            row = (counter_all, fullfile, "Datei ist kein Bild und wurde übersprungen",)
            mywriter.writerow(row)
            counter_all += 1


print("\n\nEs wurde(n) {} Datei(en) verarbeitet.".format(counter_processed), file=logfile)
print("Es wurde(n) {} Datei(en) übersprungen.".format(counter_skipped), file=logfile)
endzeit = time.strftime("%d.%m.%Y_%H-%M-%S %Z")  # für Logfile
ende = time.time()  # für Berechnung der Dauer des Skripts
print("\n\nEnde des Skripts: {}".format(endzeit), file=logfile)
dauer = ende - start
print("\nDauer der Abarbeitung: {:.2f} Sekunden bzw. rund {:.2f} Minuten".format(dauer, dauer/60), file=logfile)


logfile.close()
gesamt.close()
