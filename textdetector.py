
def getIntent(text,triggerwords,searchwords):
    words = str(text).split()
    for n in words:
        for i in list(triggerwords):
            if i == n:
                #felismeri a szót
                bias = 0
                for b in list(searchwords):
                    bias += words.count(b)
                if bias > round(len(words) * 0,75):
                    return(True)
                else:
                    return(False)
            else:
                if len(words) > 0:
                    words.pop(0)
                else:
                    return(False)
    return(False)