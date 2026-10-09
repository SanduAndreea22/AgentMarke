# Content Kit — Arhitectura (etapa 4)

> Făcută de `produs-arhitect`. Aprobată de Andreea pe 2026-10-09.
> Lungimea postării: fiecare om o alege în fișă; implicit 350-450 de
> cuvinte (propunerea coordonatorului, aprobată odată cu structura).

## 1. Cum arată kitul

Kitul e un singur Claude Project, cu 3 cuvinte-comandă: **IDEI**, **SCRIE**,
**VERIFICĂ**. Dacă omul scrie liber, fără comandă, kitul îl întreabă care
dintre cele 3 îi trebuie.

- **Instrucțiunile proiectului:** cele 3 roluri și regulile comune (doar
  fapte din fișă, română vorbită, fără clișee de AI).
- **Fișierele de cunoștințe:** un singur fișier, Fișa de brand completată.
- **VERIFICĂ se face într-o conversație nouă**, unde omul lipește doar
  textul postării. Așa nu verifică cel care a scris.

## 2. Fișa de brand

Se completează o singură dată. Fiecare câmp are un exemplu de un rând.

1. Cine ești și ce faci, într-o propoziție.
2. Cui vorbești: clientul tău, în cuvinte de zi cu zi.
3. Ce problemă îi rezolvi.
4. Fraze pe care le spun clienții tăi (2-5, exact cum le-ai auzit).
5. **Fapte adevărate despre mine și afacerea mea**: servicii, ani,
   proiecte, rezultate pe care le poți dovedi. Kitul nu afirmă nimic din
   afara acestei liste.
6. Ce oferi și ce vrei să facă cititorul după ce citește.
7. Ce NU vrei să apară: nume de clienți, promisiuni, subiecte.
8. Cum vorbești: 3 cuvinte despre ton; „tu” sau „dumneavoastră”.
9. Cuvinte pe care le folosești și cuvinte pe care nu le folosești
   niciodată.
10. 1-3 texte scrise de tine care sună ca tine.
11. Temele tale (3-5).
12. Câte postări pe săptămână, în ce zile și cât de lungi (implicit:
    350-450 de cuvinte).

## 3. Cele 3 roluri

### IDEI (din directorul: PLAN + BRIEF)

- **Primește:** fișa și, opțional, titlurile ultimelor postări, pe care le
  cere el.
- **Dă înapoi:** 2-3 idei. Pentru fiecare: ziua, tema, situația clientului,
  unghiul, de ce acum și faptele din fișă pe care se sprijină.
- **Reguli:**
  - temele se rotesc și nu se repetă;
  - formatul implicit e „situație trăită de client → ce faci diferit → ce
    se schimbă pentru el”;
  - un singur segment de client pe postare.
- **Cere informații** când fișa nu are teme sau fapte.
- **Refuză să inventeze** proiecte, clienți, rezultate sau știri.

### SCRIE (din writer)

- **Primește:** o idee („SCRIE 2”) sau o temă într-o propoziție.
- **Dă înapoi:** postarea, 3-5 hashtag-uri și o notă cu faptele folosite,
  fiecare legată de câmpul 5.
- **Reguli:**
  - hook-ul nu pornește dintr-o generalizare;
  - o singură idee și un singur exemplu;
  - fără negări absolute și fără fraze care sună frumos, dar nu spun
    nimic;
  - întrebarea de final are răspuns în câteva secunde;
  - lungimea e cea din câmpul 12.
- **Un fapt care nu e în fișă** apare ca `[DE COMPLETAT: …]` și nu se
  inventează niciodată.

### VERIFICĂ (din verificator + cititorul fără context)

- **Primește:** doar textul postării, într-o conversație nouă.
- **Dă înapoi:**
  - `VERDICT: GATA DE POSTAT | DE REPARAT`;
  - „Ce am înțeles”, într-o propoziție;
  - „Unde m-aș opri”, cu citat;
  - probleme numerotate, fiecare cu citat → ce pui în loc.
- **Reguli:**
  - faptele sunt poartă dură: orice afirmație care nu e în câmpul 5 duce
    la DE REPARAT;
  - verifică și cuvintele interzise, gramatica și diacriticele;
  - nu există observații opționale.
- **Nu inventează un fapt ca să repare textul.** Întreabă: „e adevărat?
  dacă da, adaugă-l în fișă; dacă nu, scoate fraza”.
- După cel mult 2 reparații, omul postează sau renunță.

## 4. Ghidul de pornire (5 pași)

1. Intri pe claude.ai. Disponibilitatea proiectelor în planul gratuit e
   [DE VERIFICAT]. În etapa 1 a produsului descrieri-anunturi s-a găsit
   „Free: până la 5 Proiecte” pe claude.com/pricing; se reconfirmă înainte
   de livrare.
2. Creezi un Project și lipești instrucțiunile.
3. Completezi fișa (30-45 de minute) și o încarci în fișierele proiectului.
4. Prima rundă: IDEI → SCRIE 1 → conversație nouă → VERIFICĂ.
5. Săptămânal: luni IDEI, apoi SCRIE și VERIFICĂ pentru fiecare postare.

## Bloc final

- **Dimensiune MVP:** 3 fișiere, cam 5 pagini: instrucțiuni (2-3), fișă
  (1-2), ghid (1).
- **Timp estimat de creare:** 10-12 ore, din care 3 ore de test pe fișa
  Andreei.
- **FAPTE PERMISE:**
  - Andreea a construit și folosește o echipă de agenți AI pentru
    LinkedIn: director, agent de text, agent de poză, verificator,
    corector. Surse: `content_agent/prompts/linkedin_team.md` și
    `.claude/agents/linkedin-*.md`.
  - Sistemul are o regulă care nu lasă să apară fapte inventate și un
    cititor fără context care arată unde s-ar opri cineva din citit.
  - Kitul e o versiune simplificată, cu 3 roluri.
- **INTERZIS:**
  - urmăritori, reach, clienți, „îți garantează”;
  - cifre de timp economisit, pentru că nu sunt măsurate;
  - testimoniale sau „testat de X oameni” înainte de test;
  - „scrie perfect ca tine”, „zero greșeli”;
  - alte platforme sau limbi;
  - numele „Claude Content Kit” și orice sugestie de produs oficial
    Anthropic, până la verificarea regulilor de brand.
- **Scos din sistemul original:**
  - agentul de poză (cere alt instrument);
  - avizul directorului (îl acoperă VERIFICĂ);
  - planul din statistici (ar sugera reach);
  - research pe web (risc de fapte inventate);
  - scorul din 30 și momentul WOW (nu sunt în definiție);
  - log-ul (îl înlocuiește întrebarea „ce ai postat recent?”);
  - bucla automată de revizii (o face omul);
  - regulile specifice Andreei (vin din fișă).
- **Ce se pierde:** verificarea e mai puțin independentă decât agenții
  separați din sistemul original. Conversația nouă reduce riscul, dar nu
  îl elimină.
