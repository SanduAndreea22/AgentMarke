# Produse & Servicii — Portofoliu Real

> Sursă: site-ul live (`SanduAndreea22/andreeatech`) — pagina Portofoliu
> (`projects.html`) și pagina Produse (`products.html`). Singura sursă de
> adevăr pentru referințe de portofoliu în conținut. Agentul nu are voie
> să menționeze alt proiect decât cele de mai jos, și nu are voie să
> adauge cifre de rezultat care nu sunt confirmate aici (`result_highlight`
> e un câmp opțional per proiect — dacă lipsește, nu se inventează).

## Portofoliu (sisteme pentru clienți / demo) — pagina „Portofoliu"

> Citat FAQ: „Proiectele din Portofoliu (Al Noir, Platform Tickets,
> Bookora) sunt exemple din ce pot construi, nu produse de vânzare."

### Al Noir

- Sistem de rezervări, plăți prin Stripe, gestiune de inventar, dashboard.
- Bun pentru unghiuri despre: restaurante, saloane, clinici, orice business
  bazat pe rezervări/programări; plăți online; vizibilitate operațională.

### Bookora

- Sistem de booking/programări.
- Bun pentru unghiuri despre: eliminarea gestiunii manuale
  (telefon/WhatsApp/Excel) a programărilor.

### Platform Tickets

- Platformă de ticketing: integrare Stripe, cod QR, generare PDF.
- Bun pentru unghiuri despre: evenimente, vânzare de bilete online,
  automatizarea proceselor manuale.

### Cassian & Voicu

- Demo cabinet de avocatură — doar zona de admin, fără portal de client.
- Bun pentru unghiuri despre: servicii juridice, digitalizare pentru
  domenii care nu se gândesc automat la „sistem" (nu doar HoReCa/beauty).

### Django E-Commerce

- Marketplace online: checkout securizat, gestiune avansată de inventar.
- Live.
- Bun pentru unghiuri despre: retail/e-commerce, plăți online, gestiune
  de stoc — dincolo de zona strict de programări/rezervări.

Notă: pagina de Portofoliu spune explicit că proiectele afișate sunt din
zona rezervări/programări, dar principiile (flux clar, automatizat, care
ține pasul cu afacerea) „se aplică la orice proces repetitiv, indiferent
de domeniu" — util pentru unghiuri de conținut către alte industrii.

## Detaliu tehnic real — Bookora

De folosit ca dovadă concretă de expertiză tehnică (nu doar afirmație
generică „am construit un sistem de rezervări"), cu grijă să rămână
explicat pe înțelesul cuiva non-tehnic dacă apare într-o postare (vezi
`audience.md`): problema rezolvată e suprapunerea de programări (double
booking) — soluția blochează rândul din baza de date în timpul creării
unei rezervări (Django Transaction API, `select_for_update`), iar
sloturile disponibile se calculează în incremente de 30 de minute,
filtrând rezervările deja confirmate și indisponibilitatea furnizorului.

## Proiect principal, nelansat — Clarito

- **Ce face:** planner digital care unifică gestionarea emoțiilor și a
  bugetului personal — combină organizarea personală, reflecția
  emoțională și gestionarea financiară într-o singură experiență.
- **Relație cu Emotional Planner/MyBudget:** e evoluția/unificarea celor
  două produse de mai sus într-un singur produs — Emotional Planner și
  MyBudget sunt acum precursori/parte din el, nu proiecte fără legătură.
- **Status: în dezvoltare, nelansat încă** — se menționează explicit ca
  „în construcție"/„urmează", niciodată ca disponibil de testat acum.
- **Cum se folosește în conținut:** e proiectul principal al Andreei,
  direcția pe termen lung alături de brandul personal — poate fi folosit
  ca fir roșu recurent (nu în fiecare postare), nu doar ca exemplu
  punctual.

## Produse proprii — pagina „Produse" (Early Access, gratuite)

> Citat: „produse personale — pornite din nevoi personale, nu dintr-un
> brief". Diferite de Portofoliu: nu sunt construite pentru un client, sunt
> oferite direct.
>
> **Notă de denumire — de reținut:** site-ul afișează public aceste
> produse sub nume descriptive lungi, dar în conținut (LinkedIn/Facebook)
> Andreea le numește **MyBudget** și **Emotional Planner** — astea sunt
> numele de folosit în postări, nu variantele de pe site.

### Emotional Planner

- Nume pe site: „Planner de Echilibru Personal & Productivitate".
- Planner zilnic care urmărește starea alături de task-uri — planificare
  zilnică/săptămânală, obiective/obiceiuri/priorități, spațiu de reflecție.

### MyBudget

- Nume pe site: „Tracker Inteligent de Buget & Finanțe".
- Urmărește venituri, cheltuieli, limite de buget — evidență, privire de
  ansamblu, urmărirea economiilor/obiectivelor financiare.

## SM Writer — proiect propriu, exemplu valid de portofoliu

Agentul AI intern care generează zilnic materialul de LinkedIn al Andreei
(vezi `sm_writer_prompt.md`) — **e un proiect real, poate fi menționat ca
exemplu de portofoliu** (dovadă de expertiză în automatizare/AI/product),
nu doar context intern. „Nu e un concept, e ceva ce rulează acum."

## Reguli de nume — obligatoriu

Numele de conținut (nu cele de site, unde diferă) pentru portofoliu:
**Al Noir, Bookora, Platform Tickets, Cassian & Voicu, Django E-Commerce,
MyBudget, Emotional Planner, Clarito, SM Writer.** Astea sunt singurele
proiecte proprii care pot fi menționate ca experiență reală — „nu există
(încă) clienți, utilizatori externi sau studii de caz proprii care pot fi
citate ca atare". Clarito e singurul dintre ele nelansat — se menționează
mereu ca atare, niciodată ca disponibil acum.

## Reguli de utilizare în conținut

- Folosește **exact** numele din secțiunea „Reguli de nume — obligatoriu"
  de mai sus — nu variante prescurtate și nu numele lungi de pe site
  pentru MyBudget/Emotional Planner (vezi „Notă de denumire" mai sus). Nu
  se repetă lista aici, ca să nu se desincronizeze din nou dacă se adaugă
  proiecte noi (exact ce s-a întâmplat până la acest audit).
- Nu se inventează cifre de rezultat (ex. „+40% rezervări") pentru aceste
  proiecte fără confirmare explicită din partea Andreei (câmpul
  `result_highlight` din site, când există, e sursa validă).
- Proiectele din Portofoliu nu sunt neapărat clienți reali plătitori —
  agentul nu trebuie să le prezinte ca "am ajutat un client X să..." decât
  dacă Andreea confirmă explicit că e vorba de un client real.
