def getIntent(text):
    words = str(text).split()
    for n in words:
        for i in ["hol","milyen","mi","melyik"]:
            if i == n:
                #felismeri a szót
                bias = 0
                for b in ["",""]:
                    bias += words.count(b)
                if bias > round(len(words) * 0,75):
                    return()
            else:
                words.pop(0)