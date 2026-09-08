# AgentMarke

Repo pentru sistemul de generare de conținut LinkedIn/Facebook al
Andreei (brand Andreea Tech) — vezi `content_agent/`.

## Regulă obligatorie — orice cerere de conținut LinkedIn/Facebook

Când Andreea cere o postare, idei de conținut, sau orice material pentru
**LinkedIn sau Facebook**, folosește **exclusiv**:

- `content_agent/prompts/linkedin_prompt.md` pentru LinkedIn.
- `content_agent/prompts/facebook_prompt.md` pentru Facebook.
- Context real din `content_agent/context/` și `content_agent/knowledge/`
  (brand, audiență, oferte/prețuri, ton, portofoliu, FAQ, exemple reale).

**Nu folosi alte skill-uri generice** (ex. `/marketing-copy` sau orice alt
skill de copywriting din setul personal al utilizatoarei) pentru acest
tip de cerere — acest repo are propriul sistem, testat și aprobat de
Andreea, mai specific și mai bine calibrat decât un skill generic.

Dacă Andreea nu specifică platforma (LinkedIn sau Facebook), **întreabă
explicit înainte să scrii** — nu presupune și nu amesteca regulile celor
două prompturi. Detalii complete în `content_agent/CLAUDE.md` și
`content_agent/prompts/README.md`.
