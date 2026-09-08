# Log postări generate

> Scop: Etapa 2 (Content Strategist) din `prompts/linkedin_prompt.md` și
> `facebook_prompt.md` cere „nu repeta categoria/formatul folosit ultima
> dată" — regulă care nu funcționează cross-sesiune fără o evidență
> persistentă. Acest fișier e evidența. **Se actualizează după fiecare
> postare finală aprobată** (adaugi un rând, nu ștergi istoricul).
>
> Pentru LinkedIn, verifică ultimele 1-2 rânduri cu Platformă=LinkedIn
> înainte să alegi categoria/formatul la Etapa 2 — nu repeta niciuna din
> ele. Pentru Facebook nu există rotație strictă de categorie (vezi
> `facebook_prompt.md`), dar tot verifici să nu repeți hook-ul/unghiul.

| Data | Platformă | Categorie temă | Format | Obiectiv | Titlu | Fișier |
|---|---|---|---|---|---|---|
| 2026-09-08 | Facebook | — (fără rotație strictă) | problem→solution | autoritate/educațional | FB — Programări pierdute în telefon/WhatsApp/Excel | `outputs/facebook/2026-09-08-programari-pierdute-sistem-manual.md` |
| 2026-09-08 | Facebook | — (fără rotație strictă) | problem→solution | relatable/educațional | FB — Nu vezi unde se scurg banii din business | `outputs/facebook/2026-09-08-lipsa-vizibilitate-dashboard.md` |
| 2026-09-08 | Facebook | — (fără rotație strictă) | before→after | relatable/educațional | FB — Seara dinainte de eveniment, verificat manual cine a plătit | `outputs/facebook/2026-09-08-vanzare-bilete-evenimente-manual.md` |
| 2026-09-08 | LinkedIn | Antreprenoriat / Product Leadership | lecție de business | autoritate/educațional | Duolingo a cerut angajaților să fie evaluați după cât de mult folosesc AI | `outputs/linkedin/2026-09-08-duolingo-mandat-ai-esuat.md` |
| 2026-09-08 | LinkedIn | Automatizare / Product Development | mit (automatizarea elimină omul) | autoritate/educațional | Automatizare = mai puțină muncă repetitivă, nu mai puțin om | `outputs/linkedin/2026-09-08-automatizare-nu-inseamna-eliminarea-omului.md` |
| 2026-09-08 | LinkedIn | UX | greșeală frecventă | autoritate/educațional | Cea mai frecventă greșeală de UX pe care o văd la fondatori | `outputs/linkedin/2026-09-08-greseala-ux-cassian-voicu.md` |

## Cum adaugi un rând nou

După ce o postare trece de Etapa 5 (Auditor, `APPROVE`) și e salvată în
`outputs/linkedin/` sau `outputs/facebook/`, adaugi un rând aici cu:
data, platforma, categoria de temă (pentru LinkedIn — din lista de 14 din
`linkedin_prompt.md` Etapa 2; pentru Facebook, „—" dacă nu se aplică),
formatul (postare/articol/opinie/mit/etc.), obiectivul, titlul, și calea
către fișierul salvat.
