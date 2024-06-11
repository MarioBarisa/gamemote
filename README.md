Gamenote - videogame tracking system

# OSNOVE GAMENOTE
Gamenote je specijalizirani web servis za osobnu uporabu koji olakšava praćenje odigranih videoigara.
Gamenote omogućava korisniku da unese u sustav sve videoigre koje je igrao,
te da na jednom mjestu ima lijepo strukturiranu listu svoje zbirke videoigara. Korisnik unosi osnovne informacije
kao što su; naslov videoigre, platforma na kojoj je videoigra igrana, sati u videoigri, žanr videoigre, izdavač, ocjena korisnika za videoigru, osobne bilješke korisnika.
Kao povratnu informaciju korisnik dobiva lijepo strukturiranu listu te uz nju razne analitičke prikaze "profila igrača" kao što je piechart žanrova videoigara,  ili najzastupljenije platforme.

# KALSE

Videoigra ( id_videoigra, ime, ocjena, žanr, platforma, sati_u_videoigir,)

# Koristene tehnologije
BACKEND - Flask sa SQLAlchemy, render_template, request, redirect, url_for, jsonify, request te defaultdict ( iz bibiloteke collections )
FRONTEND - HTML i CSS ( Bootstrap 5 ) te Vanilla JavaScript za sortiranje tablice prema specificiranim stupcima
ANALIZA - apexcharts.js kao alternativa chart.js (nema neke razlike, moja osobna preferencija)

# Funkcionalnosti
- Dodavanje odigranih videoigara te njihovi atributi
- Sortiranje prema zelji ( ime, ocjena, id, playtime)
- Analiza profila igraca
- Brisanje videoigre iz liste
  
