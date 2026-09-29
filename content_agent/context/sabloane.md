# Sistemul de șabloane — Andreea Tech

> **Status: PROPUNERE — de confirmat de Andreea** (2026-09-29).
> Se sprijină pe `brand_fundatie.md` (culori, fonturi), `ghid_voce.md`
> (text) și `offers.md` (pachete). Logo-ul nu e încă ales (vezi
> `logo_directii.md`) — peste tot unde scrie **[SEMN]** intră monograma
> aleasă; până atunci, textul „Andreea Tech" în Archivo ExtraBold.

## Ce intră în prima lună — și ce nu

Prioritizat după ce folosește Andreea **acum**, nu după ce ar fi frumos
de avut. În repo nu există semne că folosește prezentări sau newsletter;
e-mailuri către clienți nu are încă (confirmat 2026-09-28).

| # | Șablon | De ce acum | Cât de des |
|---|---|---|---|
| 1 | **Poza de postare LinkedIn (4:5)** | se folosește la fiecare postare | 2-3 / săptămână |
| 2 | **Banner LinkedIn** | primul lucru văzut când cineva îți deschide profilul după o postare | o dată |
| 3 | **Oferta PDF** | pachetele au preț fix — oferta e aceeași structură la fiecare client | la fiecare cerere |
| 4 | **Semnătura de e-mail** | apare în fiecare răspuns către un client nou | o dată |

**Amânate, cu motiv:**
- **Prezentări (16:9)** — nimic în repo nu arată că prezintă; consultația
  e discuție, nu slide-uri. Se face când apare prima nevoie reală.
- **Șablon de e-mail** — nu există încă e-mailuri; semnătura e suficientă.
- **Carusel LinkedIn** — formatul de acum e postare cu o singură poză.
- **Facebook** — Andreea a cerut sistemul doar pentru LinkedIn.

## Reguli comune tuturor șabloanelor

- **Culori:** fundal `#EBEEF8` sau alb `#FFFFFF`; text `#10173D`;
  text secundar `#263568`; **un singur accent** `#2743B8`.
  Fără degrade, sclipiri, umbre puternice.
- **Fonturi:** titluri **Archivo** (ExtraBold 800); text **Inter**
  (Regular 400 / SemiBold 600). Maximum 2 fonturi pe material.
- **Margini:** minimum 6% din lățime pe fiecare latură — nimic lipit de
  margine.
- **Diacritice cu virgulă** (ș, ț), ghilimele „...".
- **Text:** după `ghid_voce.md` — fără jargon, fără englezisme evitabile.

## 1. Poza de postare LinkedIn

- **Dimensiune:** 1080 × 1350 px (4:5).
- **Structură:**
  - sus (primele ~25%): **titlul** — maximum 6 cuvinte;
  - mijloc (~60%): **imaginea care arată contrastul** din hook (ex.
    Luni/Joi) — cu etichete reale de 1-2 cuvinte, nu bare abstracte;
  - jos (~15%): spațiu liber + **[SEMN]** mic în colțul din dreapta jos.
- **Ierarhia tipografică:**
  | Nivel | Font | Mărime | Culoare |
  |---|---|---|---|
  | Titlu | Archivo 800 | 64-80 px | `#10173D` |
  | Etichete | Inter 600 | 32-40 px | `#10173D` |
  | Accent (un cuvânt/element) | — | — | `#2743B8` |
- **Elemente reutilizabile:** zona de titlu, [SEMN] în colț, fundalul
  `#EBEEF8`.
- **Consecvent la fiecare postare:** poziția titlului, poziția [SEMN],
  un singur accent albastru.
- **Poate varia:** ce arată mijlocul (telefon, listă, obiect, ilustrație).
- **Test obligatoriu:** se înțelege fără să citești postarea
  (regula din `linkedin-image-prompt.md`).

## 2. Banner LinkedIn

- **Dimensiune:** 1584 × 396 px.
- **Zonă moartă:** colțul din stânga jos e acoperit de poza de profil pe
  desktop și de centru pe mobil — **textul stă în dreapta**, niciodată
  în stânga jos.
- **Structură:** fundal `#EBEEF8`; în dreapta, pe două rânduri:
  - „De la o interacțiune obișnuită, la o experiență de care oamenii își
    amintesc." — Archivo 800, `#10173D`;
  - dedesubt: „Website · Sistem · Automatizare" — Inter 600, `#2743B8`.
- **Consecvent:** exact promisiunea din `brand_fundatie.md`, cuvânt cu
  cuvânt.
- **Fără:** poză cu laptop, cod pe ecran, iconițe de tehnologii.

## 3. Oferta PDF

- **Dimensiune:** A4 portret (210 × 297 mm), 3-4 pagini.
- **Structură fixă:**
  1. **Copertă:** [SEMN] + „Ofertă pentru [numele business-ului]" + data.
  2. **Ce am înțeles:** situația clientului, în 3-5 propoziții, cu
     cuvintele lui (tiparul „Unde ești acum" din `tone_of_voice.md`).
  3. **Ce propun:** pachetul — **exact** numele, prețul, termenul și ce
     include din `offers.md`. Add-on-uri doar dacă au fost cerute.
  4. **Ce urmează:** pașii, termenul, 7 zile de stabilizare gratuită,
     răspuns în 24h, contact.
- **Ierarhia tipografică:**
  | Nivel | Font | Mărime |
  |---|---|---|
  | Titlu pagină | Archivo 800 | 28 pt |
  | Subtitlu | Archivo 700 | 16 pt |
  | Text | Inter 400 | 11 pt, interlinie 1,5 |
  | Preț | Archivo 800 | 24 pt, `#2743B8` |
- **Elemente reutilizabile:** copertă, subsol cu [SEMN] + nume + e-mail
  pe fiecare pagină, cutia de preț.
- **Consecvent:** prețurile și termenele copiate din `offers.md` —
  niciodată scrise din memorie; fără tarif orar; copywriting doar ca
  add-on.
- **Poate varia:** doar pagina 2 (situația clientului) și add-on-urile.

## 4. Semnătura de e-mail

- **Dimensiune:** maximum 600 px lățime, maximum 4 rânduri.
- **Structură:**
  ```
  Andreea Sandu
  Digital Products & Experiences
  [site] · [e-mail]
  Răspund în maximum 24h.
  ```
- **Tipografie:** numele în bold, `#10173D`; restul text normal,
  `#263568`; site-ul în `#2743B8`. Fără imagini mari, fără citate, fără
  iconițe de rețele sociale colorate.
- **Consecvent:** aceeași în toate e-mailurile.

## Ce rămâne neschimbat peste tot

1. Un singur accent de culoare (`#2743B8`).
2. Archivo pentru titluri, Inter pentru text.
3. Promisiunea scrisă identic, cuvânt cu cuvânt.
4. [SEMN] în aceeași poziție pe același tip de material.
5. Prețuri doar din `offers.md`.
