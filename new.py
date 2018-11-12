from configparser import ConfigParser
import os, string

config = ConfigParser()
config.read("settings.ini")
modul = config.get("Global", "modul")
gruppe = config.get("Global", "gruppe")
sem = config.get("Global", "sem")
autor = config.get("Global", "autor")
num = config.getint("Global", "num")

num += 1
config.set("Global", "num", str(num))

with open("settings.ini", 'w') as f:
    config.write(f)
    f.close()

with open("resource/template.tex", "r") as f:
    content = f.read()
    f.close()

os.mkdir("Blatt " + str(num))

with open("Blatt " + str(num) + "/" + modul + " - " + str(num) + ".tex", "w") as f:
    f.write(content.replace("%GRUPPE%", gruppe).replace("%MODUL%", modul).replace("%AUTOR%", autor).replace("%NUM%", str(num)).replace("%SEM%", sem))
    f.close()

