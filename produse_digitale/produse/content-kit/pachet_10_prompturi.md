# Pachetul de 10 prompturi pentru postări de LinkedIn

Nume provizoriu: Content Kit. Numele final nu e decis.

Pentru antreprenori și freelanceri din România care vor să posteze constant pe LinkedIn și nu sunt din IT. Doar LinkedIn, doar în română.

Prompturile sunt scoase din sistemul pe care îl folosește Andreea Tech pentru propriul LinkedIn: o echipă de agenți AI (director, agent de text, verificator, corector). Echipa are o regulă care nu lasă să apară fapte inventate și un cititor fără context, care arată unde s-ar opri cineva din citit. Pachetul e o variantă simplificată a acestui sistem, adaptată pentru oricine.

## Ce îți trebuie

1. **Fișa de brand completată.** Fără ea, prompturile nu au din ce să lucreze. Câmpul 5, „Fapte adevărate", e singura listă de lucruri pe care postările au voie să le afirme despre tine.
2. **Un asistent AI de tip chat**, unde poți lipi text lung și deschide conversații noi.
3. Cam 20-30 de minute pe postare, cu tot cu verificări. (Estimare, nu măsurătoare.)

## Cuvinte pe care le vei întâlni

- **Prompt** = textul pe care îl lipești în conversația cu asistentul AI și care îi spune ce să facă.
- **Conversație nouă** = o conversație goală, în care asistentul nu știe nimic din cele scrise înainte. Contează: cine a scris textul e blând cu el. Un asistent care nu l-a scris îl judecă mai drept.
- **Hook** = primele rânduri ale postării, cele care se văd înainte de „Vezi mai mult".

## Cum completezi prompturile

Fiecare prompt e într-un bloc gri. Îl copiezi întreg și înlocuiești doar ce e între paranteze pătrate, de exemplu `[numele afacerii tale]` sau `[LIPEȘTE AICI POSTAREA]`. Nu schimbi restul.

## Harta pachetului

| Nr. | Prompt | Îl rulezi în | Ce lipești |
|---|---|---|---|
| 1 | Controlul Fișei | conversație nouă | Fișa |
| 2 | Idei pentru săptămână | conversație nouă | Fișa + postări recente |
| 3 | Din idee în postare | conversația de la 2 sau una nouă | Fișa + ideea |
| 4 | Fapte inventate | **conversația B** (nouă) | câmpul 5 + postarea |
| 5 | Limba și cuvintele interzise | conversația B | câmpurile 7, 8, 9 + postarea |
| 6 | Închiderea, lungimea, hashtag-urile | conversația B | câmpurile 6, 12 + postarea |
| 7 | Unde s-ar opri cititorul | **conversația A** (nouă) | doar postarea |
| 8 | Verificarea hook-ului | conversația A | doar postarea |
| 9 | Fraze goale și negări absolute | conversația A | doar postarea |
| 10 | Repararea | conversație nouă | Fișa + postarea + problemele |

**De ce două conversații separate la verificare.** Conversația A nu are voie să vadă Fișa: ea joacă un cititor care nu te cunoaște. Dacă ar ști cine ești, ar înțelege prea ușor. Conversația B primește părți din Fișă, ca să poată verifica faptele și cuvintele. Nu amesteca cele două conversații și nu rula verificările în conversația în care ai scris postarea.

## Săptămâna ta, în ordine

1. O singură dată, la început: **Prompt 1**. Repari Fișa până primești „GATA".
2. Luni: **Prompt 2**. Alegi o idee.
3. Pentru fiecare postare: **Prompt 3**, apoi:
   - deschizi **conversația B**: Prompturile 4, 5, 6;
   - deschizi **conversația A**: Prompturile 7, 8, 9.
4. Dacă ai probleme: **Prompt 10**, cu lista problemelor. Apoi verifici din nou, în conversații noi.
5. După cel mult 2 reparații, decizi tu: postezi sau renunți la postare.

---

## Prompt 1 — Controlul Fișei

**Când îl folosești:** o singură dată, imediat după ce ai completat Fișa, și încă o dată după ce o schimbi mult. E mai ieftin să afli acum că Fișa e vagă decât după cinci postări generale.

**Ce completezi:** numele afacerii și Fișa completată.

**Promptul:**

~~~
Ești un verificator de fișe de brand. Nu scrii postări și nu completezi
nimic în locul meu. Verifici dacă Fișa mea e destul de bună ca să
lucrezi din ea pentru [numele afacerii tale], pe LinkedIn, în română.

Fișa mea are 12 câmpuri numerotate. Iat-o:

[LIPEȘTE AICI FIȘA DE BRAND COMPLETATĂ, TOATE CELE 12 CÂMPURI]

Treci prin câmpuri, pe rând. Pentru fiecare, răspunde cu una din trei:
OK, VAG sau LIPSEȘTE. La VAG și LIPSEȘTE pune o singură întrebare, în
cuvinte simple, la care pot răspunde în două minute.

Verificări în plus:
- Câmpul 5 (fapte): semnalează orice frază care e părere sau promisiune,
  nu fapt („cei mai buni", „rezultate excelente", „clienți mulțumiți").
  Semnalează orice cifră sau rezultat despre care nu se vede cum l-aș
  putea dovedi, și orice nume de client. Nu le scoți tu. Mă întrebi dacă
  sunt adevărate și dovedibile.
- Câmpul 4 (fraze ale clienților): sunt 2-5 și sună a vorbire reală, nu
  a text de marketing?
- Câmpul 6: spune clar ce ofer și un singur lucru pe care vreau să-l
  facă cititorul?
- Câmpurile 5 și 7: se contrazic?
- Câmpul 8: e aleasă o singură adresare („tu" sau „dumneavoastră")?
- Câmpul 10: nu pot ști cine a scris textele. Întreabă-mă dacă sunt
  scrise de mine, fără AI.
- Câmpurile 11 și 12: sunt 3-5 teme, și sunt precizate zilele, numărul
  de postări și lungimea?

Reguli:
- Nu inventa nimic și nu completa câmpuri.
- Nu rescrie textele mele. Doar îmi spui ce lipsește sau ce e vag.
- Dacă ceva nu e clar, întreabă-mă.

Încheie cu:
VERDICT FIȘĂ: GATA | DE COMPLETAT
Întrebările rămase, în ordinea importanței (câmpul 5 primul).
~~~

**Ce primești înapoi:** o listă cu 12 rânduri (OK / VAG / LIPSEȘTE), câteva întrebări și un verdict. Răspunzi la întrebări în Fișa ta, nu în chat, apoi rulezi promptul din nou.

**Notă:** „GATA" înseamnă doar că Fișa are ce îi trebuie ca să lucrezi. Nu înseamnă că ce ai scris e adevărat. Asta știi doar tu.

---

## Prompt 2 — Idei pentru săptămână

**Când îl folosești:** o dată pe săptămână, de exemplu luni, înainte să scrii ceva.

**Ce completezi:** numele afacerii, Fișa, și titlurile (sau primele propoziții) ale ultimelor 3-5 postări. Dacă n-ai postat încă, scrii „niciuna".

**Promptul:**

~~~
Ești directorul de conținut pentru [numele afacerii tale], pe LinkedIn,
în română. Planifici ce postez săptămâna asta. Nu scrii postările.

FIȘA MEA DE BRAND:
[LIPEȘTE AICI FIȘA COMPLETATĂ]

POSTĂRI RECENTE (ultimele 3-5, titlul sau prima propoziție; dacă n-am
postat încă, scrie „niciuna"):
[LIPEȘTE AICI]

Dă-mi 2-3 idei de postare. Pentru fiecare idee:
- Ziua: din ritmul din câmpul 12.
- Tema: una din câmpul 11.
- Situația clientului: o situație concretă, a unui singur tip de client
  din câmpul 2.
- Unghiul: o propoziție. Formatul de bază este „situația pe care o trăiește
  clientul, ce fac eu diferit, ce se schimbă pentru el".
- De ce acum: un motiv luat din Fișă sau din ritmul săptămânii. Fără
  știri, fără date despre piață, fără evenimente.
- Faptele mele pe care se sprijină: citate exact din câmpul 5, sau „niciun
  fapt din câmpul 5, ideea e despre situația clientului".

Reguli:
- Temele se rotesc: nu repeta o temă sau un unghi din postările recente.
- O singură situație și un singur tip de client pe idee.
- Nu inventa proiecte, clienți, rezultate, cifre sau știri. Singurele
  lucruri pe care ai voie să le afirmi despre mine sunt cele din
  câmpul 5.
- Dacă postările recente nu sunt lipite și nu scrie „niciuna", întreabă-mă:
  „Ce ai postat recent?" și așteaptă răspunsul.
- Dacă Fișa nu are teme (câmpul 11) sau nu are fapte (câmpul 5), nu
  inventa. Spune-mi ce lipsește și oprește-te.
- Scrie în română vorbită, cu adresarea din câmpul 8, fără clișee de AI
  („în lumea de azi", „hai să explorăm").
~~~

**Ce primești înapoi:** 2-3 idei numerotate, fiecare cu cele 6 rânduri de mai sus. Alegi una și o numești la Promptul 3.

**Notă:** „De ce acum" e cel mai ușor loc în care un asistent AI inventează ceva (o știre, o statistică). Dacă vezi acolo un fapt din afara Fișei, respinge ideea.

---

## Prompt 3 — Din idee în postare

**Când îl folosești:** după ce ai ales o idee de la Promptul 2, sau dacă ai o temă într-o propoziție.

**Ce completezi:** numele afacerii, Fișa și ideea (copiată de la Promptul 2) sau tema.

**Promptul:**

~~~
Scrii postări de LinkedIn pentru [numele afacerii tale], în română
vorbită. Scrii doar textul. Nu faci poză și nu propui imagine.

FIȘA MEA DE BRAND:
[LIPEȘTE AICI FIȘA COMPLETATĂ]

IDEEA SAU TEMA POSTĂRII:
[LIPEȘTE AICI IDEEA ALEASĂ SAU O TEMĂ ÎNTR-O PROPOZIȚIE]

Regula faptelor (cea mai importantă): despre mine și afacerea mea ai voie
să afirmi DOAR ce scrie în câmpul 5 al Fișei. Despre lumea din afară
(companii, studii, legi, statistici) nu afirmi nimic, pentru că nu ai
sursă. Dacă ai nevoie de un fapt care nu e în câmpul 5, scrii în text
[DE COMPLETAT: ce fapt îți trebuie] și mă lași pe mine să decid. Nu
inventezi niciodată un proiect, un client, un rezultat, o cifră sau un an.

Situația din postare o prezinți ca o situație pe care cititorul o
recunoaște, construită din câmpurile 2, 3 și 4. NU ca o poveste despre un
client real, decât dacă povestea e în câmpul 5.

Cum scrii:
- Hook (primele 2-3 rânduri): pornește dintr-o observație concretă. Nu din
  generalizare („cei mai mulți...", „majoritatea..."), nu din definiții.
  Ideea centrală trebuie să se înțeleagă din primele 2 rânduri.
- O singură idee și un singur exemplu. Nu repeta aceeași idee cu alte
  cuvinte ca să lungești.
- Fără negări absolute („X nu e problema", „nu ține de Y"). Nuanțează:
  „nu ține doar de X".
- Fără fraze care sună frumos, dar nu spun nimic. Dacă n-ai spune fraza
  așa, vorbind cu o prietenă, rescrie-o.
- Paragrafe de 3-5 propoziții, nu o propoziție pe rând. Fără emoji, fără
  semnul exclamării, fără liste cu buline.
- Ton și adresare din câmpul 8. Folosește cuvintele din câmpul 9 și
  evită-le pe cele interzise. Textele din câmpul 10 sunt doar model de
  ton: nu le copia fraze întregi.
- Postarea se încheie cu o întrebare la care cineva poate răspunde în
  câteva secunde (da/nu, o alegere simplă, un număr), în acord cu ce am
  scris la câmpul 6.
- Lungimea: cea din câmpul 12. Dacă nu e precizată, 350-450 de cuvinte.
- Scrie cuvintele românești în loc de cele englezești, ori de câte ori
  există.

Dă-mi, în ordine:
1. Postarea, gata de copiat.
2. 3-5 hashtag-uri, specifice acestei postări (nu cele generale, folosite
   de toată lumea).
3. „Nota faptelor": lista faptelor afirmate în postare, fiecare legată de
   rândul din câmpul 5 de unde vine. Dacă ai folosit [DE COMPLETAT: ...],
   spune-o aici.
~~~

**Ce primești înapoi:** postarea, hashtag-urile și nota faptelor. Citește nota înainte de postare: dacă un fapt din ea nu are un rând în câmpul 5, ai prins o problemă.

**Notă:** textul rezultat nu e „perfect" și nu e gata de postat. Urmează verificarea, la Prompturile 4-9, în conversații separate.

---

## Prompt 4 — Fapte inventate

**Când îl folosești:** primul pas de verificare, mereu. Dacă faptele nu trec, restul nu mai contează, pentru că oricum rescrii.

**Ce completezi:** deschizi **conversația B** (nouă, goală). Lipești câmpul 5 din Fișă (doar acela) și postarea.

**Promptul:**

~~~
Ești un verificator de fapte. Nu ai scris postarea de mai jos și nu o
aperi. Cauți ce e afirmat și nu e adevărat sau nu se poate dovedi pe baza
listei mele.

FAPTELE MELE ADEVĂRATE (singurele lucruri pe care postarea are voie să
le afirme despre mine și afacerea mea):
[LIPEȘTE AICI CÂMPUL 5 DIN FIȘĂ]

POSTAREA:
[LIPEȘTE AICI POSTAREA, DOAR TEXTUL]

Ce faci:
1. Citește postarea frază cu frază. Scoate fiecare afirmație concretă
   despre mine, afacerea mea, clienții mei, proiecte, ani, prețuri,
   rezultate, cifre. Scoate și orice afirmație despre lumea din afară:
   companii, studii, legi, statistici, „cei mai mulți", „cercetările
   arată".
2. Pentru fiecare, citează fraza și răspunde: SE REGĂSEȘTE (spune în ce
   rând din lista mea) sau NU SE REGĂSEȘTE.
3. Păreri, opinii și situații generale care nu pretind că s-au întâmplat
   cuiva anume nu sunt fapte. Dar „am ajutat un client", „un client mi-a
   spus", orice cifră și orice nume de companie sunt fapte.
4. Orice NU SE REGĂSEȘTE înseamnă DE REPARAT. Nu există „observații
   opționale".

Reguli:
- Nu repara textul inventând un fapt. Pentru fiecare problemă mă întrebi:
  „E adevărat? Dacă da, adaugă-l în câmpul 5 și rulează din nou. Dacă nu,
  scoate fraza." Poți propune și o variantă a frazei fără faptul în
  discuție.
- Dacă lista mea e goală, oprește-te și spune-mi că nu poți verifica.
- Nu judeca stilul, tonul sau gramatica. Doar faptele.

Răspunde în formatul:
VERDICT FAPTE: ÎN REGULĂ | DE REPARAT
Afirmații verificate: [fiecare cu citat și SE REGĂSEȘTE / NU SE REGĂSEȘTE]
Probleme: [numerotate: citat → întrebarea pentru mine → varianta fără fapt]
~~~

**Ce primești înapoi:** un verdict și lista afirmațiilor, fiecare cu un semn clar. La „DE REPARAT" trimiți problemele la Promptul 10.

**Notă:** verificatorul compară postarea cu lista ta, atât. Nu poate ști dacă lista însăși e adevărată. Asta e răspunderea ta, de la câmpul 5.

---

## Prompt 5 — Limba și cuvintele interzise

**Când îl folosești:** după Promptul 4, în aceeași conversație B.

**Ce completezi:** câmpurile 7, 8 și 9 din Fișă și postarea (dacă ai corectat-o între timp, versiunea nouă).

**Promptul:**

~~~
Ești un corector de limbă română. Nu ai scris postarea de mai jos și nu
o aperi. Cauți greșeli și ce nu respectă regulile mele.

REGULILE MELE:
Ce NU vreau să apară (câmpul 7): [LIPEȘTE AICI]
Ton și adresare (câmpul 8): [LIPEȘTE AICI]
Cuvinte folosite și cuvinte interzise (câmpul 9): [LIPEȘTE AICI]

POSTAREA:
[LIPEȘTE AICI POSTAREA, DOAR TEXTUL]

Verifică, în ordine:
1. Cuvinte din lista „nu folosesc niciodată", subiecte sau promisiuni
   din „ce NU vreau să apară".
2. Adresare: postarea folosește consecvent „tu" sau „dumneavoastră",
   conform câmpului 8?
3. Diacritice: ș și ț cu virgulă (nu cu sedilă), ă, â, î puse corect.
4. Ghilimele românești „...", nu "...". Cratime corecte („n-am",
   „într-o", „s-a"). Virgulă înainte de „dar" și „ci", și după o
   subordonată pusă în față.
5. Acord (subiect–predicat, gen, număr) și timp verbal consecvent.
6. Cuvinte englezești care au echivalent românesc. Calcuri din engleză.
7. Emoji, semnul exclamării, liste cu buline fără rost.
8. Expresii de AI: „în lumea de azi", „în era digitală", „hai să
   explorăm", „game-changer".

Reguli:
- Nu rescrie postarea. Dă doar lista de greșeli.
- Fiecare greșeală: citatul exact → forma corectă. Nu există observații
  opționale: ori e greșeală, ori nu.
- Nu atinge faptele și nu schimba sensul.

Răspunde în formatul:
VERDICT LIMBĂ: ÎN REGULĂ | DE REPARAT
Probleme: [numerotate: citat → ce pui în loc]
~~~

**Ce primești înapoi:** un verdict și o listă scurtă de greșeli, fiecare cu varianta corectă. La „DE REPARAT" ajung la Promptul 10.

**Notă:** un asistent AI mai scapă greșeli de limbă, mai ales virgulele. Citește tu textul o dată, cu voce tare, înainte de postare.

---

## Prompt 6 — Închiderea, lungimea, hashtag-urile

**Când îl folosești:** ultimul din conversația B.

**Ce completezi:** câmpurile 6 și 12 și postarea.

**Promptul:**

~~~
Ești un verificator de format pentru postări de LinkedIn. Nu ai scris
postarea și nu o aperi.

CE VREAU SĂ FACĂ CITITORUL (câmpul 6): [LIPEȘTE AICI]
RITM ȘI LUNGIME (câmpul 12): [LIPEȘTE AICI]

POSTAREA (cu hashtag-urile la sfârșit):
[LIPEȘTE AICI POSTAREA]

Verifică:
1. Lungimea: numără cuvintele din corpul postării (fără hashtag-uri).
   Spune numărul și dacă se încadrează în lungimea din câmpul 12. Dacă nu
   ești sigur de numărare, scrie „aproximativ" și spune-mi să verific
   într-un contor de cuvinte.
2. Întrebarea de final: există una? Se poate răspunde în câteva secunde
   (da/nu, o alegere simplă, un număr)? Dacă e o întrebare deschisă, care
   cere un răspuns lung, e DE REPARAT.
3. Se potrivește închiderea cu ce vreau să facă cititorul (câmpul 6)?
4. Hashtag-uri: între 3 și 5, specifice acestei postări. Cele generale,
   pe care le pune oricine, sunt DE REPARAT.
5. Postarea are o singură idee și un singur exemplu? Dacă are două
   idei sau două exemple, spune care.

Reguli:
- Nu rescrie postarea și nu scrie tu întrebarea. Spui doar ce e greșit și
  cum ar trebui să fie.
- Nu există observații opționale.

Răspunde în formatul:
VERDICT FORMAT: ÎN REGULĂ | DE REPARAT
Cuvinte: [număr]
Probleme: [numerotate: citat → ce trebuie schimbat]
~~~

**Ce primești înapoi:** numărul de cuvinte, un verdict și, dacă e cazul, 2-3 probleme.

**Notă:** numărul de cuvinte dat de un asistent AI este adesea aproximativ. Dacă ești aproape de limită, lipește textul într-un contor de cuvinte.

---

## Prompt 7 — Unde s-ar opri cititorul

**Când îl folosești:** primul din **conversația A**: o conversație nouă, goală. Aici NU lipești Fișa și nu spui nimic despre tine.

**Ce completezi:** doar postarea (fără hashtag-uri și fără titlu).

**Promptul:**

~~~
Ești un om care dă scroll pe LinkedIn seara, pe telefon. Ai propria ta
treabă, dar nu ești din IT. N-ai auzit niciodată de cel care a scris
postarea și nu știi nimic despre el. Nu știi ce a vrut să spună: știi doar
ce e scris.

Mai jos e o postare. Citește-o o singură dată, ca pe telefon, și răspunde
doar pe baza a ce ai înțeles din ea.

POSTAREA:
[LIPEȘTE AICI DOAR TEXTUL POSTĂRII]

Verifică:
1. Primele 2-3 rânduri: ai apăsa „Vezi mai mult"? Înțelegi despre ce e
   vorba fără să citești restul?
2. Ideea principală: o poți spune într-o propoziție, cu cuvintele tale,
   după o singură citire? Dacă nu poți, e NECLAR.
3. Cuvinte pe care nu le înțelegi: termeni tehnici, nume neexplicate,
   englezisme.
4. Repetiții: același punct spus de două ori cu alte cuvinte. Citează
   ambele locuri.
5. Salturi de logică: o concluzie care nu decurge din ce era înainte.
6. Orice îndemn („încearcă...", „notează...") care nu-ți spune exact ce
   să faci.
7. Întrebarea de final: știi exact ce ți se cere să răspunzi, în câteva
   secunde? Ai răspunde?
8. Fiecare frază: are sens luată singură? Ai spune-o așa, vorbind?
9. Unde te-ai opri din citit sau ai începe să sari rânduri?

Reguli:
- Nu judeca stilul, faptele sau strategia. Doar dacă se înțelege.
- Nu ghici ce a vrut autorul. Dacă tu nu ai înțeles, e problemă a
  textului.
- Orice frază pe care a trebuit s-o citești de două ori, care sună
  frumos, dar nu spune nimic concret, sau care sună ciudat în română
  vorbită, înseamnă NECLAR. Nu există observații opționale.

Răspunde în formatul:
VERDICT: CLAR | NECLAR
Ce am înțeles: [ideea postării, într-o propoziție, cu cuvintele tale]
Unde m-aș opri: [citatul exact | „am citit până la capăt"]
Probleme: [numerotate: citat → de ce te-a încurcat. Sau „niciuna"]
~~~

**Ce primești înapoi:** ce a înțeles „cititorul", locul exact unde s-ar opri, și problemele numerotate.

**Notă:** compară „Ce am înțeles" cu ce voiai tu să spui. Dacă sunt diferite, postarea nu spune ce crezi că spune, chiar dacă verdictul e CLAR. Dacă „Unde m-aș opri" e înainte de întrebarea de final, mulți cititori reali s-ar opri tot acolo.

---

## Prompt 8 — Verificarea hook-ului

**Când îl folosești:** în conversația A, după Promptul 7. Hook-ul e partea care decide dacă postarea e citită.

**Ce completezi:** doar postarea.

**Promptul:**

~~~
Ești un editor care citește doar începutul postărilor de LinkedIn, adică
primele 2-3 rânduri, cele care se văd înainte de „Vezi mai mult". Nu ai
scris postarea și nu o aperi.

POSTAREA:
[LIPEȘTE AICI DOAR TEXTUL POSTĂRII]

Verifică începutul după aceste reguli:
1. Pornește dintr-o observație concretă sau o situație? Sau dintr-o
   generalizare largă, greu de susținut („cei mai mulți...",
   „majoritatea...", „toată lumea...")? Generalizarea e DE REPARAT.
2. Începe cu o definiție sau cu o explicație? E DE REPARAT.
3. Ideea centrală se înțelege din primele 2 rânduri? Dacă nu, e DE
   REPARAT.
4. Conține o negare absolută („X nu e problema", „nu ține de Y")? E DE
   REPARAT. Se nuanțează: „nu ține doar de X".
5. Sună a vorbire, ca o frază spusă la cafea, sau a text de reclamă?
6. Te face să vrei să citești mai departe? Spune sincer.

Reguli:
- Dacă hook-ul e DE REPARAT, propune 2 variante noi. Variantele folosesc
  DOAR ce e deja în postare: nu adaugi fapte, cifre sau exemple noi.
- Nu rescrie restul postării.
- Nu există observații opționale.

Răspunde în formatul:
VERDICT HOOK: BUN | DE REPARAT
Primele rânduri citate: [textul exact]
Probleme: [numerotate: citat → regula încălcată]
Variante (doar dacă e DE REPARAT): [2 variante, doar cu ce e în postare]
~~~

**Ce primești înapoi:** un verdict, regula încălcată și, dacă e nevoie, două variante de început.

**Notă:** cele două variante sunt sugestii. Alege una, dar citește tot textul din nou: un hook nou poate lăsa pe loc propoziții care acum nu mai leagă.

---

## Prompt 9 — Fraze goale și negări absolute

**Când îl folosești:** în conversația A, după Promptul 8. Prinde ce scapă de obicei la prima citire: fraze care sună bine, dar nu spun nimic.

**Ce completezi:** doar postarea.

**Promptul:**

~~~
Ești un editor strict. Nu ai scris postarea de mai jos și nu o aperi.
Cauți fraze care nu spun nimic concret și afirmații prea tari.

POSTAREA:
[LIPEȘTE AICI DOAR TEXTUL POSTĂRII]

Caută și citează exact:
1. Fraze care sună frumos, dar nu spun nimic (de exemplu: „îți poate
   spune ceva util", „ai mai mult din tine", „se așază mai bine").
2. Construcții nefirești în română vorbită (de exemplu: „Tu da.", „omul
   care o are de dus").
3. Nuanțări de umplutură (de exemplu: „Ține și de asta, sigur.", „Ideea
   pe care o luăm des de bună e că...").
4. Negări absolute care neagă complet un factor real („X nu e problema",
   „nu contează Y", „nu ține de Z"). Spune cum se nuanțează: „nu ține
   doar de Z".
5. Tiparul „nu X, ci Y" folosit de mai mult de 2 ori.
6. Comparații defensive cu alții („majoritatea celor din domeniu fac X,
   eu fac Y").
7. Mai mult de două exemple înșirate la rând.
8. Aceeași idee spusă de două ori, cu alte cuvinte.

Reguli:
- Pentru fiecare problemă: citatul exact → de ce e o problemă → ce pui în
  loc, folosind doar ce e deja în text. Dacă fraza nu are ce să spună,
  propune scoaterea ei.
- Nu adăuga fapte, cifre sau exemple noi.
- Nu rescrie toată postarea.
- Nu există observații opționale.

Răspunde în formatul:
VERDICT SENS: ÎN REGULĂ | DE REPARAT
Probleme: [numerotate: citat → de ce → ce pui în loc. Sau „niciuna"]
~~~

**Ce primești înapoi:** o listă scurtă de fraze de scos sau de reformulat, fiecare cu o propunere.

**Notă:** dacă asistentul nu găsește nimic, nu înseamnă că textul e perfect. Citește-l tu o dată cu gândul „așa aș spune și la cafea?".

---

## Prompt 10 — Repararea

**Când îl folosești:** când unul din Prompturile 4-9 a dat „DE REPARAT" sau „NECLAR". Repară exact punctele numite, nu mai mult.

**Ce completezi:** numele afacerii, Fișa, postarea și problemele (lipite exact cum le-ai primit, din toate verificările).

**Promptul:**

~~~
Ești agentul de text pentru [numele afacerii tale], pe LinkedIn, în
română vorbită. Repari o postare pe baza unor probleme numite de
verificatori. Nu rescrii de la zero ce a trecut deja.

FIȘA MEA DE BRAND:
[LIPEȘTE AICI FIȘA COMPLETATĂ]

POSTAREA ACTUALĂ:
[LIPEȘTE AICI POSTAREA]

PROBLEMELE DE REPARAT (copiate din verificări):
[LIPEȘTE AICI PROBLEMELE, CU CITATELE]

Reguli:
1. Repari exact punctele numite. Ce nu e pe listă rămâne cuvânt cu cuvânt
   cum e.
2. Despre mine și afacerea mea afirmi DOAR ce e în câmpul 5. Nu repari o
   problemă inventând un fapt. Dacă o reparație cere un fapt pe care
   nu-l ai, scrii [DE COMPLETAT: ce fapt îți trebuie] sau scoți fraza.
3. Dacă o problemă cere un răspuns de la mine (de exemplu „e adevărat?"),
   nu ghici. Întreabă-mă și oprește-te.
4. Nu schimbi lungimea cu mai mult de câteva cuvinte, față de câmpul 12.
5. Păstrează tonul, adresarea și cuvintele din Fișă.

Dă-mi, în ordine:
1. Postarea reparată, gata de copiat (cu 3-5 hashtag-uri).
2. „Revizie": lista modificărilor, punct cu punct: problema → ce ai
   schimbat.
3. „Nota faptelor": faptele afirmate, fiecare legată de rândul din
   câmpul 5.
~~~

**Ce primești înapoi:** postarea reparată, lista modificărilor și nota faptelor.

**Notă:** după reparare, verifici din nou în conversații NOI (A și B), nu în cea în care ai reparat. **Maximum două reparații.** Dacă după a doua tot ai probleme, decizi tu: postezi cu ce ai, sau renunți la postarea asta și iei altă idee de la Promptul 2.

---

## Cât de sigur e sistemul

- Pachetul reduce riscul ca o postare să conțină lucruri inventate sau neclare. Nu îl elimină.
- Verificarea e mai puțin independentă decât într-o echipă de agenți separați. Conversația nouă ajută, dar tot același tip de asistent verifică.
- Tu rămâi ultima verificare, mai ales la fapte. Asistentul nu poate ști dacă ce ai scris la câmpul 5 e adevărat.
- Pachetul nu promite urmăritori, vizualizări sau clienți. Te ajută să scrii și să verifici postări, atât.
