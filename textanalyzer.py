from textdetector import *
def analyze(string):
    string = str(string)
    string = string.lower()
    if getIntent(string,["milyen","melyik","mi","hol","kövi","következő"],["hol","milyen","melyik","hol","terem","teremben","óra","órán","lesz","leszünk","lesz?","leszünk?","óra?"]) == True:
        return("Üzenet")
    else:
        return("NONE Errno 1: nodec")