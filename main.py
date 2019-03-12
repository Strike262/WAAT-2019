# coding=utf-8
from booleanModel import match, BooleanModel

if __name__ == "__main__":
    print "Using Fufunctions:"
    print match("recupero") & match("web")
    print match("recupero") | match("web")
    print match("recupero") & match("relitto", negation=True)
    print (match("web") | match("uso")) & match("strumenti")
    print (match("uso") | match("web")) & match("strumenti", negation=True)
    print match("informazioni") & match("relitto") & match("studente")
    print match("informazioni") | match("relitto") | match("studente")
    print match("bologna") | match("padova", negation=True)
    print "Using Objects:"
    print BooleanModel("recupero") & BooleanModel("web")
    print BooleanModel("recupero") | BooleanModel("web")
    print BooleanModel("recupero") & ~BooleanModel("relitto")
    print (BooleanModel("web") | BooleanModel("uso")) & BooleanModel("strumenti")
    print (BooleanModel("uso") | BooleanModel("web")) & ~BooleanModel("strumenti")
    print BooleanModel("informazioni") & BooleanModel("relitto") & BooleanModel("studente")
    print BooleanModel("informazioni") | BooleanModel("relitto") | BooleanModel("studente")
    print BooleanModel("bologna") | ~BooleanModel("padova")
