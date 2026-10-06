# Metodologia de creare a produselor digitale

> Sursa: textul dat de Andreea pe 2026-10-06 (etapele 4-10, regula de
> aprobare, modul de lucru, formatul primei analize). Etapele 1-3 nu au
> fost trimise încă; „Prima analiză" ține locul lor până atunci.
> Împărțirea pe agenți și porțile de aprobare sunt în `README.md`.

## Prima analiză (când vine o idee nouă)

Răspunsul are, în această ordine:

1. Ce înțeleg că este ideea
2. Pentru cine este
3. Problema rezolvată
4. Ce cred că este puternic
5. Ce nu este încă clar
6. Ce aș schimba
7. Produsul minim pe care l-aș testa
8. 3 întrebări de clarificare

Nu se construiește produsul complet până când Andreea nu aprobă direcția.

## Etapa 4 — Arhitectura produsului

Structura completă a produsului. Pentru fiecare componentă: **scopul, ce
conține, cum o folosește clientul, rezultatul obținut.**

Dacă produsul este un agent AI, se definesc: **rolul agentului,
inputurile, outputurile, workflow-ul, regulile, limitele, criteriile de
calitate, exemplele de utilizare, cazurile în care trebuie să ceară
informații suplimentare, cazurile în care trebuie să refuze să inventeze
informații.**

## Etapa 5 — Crearea produsului

Doar după aprobarea arhitecturii. Produsul trebuie să fie complet, clar,
practic, ușor de folosit, coerent, fără informații redundante.

- Prompt system → prompturile complete, organizate într-o structură logică.
- Agent AI → instrucțiunile agentului + exemple de input/output.
- Template sau workbook → toate secțiunile necesare.

## Etapa 6 — Testare

Înainte de finalizare, cel puțin **3 scenarii diferite**. Pentru fiecare:

```
Input:
Proces:
Output așteptat:
Posibile erori:
Cum ar trebui corectat sistemul?
```

Se caută în special: contradicții, instrucțiuni ambigue, informații
lipsă, pași inutili, rezultate care nu corespund problemei inițiale.

## Etapa 7 — Product ladder

Pentru fiecare produs finalizat, o posibilă scară:

- **FREE** — un produs foarte mic care demonstrează valoarea.
- **ENTRY** — simplu, cu preț redus.
- **CORE** — produsul principal.
- **PREMIUM** — mai complex, cu mai multe funcții sau personalizare.

Nu se creează automat toate variantele. Se recomandă doar cele care au
logică pentru produsul respectiv.

## Etapa 8 — Poziționare și vânzare

După aprobarea produsului: nume final, tagline, descriere scurtă,
descriere lungă, problema pe care o rezolvă, ce primește clientul, pentru
cine este, pentru cine NU este, beneficii, obiecții posibile, FAQ, CTA,
idei de demonstrație.

Interzise, dacă nu pot fi demonstrate: „îți garantează", „îți dublează
veniturile", „îți aduce clienți garantat".

## Etapa 9 — Preț

Un **interval**, nu un preț prezentat ca adevăr obiectiv. Se explică: ce
justifică prețul, ce ar face produsul mai valoros, ce l-ar face prea
scump, ce variantă ar putea fi testată inițial. Dacă nu există
suficiente informații despre piață, se spune clar că e o ipoteză de
testat.

## Etapa 10 — Lansare

După aprobarea produsului, un mini-plan: produsul, oferta, canalul,
conținutul de promovare, produsul gratuit (dacă are sens), CTA, primele
experimente, ce metrici urmărim. Nu se presupune că primul produs va avea
succes. **Obiectivul inițial este validarea.**

## Regula de aprobare

Nu se iau decizii importante despre produs fără aprobarea Andreei. Se pot
propune produse, modificări, simplificări, agenți noi, structuri noi,
variante de preț, strategii de lansare — dar nicio sugestie nu e
aprobată până când Andreea confirmă explicit.

## Mod de lucru

Incremental. Nu un produs de 100 de pagini când 10 pagini rezolvă aceeași
problemă. Întâi MVP-ul; după validare, versiunea următoare. Înainte de
orice etapă care construiește efectiv produsul, se întreabă: **„Vrei să
trecem la următoarea etapă?"**
