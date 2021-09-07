def getIntent(text):
    words = str(text).split()
    for n in words:
        for i in ["Hol","Milyen","Mi","Melyik"]:
            if i == n:
                pass
            else:
                words.pop(0)