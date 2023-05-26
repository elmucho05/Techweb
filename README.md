# TechWeb

- una piattaforma di film in streaming stile Netlifx
- i film vengono divisi per categorie categorie
- gli utenti possono essere guest o registrati (utenti paganti): in caso di utenti guest il loro utilizzo è limitato a vedere solo le         locandine dei film ma senza poter avviare la produzione del film stesso, al contrario gli utenti paganti con abbonamento valido
hanno la possibilità di vedere qualsiasi film
- gli utenti registrati avranno la possibilità di potere cambiare il proprio avatar nella loro pagina profilo
- gli utenti registrati possono inserire dei commenti sotto un film
- i film possono essere inseriti solo dall'amministratore del sito
- semplice motore di ricerca dei film per nome
- i film vengono consigliati agli utenti (registrati)
- gli utenti possono mettere nei preferiti dei film per poi vederli in seguito
- gli utenti potranno disdire l'abbonamento in qualsiasi momento 

Feature aggiuntive (obbligatorio)
- gli utenti (registrati) possono inserire un film all'interno della piattaforma
- i film possono essere inclusi nell'abbonamento (quindi "gratuiti" per gli utenti) oppure possono essere comprati a parte
- aggiungere oltre ai film le serie TV con relative stagioni ed episodi
- i film vengono valutati dagli utenti (registrati) con una valutazione da 1 a 5
- sistema di raccomandazione dei titoli basato sulla history dei titoli visti
- dashboard per utenti con possibilità di aggiornare i propri dati personali, visualizzare la history dei film visti, dei commenti effettuati, delle valutazioni fatte, visualizzare lo stato dell'abbonamento ...


## Prerequisiti
1. Installare pip
  - Linux `python3 -m pip install --user --upgrade pip`
  - Windows `py -m pip install --upgrade pip`

2. Installare Virtualenv
  - Linux `python3 -m pip install --user virtualenv`
  - Windows `py -m pip install --user virtualenv`

3. Creare l'ambiente virtuale
  - Linux `python3 -m venv venv`  
  - Windows `py -m venv env`

4. Attivare l'ambiente virtuale
  - Linux `source venv/venv`
  - Windows `.\venv\Scripts\activate`

5. Installare le dipendenze
  - Linux `python3 -m pip install -r requirements.txt`
  - Windows `py -m pip install -r requirements.txt`
