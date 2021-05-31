# Smartphone analyzer

I dette projekt har vi tænkt os at vurdere forskellige mobiltelefoners popularitet fra Versus. Vi gør dette ved at scrape de forskellige oplysninger om mobiltelefonen vha. selenium fra Versus.com. Vi regner med at bruge bl.a. display, storage, RAM, camera & battery som vores feature vektor.

## List of used technologies
* Flask
* Pandas
* Numpy
* Matplotlib
* Request
* BS4
* CSV

## Installation guide
```bash
git clone project
```
###### MUST have python3 installed!

## User guide
###### Execute the following in this order:
#### data
```python
run python webscraping.py
run python rating.py
```
#### server
```python
run python Server.py
```
#### endpoints
```python
http://127.0.0.1:5000/avgprice/
http://127.0.0.1:5000/bestphonebestspecs/
http://127.0.0.1:5000/bestphoneformoney/
http://127.0.0.1:5000/worstphoneformoney/
http://127.0.0.1:5000/biggestandsmallest/
```

## Status
Vi kunne ikke anvende komplett's hjemmeside, da de ikke har udfyldt specifikationer på mange af deres telefoner. Derfor har vi i stedet anvendt versus.com.

Vi nåede ikke at besvare de sidste to problemstillinger, som involverer machine-learning.

## List of Challenges you have set up for your self
* Webscraping
* Manipulering af data
* Opsætning af klasser
* Opsætning af server
* Opsætning af endpoints
* Fremvisning af data gennem serveren


## Contributers
* cph-ha170
* cph-ah482