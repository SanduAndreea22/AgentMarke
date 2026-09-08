# Skill: content_ideas

**Status:** ✅ construit (v1)

## Ce face

Primește un topic + obiectiv + audiență + platformă și generează 5 unghiuri
de conținut distincte, gata de ales de Andreea. Nu scrie postarea finală —
doar unghiurile. Scrierea propriu-zisă se face în `skills/linkedin_post`
sau `skills/facebook_post`, pe unghiul ales.

## Când se folosește

- La începutul fluxului de creare de conținut, când există un topic dar nu
  și un unghi clar.
- Când Andreea cere "idei de conținut despre X".

## Input

```
Topic: [subiectul central]
Objective: [lead generation | authority/portfolio | educational]
Audience: [segment specific din context/audience.md, sau "default"]
Platform: [LinkedIn | Facebook | both]
```

Dacă lipsește un câmp, agentul întreabă înainte să genereze (nu presupune
obiectivul sau audiența implicit).

## Proces

1. Citește `context/brand.md`, `context/audience.md`,
   `context/content_strategy.md` și `knowledge/products_services.md`
   înainte să genereze idei.
2. Pentru fiecare unghi, verifică dacă se poate ancora într-un proiect
   real din portofoliu (nu obligatoriu, dar de preferat).
3. Generează exact 5 unghiuri, folosind tiparele din
   `context/content_strategy.md`:
   1. **Problem → solution**
   2. **Mistake → lesson**
   3. **Before → after**
   4. **Educational**
   5. **Contrarian**
4. Pentru fiecare unghi oferă: o propoziție de hook posibil + o notă
   scurtă de ce funcționează pentru audiența/obiectivul dat.
5. Nu scrie postarea completă în acest pas — doar unghiul + hook-ul
   ilustrativ.

## Output (format)

```
## Content Ideas: [Topic] — [Objective] — [Audience] — [Platform]

1. Problem → Solution
   Hook: "..."
   De ce funcționează: ...
   Portofoliu relevant: [proiect sau „—"]

2. Mistake → Lesson
   Hook: "..."
   De ce funcționează: ...
   Portofoliu relevant: [proiect sau „—"]

3. Before → After
   Hook: "..."
   De ce funcționează: ...
   Portofoliu relevant: [proiect sau „—"]

4. Educational
   Hook: "..."
   De ce funcționează: ...
   Portofoliu relevant: [proiect sau „—"]

5. Contrarian
   Hook: "..."
   De ce funcționează: ...
   Portofoliu relevant: [proiect sau „—"]

Alege un număr (1-5) pentru a continua cu postarea completă.
```

## Reguli

- Nu inventa proiecte de portofoliu — dacă niciunul din
  `knowledge/products_services.md` nu se potrivește, scrie „—" în loc să
  forțezi o referință.
- Nu inventa statistici sau rezultate în hook-uri.
- Hook-urile trebuie să fie specifice topicului dat, nu generice
  ("Vrei mai multe clienți?" e prea vag).
- Dacă `Platform: both`, generează unghiurile o singură dată (sunt
  transversale) — adaptarea per platformă se face la pasul următor
  (`linkedin_post` / `facebook_post`), nu aici.
- Nu folosi limbaj generic de AI — vezi `knowledge/examples/bad_posts.md`.

## Exemplu de apel

```
Topic: automatizarea rezervărilor pentru saloane
Objective: lead generation
Audience: proprietari de saloane
Platform: LinkedIn
```

→ agentul citește contextul, identifică Bookora ca portofoliu relevant,
generează cele 5 unghiuri conform formatului de mai sus.

## Pasul următor

După ce Andreea alege un unghi (ex. "ia ideea 3"), agentul trece la
`skills/linkedin_post` sau `skills/facebook_post` — **acei skill-uri nu
sunt încă construite** (vezi roadmap în `CLAUDE.md`). Până atunci, acest
skill se oprește la lista de idei.
