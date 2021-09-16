from logging import StringTemplateStyle
from textdetector import *
def analyze(string):
    string = str(string)
    string = string.lower()
    if len(string.split(" ")) > 2:
        if getIntent(string,["milyen","melyik","mi","hol","kövi","következő"],["hol","milyen","melyik","hol","terem","teremben","óra","órán","lesz","leszünk","lesz?","leszünk?","óra?"]) == True:
            return("Üzenet")
        else:
            return("Errno 1: nodec")
    else:
        return("Errno 2: tsm")