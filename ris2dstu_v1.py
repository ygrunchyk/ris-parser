def authors(au):
    r=au.split(", ")
    if len(r)==2:
        return r[0]+" "+r[1][0]+"."
    if len(r)==1:
        return r[0]

def convert(ris_text):
    title=""
    journal=""
    year=""
    volume=""
    doi=""
    AU=[]
    for i in ris_text.splitlines():
        k,v=i.split("  - ")
        # print(k, v)
        if k=="T1":
            title=v
        if k=="JO":
            journal=v
        if k=="PY":
            year=v
        if k=="VL":
            volume=v
        if k=="SP":
            sp=v
        if k=="DO":
            doi=v
        if k=="AU":
            au=v
            AU.append(authors(au))
    return "%s %s. // %s. %s. %s. %s. DOI: %s"%(", ".join(AU), title, journal, year, volume, sp, doi)

f1=open("S2666165925000286.ris", "r")
s=f1.read()
f1.close() # закрити файл
r=convert(s)
print(r)