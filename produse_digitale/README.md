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

| # | Rol | Agent | Răspunde cu |
|---|---|---|---|
| 1 | 🧭 Strategul de produs | `produs-strateg` | FIȘA PRODUSULUI / AVIZ FAVORABIL-NEFAVORABIL |
| 2 | 🛠️ Creatorul | `produs-creator` | produsul complet + pagina de vânzare |
| 3 | 🔍 Verificatorul | `produs-verificator` | APROBAT / RESPINS |
| 4 | 🛒 Cumpărătorul de test | `produs-cumparator` | AȘ CUMPĂRA / N-AȘ CUMPĂRA |
| 5 | 🎯 Coordonatorul | conversația principală Claude Code | — |

## Cum circulă un produs

```
Strateg (FIȘA) → Creator (produs + pagină) → Verificator + Cumpărător
→ Strateg (AVIZ) → Andreea
```

1. **Fișa** — `produs-strateg` decide: pentru cine, ce problemă rezolvă,
   formatul, ce conține (versiunea mică!), prețul propus, ce fapte reale
   avem voie să folosim.
2. **Creare** — `produs-creator` scrie produsul complet și pagina de
   vânzare, pe fișă.
3. **Verificare, în paralel:**
   - `produs-verificator` — fapte, promisiuni, prompturi testate, voce.
   - `produs-cumparator` — primește **doar** pagina de vânzare și
     produsul, fără fișă; răspunde ca un cumpărător real.
4. **Revizie** — maximum 2, apoi se livrează marcat dacă n-a trecut.
5. **Aviz** — strategul confirmă că produsul livrează ce a promis fișa.
6. **Andreea** — primește un singur fișier final.

## Salvare pe `main`

Fiecare produs are folderul lui: `produse_digitale/produse/<nume-scurt>/`
cu `fisa.md`, `produs.md` (conținutul complet), `pagina_vanzare.md` și
`istoric.md` (verdicte, aviz, revizii). Totul se urcă pe `main`.

## Ce NU face echipa

- Nu inventează rezultate, cifre, testimoniale sau clienți.
- Nu promite venituri sau creștere garantată.
- Nu decide platforma de vânzare, prețul final sau partea legală
  (PFA/facturare) — le propune, decide Andreea.
