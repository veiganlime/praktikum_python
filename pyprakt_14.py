def wochentag(d,m,y):
    tag=["Sonntag","Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag"]
    if(m<3): y=y-1
    w=((d+int(2.6*((m+9)%12+1)-0.2)+y%100+(y%100)//4+y//400-2*(y//100)-1)%7+7)%7+1
    assert 0<=w<=6,"Rechenfehler"
    return tag[w]

t = int(input("Tag: "))
m = int(input("Monat: "))
j = int(input("Jahr: "))
wt = wochentag(t,m,j)
print(f"Der {t}.{m}.{j} ist ein {wt}")