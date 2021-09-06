intents = {
  "kovora":["Milyen óra lesz","Mi lesz a következő óra","Hol leszünk","Hol leszünk következő órán","Melyik teremben leszünk","Mi lesz a kövi óra","Hol lesz a következő óra","Melyik teremben lesz a következő óra","Melyik teremben lesz a kövi óra","Hol vagyunk"]
}
def getIntent(text):
    words = str(text).split()
    for n in words:
        pass