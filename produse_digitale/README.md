# Produse digitale — Andreea Tech

> Echipă separată de cea de LinkedIn (`content_agent/`), pentru produse
> digitale vândute sub brandul **Andreea Tech**. Decizia Andreei,
> 2026-10-06. Refolosește brandul și vocea din `content_agent/context/`
> (`brand_fundatie.md`, `ghid_voce.md`, `audience.md`) — nu le duplică.

## De ce produse

Andreea are job full-time. Produsele digitale se fac o dată și se vând
fără termene de client, în ritmul ei (seara, în weekend). Primul obiectiv
nu e venit mare, ci să afle **dacă cineva plătește** — de aceea primele
produse sunt mici și se fac în 1-2 weekenduri.

## Formate posibile

Sisteme de prompturi, agenți AI și workflow-uri AI, șabloane, workbook-uri,
checklist-uri, ghiduri, toolkit-uri, framework-uri, mini-cursuri, sisteme
pentru business, produse hibride (mai multe formate împreună).

**Avantajul real al Andreei:** a construit și folosește sisteme cu agenți
AI (echipa de conținut LinkedIn din acest repo). Produsele pot porni din
ce a construit efectiv — nu din teorie.

## Echipa (`.claude/agents/`) — un agent pe etapă

Toți agenții citesc `metodologie.md` (rolul, principiul central și
regulile comune); fiecare face doar etapele lui.

| # | Agent | Etape (din `metodologie.md`) |
|---|---|---|
| 1 | 🔎 `produs-descoperire` | 1 Descoperire → prima analiză în 8 puncte (sau 2-3 interpretări, dacă ideea e vagă) |
| 2 | 📐 `produs-definire` | 2 Definire + 3 Validare |
| 3 | 🏗️ `produs-arhitect` | 4 Arhitectura (+ dimensiune MVP, FAPTE PERMISE, INTERZIS) |
| 4 | 🛠️ `produs-creator` | 5 Crearea |
| 5 | 🧪 `produs-tester` | 6 Testarea (3+ scenarii) + reguli; verifică și textele de la 8 |
| 6 | 🛒 `produs-cumparator` | la 6 (produsul) și la 8 (textele de vânzare) |
| 7 | 🪜 `produs-ladder-pret` | 7 Product ladder + 9 Preț |
| 8 | 🏷️ `produs-pozitionare` | 8 Poziționare și vânzare |
| 9 | 🚀 `produs-lansare` | 10 Lansare |
| — | 🎯 Coordonatorul | conversația principală: porțile de aprobare, salvarea pe `main` |

## Cum circulă un produs — cu porți de aprobare

Fiecare 🔒 e o poartă: coordonatorul se oprește, îi arată Andreei
rezultatul și întreabă **„Vrei să trecem la următoarea etapă?"**. Nimic
nu trece mai departe fără un „da" explicit (regula de aprobare din
`metodologie.md`).

```
1. Etapa 1 · Prima analiză ....... descoperire        🔒 aprobă direcția
2. Etapele 2 + 3 · Definire+valid. definire           🔒 aprobă definiția
3. Etapa 4 · Arhitectura ......... arhitect           🔒 aprobă structura
4. Etapa 5 · Crearea ............. creator
5. Etapa 6 · Testarea ............ tester + cumpărător (în paralel)
   → revizii la creator (max 2)                       🔒 aprobă produsul
6. Etapele 7 + 9 · Ladder + preț . ladder-pret        🔒 aprobă treptele și intervalul
7. Etapa 8 · Poziționare ......... pozitionare → tester + cumpărător
                                                      🔒 aprobă textele
8. Etapa 10 · Lansare ............ lansare            🔒 aprobă planul
```

Ordinea 7 → 9 → 8: textele de vânzare (8) au nevoie de scara de produse
și de intervalul de preț, deci vin după ele. Dacă testerul și
cumpărătorul nu sunt de acord după 2 revizii, decide Andreea.

## Salvare pe `main`

Fiecare produs are folderul lui: `produse_digitale/produse/<nume-scurt>/`
cu `analiza.md` (etapele 1-3), `arhitectura.md`, `produs.md`, `testare.md`,
`ladder_pret.md`, `pozitionare.md`, `lansare.md` și `istoric.md`
(verdicte, aprobări, revizii) — fiecare fișier apare doar când etapa lui
e aprobată. Totul se urcă pe `main`.

## Ce NU face echipa

- Nu inventează rezultate, cifre, testimoniale sau clienți.
- Nu promite venituri sau creștere garantată.
- Nu decide platforma de vânzare, prețul final sau partea legală
  (PFA/facturare) — le propune, decide Andreea.
