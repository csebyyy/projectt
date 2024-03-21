def mpbe(o, p, mp):
    return o * 3600 + p * 60 + mp


def opmp(mp):
    return mp // 3600, (mp // 60) % 60, mp % 60

hivasok = []
sorszam = 0
f = open("hivas.txt", "rt", encoding="utf-8")
for hivas in f:
    ido = [int(i) for i in hivas.split()]
    sorszam += 1
    hivasok.append([sorszam, mpbe(*ido[:3]), mpbe(*ido[3:])])

print("3. feladat")
statisztika = [0] * 24
for hivas in hivasok:
    kezdet = hivas[1]
    ora = kezdet // 3600
    statisztika[ora] += 1

for i in range(len(statisztika)):
    db = statisztika[i]
    if db:
        print(i, "óra", db, "hívás")

print("4. feladat")
hossz = [h[2] - h[1] for h in hivasok]
max_index = hossz.index(max(hossz))
leghosszabb = hivasok[max_index]
print(f"A leghosszabb ideig vonalban lévő hívó {leghosszabb[0]}. sorban szerepel, a hívás hossza: {hossz[max_index]} másodperc.")

print("5. feladat")
var = 0
hivo_sorszam = None
o = input("Adja meg az órát: ")
p = input("Adja meg a percet: ")
mp = input("Adja meg a másodpercet: ")


idopont = mpbe(int(o), int(p), int(mp))
for sorszam, kezdet, veg in hivasok:
    if kezdet <= idopont <= veg:
        var += 1
        if not hivo_sorszam:
            hivo_sorszam = sorszam
            var -= 1
if hivo_sorszam:
    print(f"Várakozók száma: {var} a beszélő a {hivo_sorszam}. hívó.")
else:
    print("Nem volt beszélő")

print("6. feladat:")
fogadott = []
bkezd = mpbe(8, 0, 0)
bveg = mpbe(8, 0, 0)
varakozas = None
for sorszam, hkezd, hveg in hivasok:
    if hveg // 3600 < 8:
        continue
    if hkezd // 3600 >= 12:
        break
    if hveg <= bveg:
        continue
    if hkezd < bveg:
        varakozas = bveg - hkezd
        bkezd = bveg
    else:
        varakozas = 0
        bkezd = hkezd
    bveg = hveg
    fogadott.append([sorszam, bkezd, bveg, varakozas])
print(f"Az utolsó telefonáló adatai a {fogadott[-1][0]}. sorban van és {fogadott[-1][-1]} másodpercet várt.")

print("7. feladat:")
print("sikeres.txt")
sikeres = open("sikeres.txt", "w")
for sorszam, bkezd, bveg, varkozas in fogadott:
    bko, bkp, bkmp = opmp(bkezd)
    bvo, bvp, bvmp = opmp(bveg)
    print(sorszam,  bko, bkp, bkmp, bvo, bvp, bvmp, file = sikeres)
sikeres.close()