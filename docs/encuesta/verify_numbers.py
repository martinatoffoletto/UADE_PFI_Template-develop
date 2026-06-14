# -*- coding: utf-8 -*-
"""Verifica cada cifra citada en chapter03/conclusion/surveys contra el CSV."""
import csv, io, sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
PATH = "Uso de servicios de logística para envío y recepción de encomiendas en el área del AMBA(1-145).csv"
text = open(PATH, encoding="utf-8-sig").read().split("\n", 1)[1]
rows = list(csv.reader(io.StringIO(text), delimiter=";"))
hdr = [h.strip().replace("\n", " ").replace("\xa0", " ") for h in rows[0]]
data = [dict(zip(hdr, r)) for r in rows[1:] if any(c.strip() for c in r)]

def col(frag):
    return next(h for h in hdr if frag in h and not h.startswith(("Puntos", "Comentarios")))

def vals(frag):
    return [(d.get(col(frag)) or "").strip() for d in data if (d.get(col(frag)) or "").strip()]

def multi(frag):
    c = Counter()
    n = 0
    for v in vals(frag):
        n += 1
        for p in v.split(";"):
            if p.strip():
                c[p.strip()] += 1
    return c, n

ok = True
def check(desc, got, exp):
    global ok
    flag = "OK " if abs(got - exp) < 0.05 else "FAIL"
    if flag == "FAIL":
        ok = False
    print(f"[{flag}] {desc}: doc={exp} csv={round(got,1)}")

check("Total respuestas", len(data), 145)

amba = vals("Vivís o trabajas")
check("AMBA n", amba.count("Sí"), 133)
check("AMBA %", amba.count("Sí")/len(data)*100, 91.7)

perf, nperf = multi("perfiles te representa")
part = perf["Particular / consumidor final"]
pyme = perf["Trabajo en una PyME o comercio"] + perf["Tengo un emprendimiento o vendo por redes"]
check("Perfil n base", nperf, 133)
check("Particular menciones", part, 111)
check("Particular % de 145", part/145*100, 76.6)
check("Particular % de 133", part/133*100, 83.5)
check("PyME+empr menciones", pyme, 11)
check("PyME+empr % de 145", pyme/145*100, 7.6)
check("PyME % de 133", perf["Trabajo en una PyME o comercio"]/133*100, 5.3)
check("Empr % de 133", perf["Tengo un emprendimiento o vendo por redes"]/133*100, 3.0)
check("Otro n", perf["Otro"], 13)
check("Otro %", perf["Otro"]/133*100, 9.8)

uso = vals("Usás servicios")
check("Uso base", len(uso), 133)
check("Uso Sí n", uso.count("Sí"), 106)
check("Uso Sí %", uso.count("Sí")/len(uso)*100, 79.7)
check("Uso No n", uso.count("No"), 17)
check("Uso No %", uso.count("No")/len(uso)*100, 12.8)
check("Uso dispuesto n", uso.count("No usé, pero estaría dispuesto/a"), 10)
check("Uso dispuesto %", uso.count("No usé, pero estaría dispuesto/a")/len(uso)*100, 7.5)

asp, nasp = multi("aspectos tenés en cuenta")
check("Aspectos base", nasp, 116)
for k, exp_n, exp_p in [("Costos del servicio",87,75.0),("Seguridad y confianza",75,64.7),
                        ("Velocidad de entrega",74,63.8),("Zonas de entrega cubiertas",40,34.5),
                        ("Facilidad de uso / experiencia digital",35,30.2)]:
    check(f"Aspecto {k} n", asp[k], exp_n)
    check(f"Aspecto {k} %", asp[k]/nasp*100, exp_p)
asp_otro = sum(v for k,v in asp.items() if k.startswith("Otro"))
check("Aspecto Otro n", asp_otro, 6)
asp_esp = sum(v for k,v in asp.items() if k.startswith("Transporte especializado"))
check("Aspecto Transporte especializado n", asp_esp, 3)

wtp = vals("Cuánto pagarías")
check("WTP base", len(wtp), 116)
check("WTP <3000 n", wtp.count("Menos de $3.000"), 22)
check("WTP 3000-6000 n", wtp.count("$3.000 - $6.000"), 79)
check("WTP 3000-6000 %", wtp.count("$3.000 - $6.000")/len(wtp)*100, 68.1)
check("WTP 6000-10000 n", wtp.count("$6.000 - $10.000"), 14)
check("WTP >10000 n", wtp.count("Más de $10.000"), 1)

prob, nprob = multi("problemas tuviste")
check("Problemas base", nprob, 115)
for k, exp_n in [("Demoras",63),("Falta de seguimiento",50),("Dificultad para coordinar horarios",50),
                 ("Precio alto",40),("Mala atención",19),("Daños o pérdidas",19),
                 ("No tuve problemas",16),("Falta de confianza",15),("Poca cobertura",6)]:
    check(f"Problema {k} n", prob[k], exp_n)
check("Problema Demoras %", prob["Demoras"]/nprob*100, 54.8)
online = sum(v for k,v in prob.items() if "online" in k or "contratar" in k)
check("Problema contratar online n", online, 7)

est = vals("Estaría...")
check("Predisposición base", len(est), 116)
check("Muy n", est.count("Muy dispuesto/a"), 38)
check("Algo n", est.count("Algo dispuesto/a"), 43)
check("Indif n", est.count("Indiferente"), 24)
check("Poco n", est.count("Poco dispuesto/a"), 9)
check("Nada n", est.count("Nada dispuesto/a"), 2)
check("Predisposición colaborativa % (Muy+Algo)", (est.count("Muy dispuesto/a")+est.count("Algo dispuesto/a"))/len(est)*100, 69.8)

foto = vals("clasificar tu paquete")
check("Foto base", len(foto), 116)
check("Foto Sí n", sum(1 for v in foto if v.startswith("Sí")), 93)
check("Foto Sí %", sum(1 for v in foto if v.startswith("Sí"))/len(foto)*100, 80.2)
check("Foto indif n", sum(1 for v in foto if v.startswith("Me es indiferente")), 17)
check("Foto indif %", sum(1 for v in foto if v.startswith("Me es indiferente"))/len(foto)*100, 14.7)
check("Foto desconf n", sum(1 for v in foto if v.startswith("No")), 6)
check("Foto desconf %", sum(1 for v in foto if v.startswith("No"))/len(foto)*100, 5.2)

co2 = vals("Me aportaría")
check("CO2 base", len(co2), 116)
check("CO2 mucho n", co2.count("Mucho valor"), 18)
check("CO2 bastante n", co2.count("Bastante valor"), 44)
check("CO2 indif n", co2.count("Indiferente"), 24)
check("CO2 poco n", co2.count("Poco valor"), 15)
check("CO2 ningún n", co2.count("Ningún valor"), 15)
check("CO2 valora % (mucho+bastante)", (co2.count("Mucho valor")+co2.count("Bastante valor"))/len(co2)*100, 53.4)

disp = vals("dispuesto/a a transportar")
check("Disposición transportar base", len(disp), 116)
check("Disp Sí n", disp.count("Sí, me interesaría"), 48)
check("Disp Tal vez n", disp.count("Tal vez, depende de las condiciones"), 50)
check("Disp No n", disp.count("No, no me interesa"), 18)
check("Interés transportista % (Sí+TalVez)", (disp.count("Sí, me interesaría")+disp.count("Tal vez, depende de las condiciones"))/len(disp)*100, 84.5)

wta = vals("cuánto te tendrían que pagar")
check("WTA base", len(wta), 96)
check("WTA <1000 n", wta.count("Menos de $1.000"), 2)
check("WTA 1000-2500 n", wta.count("$1.000 - $2.500"), 19)
check("WTA 2500-5000 n", wta.count("$2.500 - $5.000"), 49)
check("WTA 2500-5000 %", wta.count("$2.500 - $5.000")/len(wta)*100, 51.0)
check("WTA >5000 n", wta.count("Más de $5.000"), 26)

med, nmed = multi("medio/s de transporte")
check("Medios base", nmed, 98)
for k, exp_n, exp_p in [("Auto",79,80.6),("A pie",25,25.5),("Moto",23,23.5),
                        ("Bicicleta",22,22.4),("Transporte especializado",16,16.3)]:
    check(f"Medio {k} n", med[k], exp_n)
    check(f"Medio {k} %", med[k]/nmed*100, exp_p)
mayor = sum(v for k,v in med.items() if "mayor porte" in k)
check("Medio mayor porte n", mayor, 13)

mot, nmot = multi("principal motivación")
check("Motivación base", nmot, 98)
ingreso = sum(v for k,v in mot.items() if "ingreso extra" in k)
check("Motivación ingreso extra n", ingreso, 90)
check("Motivación ingreso extra %", ingreso/nmot*100, 91.8)
espacio = sum(v for k,v in mot.items() if "espacio libre" in k)
check("Motivación espacio n", espacio, 28)
huella = sum(v for k,v in mot.items() if "huella" in k)
check("Motivación huella n", huella, 15)
comercio = sum(v for k,v in mot.items() if "comercio" in k)
check("Motivación comercio n", comercio, 6)

pre, npre = multi("preocupación sobre participar")
check("Preocupaciones base", npre, 94)
for k, exp_n in [("Responsabilidad por daños",69),("Pago / comisión",42),
                 ("Confianza en el cliente",32),("Interferencia con mi rutina",32),("Ninguna",5)]:
    check(f"Preocupación {k} n", pre[k], exp_n)
check("Responsabilidad %", pre["Responsabilidad por daños"]/npre*100, 73.4)
check("Pago %", pre["Pago / comisión"]/npre*100, 44.7)

nouso, nnouso = multi("motivos por los que no utiliza")
check("No-uso base", nnouso, 133)
for k, exp_n in [("No existe la necesidad",65),("Costos elevados",52),
                 ("Falta de confianza en prestadores/sistemas",28),("Escasez de opciones",24)]:
    check(f"No-uso {k} n", nouso[k], exp_n)
cob = sum(v for k,v in nouso.items() if "cobertura" in k)
check("No-uso sin cobertura n", cob, 15)
eco = sum(v for k,v in nouso.items() if "ecológicas" in k)
check("No-uso sin opciones ecológicas n", eco, 4)
otro2 = sum(v for k,v in nouso.items() if k.startswith("Otro"))
check("No-uso Otro n", otro2, 8)

print("\n" + ("TODO VERIFICADO ✔" if ok else "HAY DIFERENCIAS ✘"))
