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

## Echipa (`.claude/agents/`)

| # | Rol | Agent | Etape (din `metodologie.md`) |
|---|---|---|---|
| 1 | 🧭 Strategul | `produs-strateg` | Prima analiză · 4 Arhitectura · 7 Ladder · 9 Preț · 10 Lansare · Aviz |
| 2 | 🛠️ Creatorul | `produs-creator` | 5 Crearea · 8 Poziționare și vânzare |
| 3 | 🔍 Verificatorul | `produs-verificator` | 6 Testare (3+ scenarii) + reguli, pe produs și pe texte |
| 4 | 🛒 Cumpărătorul de test | `produs-cumparator` | la 6 (produsul) și la 8 (textele de vânzare) |
| 5 | 🎯 Coordonatorul | conversația principală | porțile de aprobare, salvarea pe `main` |

## Cum circulă un produs — cu porți de aprobare

Fiecare 🔒 e o poartă: coordonatorul se oprește, îi arată Andreei
rezultatul și întreabă **„Vrei să trecem la următoarea etapă?"**. Nimic
nu trece mai departe fără un „da" explicit (regula de aprobare din
`metodologie.md`).

```
1. Prima analiză .............. strateg            🔒 aprobă direcția
2. Etapa 4 · Arhitectura ...... strateg            🔒 aprobă structura
3. Etapa 5 · Crearea .......... creator
4. Etapa 6 · Testarea ......... verificator + cumpărător (în paralel)
   → revizii (max 2) → aviz strateg              🔒 aprobă produsul
5. Etapele 7 + 9 · Ladder + preț  strateg           🔒 aprobă treptele și intervalul
6. Etapa 8 · Poziționare ...... creator → verificator + cumpărător
                                                    🔒 aprobă textele
7. Etapa 10 · Lansare ......... strateg            🔒 aprobă planul
```

Ordinea 7 → 9 → 8: textele de vânzare (8) au nevoie de scara de produse
și de intervalul de preț, deci vin după ele.

**Etapele 1-3** din metodologia Andreei n-au fost trimise încă; până
atunci, „Prima analiză" ține locul lor.

## Salvare pe `main`

Fiecare produs are folderul lui: `produse_digitale/produse/<nume-scurt>/`
cu `analiza.md`, `arhitectura.md`, `produs.md`, `testare.md`,
`ladder_pret.md`, `pozitionare.md`, `lansare.md` și `istoric.md`
(verdicte, aprobări, revizii) — fiecare fișier apare doar când etapa lui
e aprobată. Totul se urcă pe `main`.

## Ce NU face echipa

- Nu inventează rezultate, cifre, testimoniale sau clienți.
- Nu promite venituri sau creștere garantată.
- Nu decide platforma de vânzare, prețul final sau partea legală
  (PFA/facturare) — le propune, decide Andreea.
