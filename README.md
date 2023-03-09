# Calculatrice Python
Application de calculatrice en Python

## Lancer l'application
Depuis un terminal :
* `git clone https://github.com/VictorCyprien/calculatrice_python.git`
* `cd calculatrice_python/`

On crée un virtualenv
* `virtualenv venv`
* __Windows__
    * `source venv/Scripts/activate`
* __Linux__
    * `source venv/bin/activate`

Puis on installe les librairies
* `pip install -r requirements.txt`

## Générer l'application
* `pyinstaller.exe --onefile calculatrice.py`