# Echipa LinkedIn — flux cu agenți separați

> Doar pentru **LinkedIn**. Facebook rămâne pe `facebook_prompt.md`, fără
> echipă. Cererile de conținut LinkedIn în Claude Code rulează implicit
> prin fluxul de aici; `linkedin_prompt.md` rămâne sursa regulilor (agenții
> îl citesc, nu îl duplică) și varianta pentru Claude Project pe claude.ai.
>
> De ce echipă și nu un singur prompt: în varianta cu un singur prompt,
> același model scrie și se auditează singur, în aceeași conversație — și
> e blând cu propriile greșeli. Aici verificatorii primesc doar
> rezultatul, fără raționamentul din spate.

## Cine e în echipă

Definițiile sunt în `.claude/agents/`:

| Rol | Agent | Răspunde cu |
|---|---|---|
| 1. 🧠 Directorul de marketing | `linkedin-director` | PLAN / BRIEF / AVIZ FAVORABIL-NEFAVORABIL |
| 2. ✍️ Agentul de text | `linkedin-text-writer` | doar textul: postarea, întrebarea, comentariul plantat, hashtag-urile (poza e a agentului de poză) |
| 3. 🖼️ Agentul de poză | `linkedin-image-prompt` | prompt de lipit în ChatGPT, format 4:5 |
| 4. 🔍 Verificatorul | `linkedin-verifier` | APROBAT / RESPINS |
| 5. 👀 Corectorul de logică | `linkedin-clarity-reader` | CLAR / NECLAR |
| 6. 🎯 Coordonatorul | conversația principală Claude Code | — |

Verificatorul nu verifică limitele pentru TikTok: echipa e doar pentru
LinkedIn. Regulile se adaugă când apare un prompt calibrat pentru TikTok.

## Cum circulă o postare

```
Director (BRIEF) → Writer ─┬→ Verificator ─┐
                           └→ Agent poză  ─┤→ Director (AVIZ) → Andreea
            Corector (doar textul) ────────┘
```

Pașii coordonatorului:

1. **Brief** — cheamă `linkedin-director` cu sarcina BRIEF (+ tema, dacă
   Andreea a dat una, + postarea din planul săptămânii, dacă există).
2. **Scriere** — cheamă `linkedin-text-writer` cu brief-ul complet.
3. **Poză** — cheamă `linkedin-image-prompt` cu brief-ul + postarea.
4. **Verificare, în paralel:**
   - `linkedin-verifier` primește brief-ul + postarea + promptul de poză.
     **Nu** primește „Nota pentru echipă" a writerului ca argument — doar
     ca listă de verificat.
   - `linkedin-clarity-reader` primește **doar** textul postării și
     comentariul plantat. Fără brief, fără titlu, fără context.
5. **Revizie** — dacă RESPINS sau NECLAR: trimite writerului (sau
   agentului de poză, dacă problema e acolo) exact problemele numite, apoi
   reia pasul 4. **Maximum 2 revizii.**
6. **Aviz** — cheamă `linkedin-director` cu sarcina AVIZ, cu brief-ul,
   varianta finală și ambele verdicte. Un aviz NEFAVORABIL consumă tot
   o revizie din cele 2.
7. **Livrare** — salvează și trimite fișierul final Andreei (vezi mai jos).

Dacă după 2 revizii tot nu trece, se livrează cea mai bună variantă
**marcată explicit**: „Nu a trecut: [verdict], probleme rămase: [...]" —
niciodată prezentată ca aprobată.

Coordonatorul nu livrează o postare cu observații nerezolvate ale
corectorului, chiar dacă verdictul e CLAR — dacă au rămas, o citește el
însuși ca Andreea și, dacă o frază nu are sens, o trimite înapoi, nu o
lasă „la alegerea ei". (Regulă adăugată după prima postare, 2026-09-27,
care a trecut cu fraze fără sens.)

Coordonatorul poate repara singur doar lucruri mecanice (diacritice, un
spațiu, un hashtag duplicat). Orice schimbare de sens trece înapoi prin
writer și verificare.

## Planul săptămânal și statisticile

1. Andreea trimite capturi de ecran cu statisticile postărilor.
2. Coordonatorul transcrie cifrele **exact cum apar în captură** în
   `content_agent/stats/linkedin_stats.md` (un rând per postare per
   captură, cu data capturii). Ce nu se citește clar → „?", nu se ghicește.
   Agenții nu văd capturile — văd doar fișierul.
3. Cheamă `linkedin-director` cu sarcina PLAN. Planul se salvează în
   `content_agent/plans/linkedin/AAAA-Wss.md` (ex. `2026-W40.md`).

## Salvare — tot ce produc agenții, pe `main`

La decizia Andreei (2026-09-27): tot ce produce echipa se salvează în
repo și se urcă pe `main`, nu doar postarea finală.

- **Postarea** → `content_agent/outputs/linkedin/AAAA-LL-ZZ-titlu-scurt.md`,
  cu secțiunile, în ordine: antet (data, obiectiv, categorie, format,
  exemplu central) · Titlu · Postare · Hashtag-uri · Prompt imagine
  (ChatGPT) · Închidere · **Brief** (blocul directorului) ·
  **Verificare** (verdictul final al verificatorului) · **Claritate**
  (verdictul final al corectorului) · **Aviz** · **Istoric revizii**
  (fiecare RESPINS/NECLAR/NEFAVORABIL și ce s-a schimbat — gol dacă a
  trecut din prima).
- **Rând nou** în `content_agent/outputs/log.md` (regulile de acolo).
- **Planul** → `content_agent/plans/linkedin/`.
- **Statisticile** → `content_agent/stats/linkedin_stats.md`.
- **Feedback de stil** de la Andreea → `content_agent/context/preferinte.md`.

Apoi commit cu mesaj clar (ex. „Add LinkedIn post: Bookora — ...") și
push pe `main`. Dacă sesiunea lucrează pe alt branch, se urcă și pe
branch-ul sesiunii, dar `main` rămâne destinația finală.
