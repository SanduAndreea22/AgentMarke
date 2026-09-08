# Cum se folosește

Înlocuiește complet SM Writer. Două moduri de folosire, la alegere —
contextul (`context/` + `knowledge/`) e același în ambele.

## Modul 1 — direct în Claude Code, pe acest repo (recomandat, mai simplu)

Nu trebuie configurat nimic. Într-o conversație Claude Code pe repo-ul
`AgentMarke`, ceri direct, de exemplu:

```
Generează materialul zilei pentru LinkedIn. Urmează
content_agent/prompts/linkedin_prompt.md.
```

sau, pentru Facebook, la fel dar cu `facebook_prompt.md`. Claude citește
fișierele din `context/`, `knowledge/` și `prompts/` direct din repo și
rulează pipeline-ul pe loc (poți cere și o singură etapă — „doar
research", „acum scrie postarea"). Nu ai nevoie de cont separat, de
upload de fișiere sau de Claude Projects.

**Important:** spui mereu explicit platforma („pentru LinkedIn" / „pentru
Facebook") când ceri conținut. Cele două prompturi trăiesc în același
repo, nu în Proiecte separate ca la Modul 2 — dacă nu specifici, Claude
trebuie să te întrebe, nu să ghicească sau să amestece stilurile.

Nu trebuie neapărat să numești fișierul explicit (`linkedin_prompt.md`) —
Claude rutează automat pe baza cuvântului „LinkedIn"/„Facebook" din
cerere, conform regulii din `/CLAUDE.md` (rădăcina repo-ului). Poți numi
fișierul oricum, ca siguranță suplimentară.

Reguli complete de rutare — ce se întâmplă dacă ceri ambele platforme
deodată, sau o platformă fără prompt dedicat (Instagram, TikTok etc.),
sau dacă un skill generic din setul tău personal ar putea prelua cererea
din greșeală — sunt în `/CLAUDE.md` la rădăcina repo-ului, nu se
duplică aici.

## Modul 2 — Claude Project pe claude.ai (opțional, dacă vrei acces fără Claude Code)

Utilă doar dacă vrei să generezi conținut și dintr-un loc fără Claude Code
(telefon, alt calculator). Setup o singură dată:

1. Pe claude.ai, creează două Proiecte: **„Andreea Tech — LinkedIn"** și
   **„Andreea Tech — Facebook"**.
2. În fiecare Proiect, la **Project Knowledge**, încarcă aceleași fișiere
   (identice în amândouă):
   - `content_agent/context/brand.md`
   - `content_agent/context/audience.md`
   - `content_agent/context/offers.md`
   - `content_agent/context/tone_of_voice.md`
   - `content_agent/context/content_strategy.md`
   - `content_agent/knowledge/products_services.md`
   - `content_agent/knowledge/faq.md`
   - `content_agent/knowledge/competitors.md`
   - `content_agent/knowledge/examples/good_posts.md`
   - `content_agent/knowledge/examples/bad_posts.md`
   - `content_agent/knowledge/sm_writer_prompt.md` (context istoric, opțional)
3. În **Custom Instructions**:
   - Proiectul LinkedIn → conținutul din `linkedin_prompt.md`.
   - Proiectul Facebook → conținutul din `facebook_prompt.md`.

## Folosire zilnică

Într-o conversație nouă în Proiectul potrivit, scrii ceva de genul:

```
Generează materialul zilei. Temă: [dacă ai una anume, altfel las-o pe el
să aleagă din rotația de teme]. Obiectiv: autoritate (default) / lead
generation.
```

Claude citește automat Project Knowledge-ul și livrează: titlu, postare,
hashtag-uri, idee de imagine, închidere (CTA sau întrebare + comentariu
plantat).

## Când actualizezi contextul

Dacă schimbi prețuri, portofoliu sau reguli de ton, editezi fișierul din
`content_agent/context/` sau `content_agent/knowledge/` aici, în repo (cu
ajutorul meu, în Claude Code), apoi reîncarci fișierul actualizat în
Project Knowledge pe claude.ai — repo-ul rămâne sursa de adevăr, Proiectul
e doar interfața de folosire zilnică.

## Roadmap (nu e construit încă)

- **Postare directă pe LinkedIn/Facebook**: Claude Projects generează
  doar textul — nu publică nimic automat. Publicarea reală ar necesita un
  instrument separat (Buffer/Zapier/Make, care au integrare directă cu
  LinkedIn și Meta și se configurează rapid, fără cod) sau un mic
  automatism construit de Andreea (Django + API-urile oficiale LinkedIn/
  Meta) — API-ul LinkedIn pentru postare cere aprobare de aplicație, e mai
  greoi decât Meta.
- **Generare de imagine**: Claude Projects nu generează imagini. „Idee de
  imagine" din livrare e gândită ca prompt de folosit manual într-un
  instrument de generare (Canva, Ideogram, DALL·E etc.) sau, ulterior,
  ca input automat către un API de imagine, dacă se construiește un
  automatism separat.

Ambele sunt fezabile ca etape viitoare, dar nu fac parte din sistemul de
azi — sistemul de azi produce text gata de copy-paste, aprobat manual de
Andreea înainte de publicare.
