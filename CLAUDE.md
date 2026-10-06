# AgentMarke

Repo pentru sistemul de generare de conținut LinkedIn/Facebook al
Andreei (brand Andreea Tech) — vezi `content_agent/` — și pentru
crearea de produse digitale Andreea Tech — vezi `produse_digitale/`.

## Regulă obligatorie — orice cerere de conținut LinkedIn/Facebook

Când Andreea cere o postare, idei de conținut, sau orice material pentru
**LinkedIn sau Facebook — inclusiv cereri generice care nu numesc
platforma explicit** (ex. „idei pentru rețelele sociale", „ceva pentru
social media"), **citește integral și urmează exact**:

- Pentru LinkedIn: **fluxul cu echipă de agenți** din
  `content_agent/prompts/linkedin_team.md` (director → writer + agent de
  poză → verificator + corector → aviz; agenții sunt în `.claude/agents/`).
  Regulile de conținut rămân în `content_agent/prompts/linkedin_prompt.md`,
  pe care agenții îl citesc.
- `content_agent/prompts/facebook_prompt.md` pentru Facebook.
- Context real din `content_agent/context/` și `content_agent/knowledge/`
  (brand, audiență, oferte/prețuri, ton, portofoliu, FAQ, exemple reale) —
  fișierele se citesc **direct din acest repo** (Claude Code) sau din
  Project Knowledge, dacă rulează ca Claude Project; sunt aceleași
  fișiere, doar căi de acces diferite.

**Nu folosi alte skill-uri generice** (ex. `/marketing-copy` sau orice alt
skill de copywriting din setul personal al utilizatoarei) pentru acest
tip de cerere — acest repo are propriul sistem, testat și aprobat de
Andreea, mai specific și mai bine calibrat decât un skill generic. (Dacă
Andreea invocă explicit un alt skill, ex. tastează `/marketing-copy`
direct, asta îi rămâne alegerea — regula de mai sus previne doar alegerea
automată greșită.)

Dacă Andreea nu specifică platforma, **întreabă explicit înainte să
scrii** — nu presupune și nu amesteca regulile celor două prompturi. Dacă
cere **ambele platforme deodată**, rulează cele două prompturi separat, în
ordine, și livrează două postări distincte — niciodată una hibridă. Dacă
cere o platformă fără prompt dedicat (Instagram, TikTok, X etc.), spune
explicit că nu există încă un prompt calibrat pentru ea și întreabă cum
procedează — nu folosi `linkedin_prompt.md`/`facebook_prompt.md` ca
înlocuitor tăcut.

Detalii complete de folosire (setup, exemple, roadmap) în
`content_agent/prompts/README.md` — `content_agent/CLAUDE.md` documentează
doar gândirea de design din spate, nu mai e mecanismul de rulare.

## Salvare pe `main`

Tot ce produc agenții LinkedIn (postare, brief, verdicte, aviz, prompt de
imagine, planuri, statistici) se salvează în repo și se urcă pe `main` —
decizia explicită a Andreei (2026-09-27). Detalii în
`content_agent/prompts/linkedin_team.md`, secțiunea „Salvare".

## Produse digitale

Când Andreea cere un produs digital (sistem de prompturi, agenți/workflow
AI, șablon, workbook, checklist, ghid, toolkit, framework, mini-curs,
sistem pentru business, produs hibrid) sub brandul Andreea Tech, urmează
fluxul din `produse_digitale/README.md` și metodologia din
`produse_digitale/metodologie.md` — un agent `produs-*` pe etapă
(descoperire → definire → arhitect → creator → tester + cumpărător →
ladder-pret → pozitionare → lansare), cu „Vrei să trecem la următoarea
etapă?" și aprobarea explicită a Andreei între etape. Nu
folosi echipa LinkedIn pentru produse și nici invers. Totul se salvează pe
`main`, în `produse_digitale/produse/<nume-scurt>/`.

