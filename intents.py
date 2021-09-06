def getIntent(text):
    words = str(text).split()
    for n in words:
        if ["Hol","Milyen","Mi","Melyik"].count(n) > 0:
            for i in range(0):
                pass