#!/usr/bin/python3
from configparser import ConfigParser
import os
import datetime

modul = input("Modulname (z.B. Theoretische Informatik III): ")
gruppe = input("Gruppenname (z.B. Gruppe 01 - Tutor): ")
autor = input("Autoren (Getrennt durch '\\\\'): ")
ws = int(datetime.date.today().strftime("%m")) in [1,2,3,10,11,12]
year = int(datetime.date.today().strftime("%Y"))

config = ConfigParser()
config.add_section("Global")
config.set("Global", "modul", modul)
config.set("Global", "gruppe", gruppe)
config.set("Global", "autor", autor)
config.set("Global", "sem", ("Wintersemester " + str(year) + "/" + str(year + 1)) if ws else ("Sommersemester " + str(year)))
config.set("Global", "num", "0")

with open("settings.ini", "w") as f:
    config.write(f)

os.remove("start.py")
