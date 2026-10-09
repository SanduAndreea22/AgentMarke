# Descrieri din fișier (nume provizoriu) — Analiză

> Etapa 1 (Descoperire), făcută de `produs-descoperire` pe 2026-10-09.
> Direcția a fost aprobată de Andreea pe 2026-10-09, **cu rezerve**: vezi
> „Decizia Andreei”. Sursele au fost verificate pe 2026-10-09.

## Ideea inițială (formularea Andreei)

„Agent pentru descrieri de produse — Primește un catalog și generează
descrieri, titluri și texte de promovare pentru magazine online.”

## Răspunsurile Andreei la întrebările de clarificare

1. **Public:** nu are acces direct la proprietari de magazine online sau la
   freelanceri. Nu presupune cerere doar pentru că ideea pare utilă. Vrea un
   public cu o problemă repetitivă, ușor de demonstrat, la care se poate
   valida disponibilitatea de a plăti.
2. **Catalog:** fișier CSV sau Excel la intrare, fișier gata de verificat la
   ieșire. Datele originale rămân neatinse. Lipsurile se semnalează, nimic
   nu se inventează.
3. **Format:** no-code. Nu ține neapărat la prompturi sau la un agent
   conversațional. Produsul trebuie să fie practic, ușor de demonstrat și
   reutilizabil pentru mai mulți clienți.

## Concluziile cercetării

### Concurența

- **Gomag** are „Gomag Prompt” ([blog Gomag](https://www.gomag.ro/blog/gomag-prompt-editor-pagini-noi-integrari-noutati/)).
  **MerchantPro** are „AI Generator”, cu diacritice și aprobare manuală
  ([MerchantPro](https://www.merchantpro.ro/app/ai_generator)). Pentru
  magazinele de pe aceste platforme, nevoia e deja acoperită.
- **Shopify Magic** e inclus în plan, dar româna nu e printre limbile
  oficiale ([App Store](https://apps.shopify.com/built-in-features/magic-product-descriptions),
  [eesel.ai](https://www.eesel.ai/blog/shopify-magic-language-support)).
- **WooCommerce:** există pluginuri (de ex. [DraftLab](https://wordpress.org/plugins/draftlab-ai-bulk-description-generator-woocommerce/)),
  dar cer cheie de API sau instalare.
- **Generatoarele gratuite** (Ahrefs, AfterShip) lucrează produs cu produs,
  prin formular. N-am găsit niciunul care să primească un fișier și să
  semnaleze lipsurile.
- **Imobiliare:** Storia are „AI Parameters”, care completează câmpuri, nu
  scrie descrieri ([StartupCafe](https://startupcafe.ro/olx-se-apropie-de-pragul-de-1-miliard-usd-venituri-dupa-un-an-de-crestere-cu-28-ai-ul-scrie-anunturi-stabileste-preturi-si-recruteaza-candidati-pe-platformele-din-romania-102463)).
  Un generator de descrieri pe Storia sau imobiliare.ro **nu am găsit**.

### Publicuri candidate

| Public | Ce am găsit | Ce rezultă |
|---|---|---|
| Magazine mici | Joburi plătite pentru descrieri ([Hipo](https://www.hipo.ro/locuri-de-munca/locuri_de_munca/271537/), [Upwork](https://www.upwork.com/freelance-jobs/apply/Shopify-Set-Good-with-images_~022051469126083413372/)). Gomag și MerchantPro acoperă deja nevoia | plan B: doar magazinele pe Shopify sau WooCommerce |
| eMAG Marketplace | AI deja folosit masiv ([Economedia](https://economedia.ro/?p=349191)); Base.com acoperă listarea | slab |
| **Agenți imobiliari** | Studiu Storia, 2026, 3.007 respondenți: 39,6% dintre profesioniști ar vrea un asistent care scrie descrierea ([StartupCafe](https://startupcafe.ro/51-dintre-profesionistii-imobiliari-care-folosesc-ai-spun-ca-economisesc-timp-cum-utilizeaza-romanii-tehnologia-la-vanzarea-si-cumpararea-locuintelor-studiu-103689)). Contactul apare pe anunț | **ales pentru test** |
| Freelanceri / asistenți virtuali | Plătesc pentru descrieri, dar mai ales pe piața în engleză | slab |

**La niciun public n-am găsit un semn public că ar plăti.**

### Variante no-code comparate în etapa 1

- **(a) Prompturi + fișier încărcat în ChatGPT sau Claude.** Se
  construiește în 1 weekend și e reutilizabil. Limite de verificat:
  răspunsurile lungi se pot opri la jumătate, iar diacriticele se pot
  strica în CSV.
- **(b) Google Sheets cu funcție AI.** Româna nu apare printre limbile
  confirmate ([Workspace Updates](https://workspaceupdates.googleblog.com/2025/09/ai-function-google-sheets-new-languages.html)).
  Limită: 350 de celule pe rulare ([Google Help](https://support.google.com/docs/answer/15877199)).
- **(c) Make, Zapier sau n8n + API, rulate de Andreea.** Nu cere nimic
  tehnic de la client, dar înseamnă muncă pentru fiecare client, deci
  devine serviciu.
- **(d) Custom GPT sau Claude Project.** Nu e confirmat dacă un utilizator
  ChatGPT Free poate deschide un GPT primit prin link. Un Claude Project se
  poate partaja doar în planurile Team și Enterprise.

### Costuri

- Generarea prin API costă aproximativ 0,10–2 $ la 100 de anunțuri.
  Estimarea e de verificat.
- Costurile reale sunt abonamentele (Claude Pro sau ChatGPT Plus, 20 $ pe
  lună, [claude.com/pricing](https://claude.com/pricing)) și timpul
  Andreei.

## Decizia Andreei (2026-10-09)

- **Acceptă agenții imobiliari ca public de testat.** Nu consideră validată
  nici cererea, nici forma de produs „set de prompturi”.
- **Etapa 2 trebuie să definească:** problema concretă, utilizatorul exact
  și diferența față de folosirea directă a ChatGPT sau Claude.
- **Întâi un prototip pentru uz propriu.** Se testează pe câteva anunțuri:
  - produce texte utile?
  - păstrează toate informațiile factuale?
  - semnalează clar ce lipsește?
- **Abia apoi:** o demonstrație scurtă și discuții cu potențiali clienți,
  ca să aflăm dacă problema îi deranjează suficient încât să plătească. Nu
  se construiește produsul complet înainte de test.
- **Setul de prompturi nu e automat soluția.** Se compară cu alternativele
  no-code și se recomandă varianta cea mai simplă pentru utilizator, cu
  costuri mici și vandabilă la mai mulți clienți.
- **Coordonatorul a adăugat:** fără mesaje comerciale nesolicitate pe
  WhatsApp, la numerele din anunțuri. Contactul se face prin LinkedIn sau
  prin emailul agenției.
