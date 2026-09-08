# Publicare directă pe Facebook

Script care ia o postare deja aprobată din `content_agent/outputs/
facebook/` și o publică pe pagina Facebook Andreea Tech, prin Meta Graph
API. **Nu rulează niciodată singur.**

## Cum îl folosești (fără terminal)

Nu deschizi tu terminalul — ceri direct, într-o conversație Claude Code
pe acest repo: „publică postarea de la Bookora pe Facebook". Claude
citește fișierul, îți arată exact textul (postare + hashtag-uri +
comentariul plantat) aici, în chat, și rulează scriptul doar după ce
confirmi explicit ("da, publică"). Fișierul se identifică din
`content_agent/outputs/log.md` sau din numele lui, nu prin ghicit.

**Regulă pentru Claude, nu doar pentru tine:** `--yes` (care sare peste
promptul interactiv din terminal) se folosește *numai* după ce Andreea a
confirmat explicit, în conversație, exact acest fișier — niciodată din
inițiativă proprie, niciodată „ca să testez", niciodată pe un fișier
diferit de cel arătat.

## Ce trebuie să faci tu, o singură dată (partea pe care n-o pot face eu)

1. **Creezi o aplicație pe Meta for Developers** (developers.facebook.com
   → My Apps → Create App → tip „Business").
2. **Găsești/generezi un Page Access Token** pentru pagina Andreea Tech,
   cu permisiunile `pages_manage_posts` și `pages_read_engagement`. Cel
   mai simplu: Graph API Explorer (developers.facebook.com/tools/explorer)
   → selectezi aplicația → selectezi pagina → generezi tokenul.
3. **Token-ul generat direct din Explorer expiră repede** (ore/zile).
   Pentru ceva stabil, schimbă-l pe un token „long-lived" (Graph API are
   un endpoint de exchange pentru asta — caută „exchange for long-lived
   page access token" în documentația Meta, se schimbă des, nu-ți dau aici
   un pas exact ca să nu fie depășit) — sau, și mai stabil, creezi un
   **System User** în Business Manager și generezi un token de-acolo, care
   nu expiră automat la fel de des.
4. **Găsești Page ID-ul** paginii (Setări pagină → About, sau din același
   Graph API Explorer, `/me/accounts`).
5. Copiezi `content_agent/publish/.env.example` ca `.env`, în același
   folder, și completezi `FACEBOOK_PAGE_ID` și
   `FACEBOOK_PAGE_ACCESS_TOKEN`. **Nu-l trimiți niciodată în chat, nu-l
   pui în alt fișier din repo** — `.env` e deja în `.gitignore`.

## Instalare

```bash
pip install -r content_agent/publish/requirements.txt
```

## Folosire

Întâi testezi fără să publici nimic:

```bash
python content_agent/publish/facebook_publish.py content_agent/outputs/facebook/2026-09-08-programari-pierdute-sistem-manual.md --dry-run
```

Cu imagine (pregătită manual, vezi mai jos):

```bash
python content_agent/publish/facebook_publish.py content_agent/outputs/facebook/2026-09-08-programari-pierdute-sistem-manual.md --image ~/Desktop/poza.jpg
```

Fără `--dry-run`, publică efectiv — dar tot îți arată textul și cere
„da" explicit înainte.

## Ce NU face scriptul

- **Nu generează imaginea** — „Idee de imagine" din fișier rămâne un
  concept text; faci imaginea separat (Canva, un generator AI) și o dai
  cu `--image`.
- **Nu rulează pe cadență/automat** — nu e un cron job, nu publică
  singur. Fiecare rulare e o decizie a ta, pentru un fișier anume.
- **Nu publică pe LinkedIn** — API-ul LinkedIn e mult mai restrictiv
  (aprobare de aplicație), nu e acoperit aici. Pentru LinkedIn rămâne
  copy-paste manual sau Buffer.

## Dacă vrei să-l rulezi pe cadență (opțional, mai târziu)

Odată ce ești confortabilă cu scriptul rulat manual, poți programa un
cron job local sau un GitHub Action care rulează automat scriptul pe un
fișier ales — dar asta înseamnă și mai puțină verificare umană înainte
de publicare, deci nu e ceva de configurat din prima. Discutăm separat
dacă ajungi acolo.
