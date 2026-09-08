# Cum se folosește — Claude Project, nu Claude Code

Acest sistem nu rulează în Claude Code. Se folosește direct pe claude.ai,
ca **Claude Project**. Înlocuiește complet SM Writer.

## Setup (o singură dată)

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
