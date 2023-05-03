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
- gli utenti (registrati) possono inserire un film inviando una richiesta all'amministratore e questo potrà decidere se accettare o no di inserirlo nel catalogo
- i film possono essere inclusi nell'abbonamento (quindi "gratuiti" per gli utenti) oppure essere noleggiati con una piccola somma aggiuntiva
- aggiungere oltre ai film le serie TV con relative stagioni ed episodi
- i film vengono valutati dagli utenti (registrati) con una valutazione da 1 a 5
- sistema di raccomandazione dei film  “chi ha visto questo film ha guardato anche...”
- dashboard per utenti con possibilità di aggiornare i propri dati personali, visualizzare la history dei film visti, dei commenti effettuati, delle valutazioni fatte, visualizzare lo stato dell'abbonamento ...

# TODO List
1. creazione di un abbonamento
2. gli utenti potranno disdire l'abbonamento in qualsiasi momento dalla dashboard
3. gli utenti (registrati) possono inserire un film inviando una richiesta all'amministratore e questo potrà decidere se accettare o no di    inserirlo nel catalogo
4. i film possono essere inclusi nell'abbonamento (quindi "gratuiti" per gli utenti) oppure essere noleggiati con una piccola somma aggiuntiva
5. i film vengono consigliati agli utenti (registrati)

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
