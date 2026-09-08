# AgentMarke

Repo pentru sistemul de generare de conținut LinkedIn/Facebook al
Andreei (brand Andreea Tech) — vezi `content_agent/`.

## Regulă obligatorie — orice cerere de conținut LinkedIn/Facebook

Când Andreea cere o postare, idei de conținut, sau orice material pentru
**LinkedIn sau Facebook — inclusiv cereri generice care nu numesc
platforma explicit** (ex. „idei pentru rețelele sociale", „ceva pentru
social media"), **citește integral și urmează exact**:

- `content_agent/prompts/linkedin_prompt.md` pentru LinkedIn.
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
