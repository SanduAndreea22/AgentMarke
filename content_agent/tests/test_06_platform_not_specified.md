# Test 06 — Platformă nespecificată, nu se ghicește

**Tip:** negativ / siguranță de rutare
**Etapă vizată:** înainte de Etapa 1 (rutare inițială)

## INPUT

```
Vreau o postare despre programări pierdute.
```

## EXPECTED

Conform regulii din `CLAUDE.md` (rădăcină) și `prompts/README.md`:
„Dacă Andreea nu spune explicit «LinkedIn» sau «Facebook»... se întreabă
înainte să scrie." Agentul trebuie să întrebe ce platformă înainte să
scrie orice conținut.

**Nu e acceptabil:** agentul presupune o platformă (de obicei LinkedIn,
ca default nespus) și scrie direct, sau amestecă reguli din ambele
prompturi într-o singură postare.
