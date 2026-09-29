# Testul de rezistență al identității vizuale — Andreea Tech

> **Status: CONFIRMAT de Andreea** (2026-09-29) — cele 5 reguli sunt
> trecute în `brand_fundatie.md` (secțiunea 7) și în `sabloane.md`.
> Testează ce e definit în `brand_fundatie.md` (culori, fonturi, logo
> ales) și `sabloane.md`. **Limită importantă:** logo-ul nou (monograma
> „AT" cu bară comună) e ales, dar **nu e desenat** — îl testez după
> specificație, nu după un desen. Logo-ul vechi de pe site e testat pe
> fișierul real (`andreeatech/static/website/logo.png`).
> Contrastele sunt calculate (formula WCAG), nu estimate.

## Datele de bază

| Combinație | Contrast | Verdict |
|---|---|---|
| Bleumarin `#10173D` pe `#EBEEF8` | 14,9 : 1 | excelent |
| Albastru `#2743B8` pe `#EBEEF8` | 7,0 : 1 | bun, și pentru text mic |
| Alb pe albastru `#2743B8` | 8,1 : 1 | bun |
| Albastru `#2743B8` pe bleumarin `#10173D` | **2,1 : 1** | **slab — nu se folosesc împreună** |
| Fundal `#EBEEF8` pe alb | **1,16 : 1** | **se pierde — pe hârtie albă nu se vede** |

În alb-negru: bleumarin → gri 25 (aproape negru), albastru → gri 72
(gri închis), fundal → gri 238 (aproape alb). **Albastrul și bleumarinul
devin două griuri închise, greu de deosebit.**

## Logo-ul vechi — test rapid

Pică în 4 din 5 situații: degradeul și sclipirea dispar la tipar
alb-negru, ornamentele și liniile de circuit devin pete la favicon și nu
se pot broda, literele serif subțiri se rup la dimensiuni mici. Confirmă
decizia de a-l înlocui.

## Cele 5 situații — identitatea nouă

### 1. Pe ecranul unui telefon

- **Ce merge:** contraste mari; Archivo gros se citește bine; poza 4:5
  ocupă ecranul.
- **Ce se poate pierde:** titlul de pe poza de postare, dacă e prea mic
  sau prea lung; pe **modul întunecat** (dark mode) al LinkedIn, fundalul
  `#EBEEF8` al pozei iese ca un dreptunghi foarte luminos.
- **Cea mai mică ajustare:** titlu minimum 64 px pe poza de 1080 px (e
  deja în `sabloane.md`) și **o variantă a monogramei albă pe `#2743B8`**
  pentru poza de profil — arată bine și pe fundal deschis, și pe întunecat.

### 2. Pe o carte de vizită tipărită

- **Ce merge:** monograma plată, bleumarinul și albastrul se tipăresc
  fidel.
- **Ce se poate pierde:** fundalul `#EBEEF8` tipărit iese **gri murdar
  sau deloc** (contrast 1,16 față de alb); textul Inter sub 7 pt se
  îneacă.
- **Cea mai mică ajustare:** carte de vizită pe **carton alb**, fără
  fundal colorat; accentul albastru doar pe monogramă sau pe o linie;
  text minimum 8 pt.

### 3. Pe un tricou brodat

- **Ce merge:** monograma fără ornamente, cu linii groase și egale, e
  potrivită pentru broderie.
- **Ce se poate pierde:** golul din interiorul lui „A" se umple de fir
  dacă monograma e mică; descriptorul „Digital Products & Experiences" nu
  se poate broda lizibil; Italiana (subțire) nu se brodează deloc.
- **Cea mai mică ajustare:** pe textil **doar monograma**, minimum
  **4 cm lățime**, o singură culoare de fir; niciodată marca combinată
  cu descriptor.

### 4. Ca favicon mic (16-32 px)

- **Ce merge:** o monogramă de două litere e formatul corect pentru
  favicon.
- **Ce se poate pierde:** la **16 px**, bara comună A–T și vârful lui
  „A" se pot contopi într-o pată; „AT" poate fi citit ca „A" + o linie.
- **Cea mai mică ajustare:** o **versiune separată pentru 16 px** —
  linii puțin mai groase, spațiu puțin mai mare în interiorul lui „A",
  albă pe fundal albastru `#2743B8` (pătrat plin, nu contur). Se verifică
  pe desen, după ce monograma e redesenată ca SVG.

### 5. Material tipărit alb-negru

- **Ce merge:** monograma într-o singură culoare rămâne identică.
- **Ce se poate pierde:** **tot ce se bazează doar pe culoare** —
  accentul albastru devine gri închis lângă textul aproape negru; pe
  poza Luni/Joi, bateria „plină" vs. „goală" se deosebește doar dacă
  diferența e de **formă** (segmente pline vs. contur), nu doar de
  culoare. Cutia de preț din ofertă nu mai iese în evidență.
- **Cea mai mică ajustare:** regulă nouă — **accentul nu poartă singur
  un înțeles**: orice element evidențiat în albastru e evidențiat și
  prin grosime, mărime sau formă (ex. prețul din ofertă: Archivo 800,
  24 pt — deja mai mare decât restul, deci trece).

## Ajustările, pe scurt (5 reguli noi)

1. Monograma are **3 variante**: bleumarin pe deschis, **albă pe
   albastru** (poză de profil, favicon), negru pur (tipar alb-negru,
   broderie).
2. **Fundalul `#EBEEF8` doar pe ecran** — la tipar, fundal alb.
3. **Favicon de 16 px desenat separat**, cu linii îngroșate.
4. **Broderie: doar monograma**, minimum 4 cm, o culoare.
5. **Accentul albastru nu e niciodată singurul semnal** — merge mereu
   împreună cu grosime, mărime sau formă. Albastrul nu stă pe bleumarin
   (contrast 2,1).
