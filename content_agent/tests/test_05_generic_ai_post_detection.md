# Test 05 — Auditorul trebuie să prindă o postare generică de AI

**Tip:** negativ / calitate
**Etapă vizată:** Auditor (nu Writer — testăm direct rubrica de audit pe
un text deja scris, deliberat slab)

## INPUT

```
Auditează această postare (LinkedIn):

"In today's fast-paced digital world, every business needs a strong
online presence. Having a website is more important than ever before.
Contact us today to learn more about our services and take your business
to the next level!"
```

## EXPECTED

Auditorul trebuie să dea:
- `AI_GENERICNESS`: scor mic (0-1) — exact tiparele din
  `knowledge/examples/bad_posts.md` („In today's fast-paced digital
  world...").
- `HOOK`: scor mic — nu oprește scroll-ul, e o deschidere generică.
- `FACTUAL_ACCURACY`: PASS (nu conține cifre inventate, doar e slabă
  calitativ) — arată că gate-ul de fapte și scorul de calitate sunt
  separate.
- `SCORE` sub pragul de 25 → **REVISE**, cu criteriile slabe identificate
  explicit (AI_GENERICNESS, HOOK).

**Nu e acceptabil:** auditorul aprobă acest text, sau dă un scor general
fără să identifice concret ce e slab.
