from time import *
def getLessonTime():
    
def request(roles):
    roleTranslate = {
        ">Biosz-kémia":"csop1",
        ">Infó":"csop2",
        ">OROSZ":"or",
        ">FRANCIA - MIHÁLYI":"frm",
        ">FRANCIA - CSIFFÁRYNÉ":"frc",
        ">NÉMET - KEZDŐ":"nk",
        ">NÉMET - HALADÓ":"nh",
        ">ANGOL - DR CSATLÓSI":"csk",
        ">ANGOL - BÁNHEGYESI":"ba",
        ">ANGOL - MIZERE":"mz",
        ">ANGOL - VÉNINGER":"ve",
        ">ANGOL - VARGA":"vi",
        ">ANGOL - KÉRI":"kj",
        ">ANGOL - MUHARI":"me",
        ">FIÚ":"fiu",
        ">LÁNY":"lany",
    }
    for i in range(roles):
        for t in range(["csop1","csop2"]):
            if roleTranslate(i) == t:
                szak = t
        for t in range(["or","frm","frc","nk","nh"]):
            if roleTranslate(i) == t:
                miny = t
        for t in range(["csk","ba","mz","ve","vi","kj","me"]):
            if roleTranslate(i) == t:
                einy = t
        for t in range(["fiu","lany"]):
            if roleTranslate(i) == t:
                nem = t
    return(nap,ora,nem,szak,einy,miny)